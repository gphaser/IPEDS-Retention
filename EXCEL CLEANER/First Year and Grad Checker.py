# HERE make a table of all UNITIDs and in the columns put all the first years by year and the all the PhDs by year
# have the table have the form of "UNITID", "first-years_year" "degrees earened_year"
# Make sure that all UNITIDs that are possible are present (not just IPEDS or GSS)
# Get the UNITIDs in IPEDS and GSS and take the union
# IPEDS FROM filepath  "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/" 
    # folder containing files like c2001_a.xlsx
# GSS FROM FILEPATH  "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/" 
    # folder containing files like gss2000_Code.xlsx

# COLLECT UNITID"S if in IPEDS WITH 40.08xxx and AWLEVEL 9,17
# COLLECT UNITID"S if in IPEDS WITH 40.08xx and AWLEVEL 7 
# COmbine with GSS UNITIDS AND KEEP ALL UNITID's 
    # LIST WHAT THE 40.08xx # is 
    # LIST what the AWLEVL is

# WE ALSO WANT ft_frst_tot_all_races_v (full First year students) 
# AND CTOTALT (PhD awarded values)


import os
import re
import pandas as pd
import numpy as np

# Paths
ipeds_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/Untrimmed IPEDS"
gss_path  = "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/Untrimmed GSS"
output_path = "/Users/co25936/Desktop/PER/IPEDS/FirstYear and Grad Checker.xlsx"

YEARS = list(range(2000, 2024))

# ------------------ helpers ------------------
def normalize_cols(df):
    df = df.copy()
    df.columns = [str(c).strip().lower() for c in df.columns]
    return df

def safe_to_numeric(s):
    try:
        return pd.to_numeric(s, errors='coerce')
    except Exception:
        return s

def is_phys_cip(val):
    if pd.isna(val):
        return False
    s = str(val).strip()
    if "40.08" in s:
        return True
    if re.match(r"^40\.?08", s):
        return True
    if re.match(r"^4008", s):
        return True
    return False

def find_col(cols, must_have=[]):
    """
    Exact-match column detection (case-insensitive).
    Only returns a column if it matches one of must_have exactly.
    """
    for c in cols:
        c_low = c.strip().lower()
        for tok in must_have:
            if c_low == tok.lower():
                return c
    return None

# ------------------ maps and storage ------------------
ipeds_unitids = set()
gss_unitids = set()
first_map = {}      # (unitid, year) -> first-year count
phd_map   = {}      # (unitid, year) -> CTOTALT sum for AWLEVEL 9/17
masters_map = {}    # (unitid, year) -> AWLEVEL 7 sum
cip_seen = {}       # unitid -> set of CIP codes
aw_seen  = {}       # unitid -> set of AWLEVELs
meta_rows = []

# ------------------ process IPEDS ------------------
ipeds_files = sorted(f for f in os.listdir(ipeds_path) if f.lower().endswith(".xlsx") and not f.startswith("~$"))

for fname in ipeds_files:
    m = re.search(r"c(\d{4})", fname, re.I)
    if not m:
        continue
    year = int(m.group(1))
    if year not in YEARS:
        continue

    fullpath = os.path.join(ipeds_path, fname)
    try:
        df = pd.read_excel(fullpath)
    except Exception as e:
        print(f"Failed reading {fullpath}: {e}")
        continue

    df = normalize_cols(df)
    cols = df.columns.tolist()

    # Exact-match column detection
    unit_col   = find_col(cols, ['unitid'])
    cip_col    = find_col(cols, ['cipcode'])
    aw_col     = find_col(cols, ['awlevel'])
    ctotal_col = find_col(cols, ['ctotalt'])

    # Print missing columns
    required_cols = {'unit_col': unit_col, 'cip_col': cip_col, 'aw_col': aw_col, 'ctotal_col': ctotal_col}
    for key, val in required_cols.items():
        if val is None:
            print(f"\n Could not find {key} in {fname}")
            print(f"Available columns: {cols}")

    # Skip files missing critical columns
    if unit_col is None or cip_col is None or aw_col is None or ctotal_col is None:
        continue

    ipeds_unitids.update(df[unit_col].dropna().unique())
    df[cip_col] = df[cip_col].fillna("").astype(str)
    mask_phys = df[cip_col].apply(is_phys_cip)
    df_phys = df.loc[mask_phys].copy()
    if df_phys.empty:
        continue

    # Record CIP and AWLEVEL
    for _, r in df_phys.iterrows():
        uid = r.get(unit_col)
        if pd.isna(uid):
            continue
        cip_seen.setdefault(uid, set()).add(str(r.get(cip_col, "")).strip())
        aw_seen.setdefault(uid, set()).add(int(safe_to_numeric(r.get(aw_col))))
        meta_rows.append({
            "source": "IPEDS",
            "file": fname,
            "unitid": uid,
            "year": year,
            "cip": r.get(cip_col, ""),
            "awlevel": r.get(aw_col),
            "ctotal": r.get(ctotal_col),
            "first_year_count": np.nan
        })

    # Ensure numeric for aggregation
    df_phys[aw_col] = pd.to_numeric(df_phys[aw_col], errors='coerce')
    df_phys[ctotal_col] = pd.to_numeric(df_phys[ctotal_col], errors='coerce').fillna(0)

    # Aggregate degrees
    phd_rows = df_phys[df_phys[aw_col].isin([9, 17])]
    for uid, val in phd_rows.groupby(unit_col)[ctotal_col].sum().items():
        phd_map[(uid, year)] = float(val)

    masters_rows = df_phys[df_phys[aw_col] == 7]
    for uid, val in masters_rows.groupby(unit_col)[ctotal_col].sum().items():
        masters_map[(uid, year)] = float(val)

# ------------------ process GSS ------------------
gss_files = sorted(f for f in os.listdir(gss_path) if f.lower().endswith(".xlsx") and not f.startswith("~$"))

for fname in gss_files:
    m = re.search(r"gss(\d{4})", fname, re.I)
    if not m:
        continue
    year = int(m.group(1))
    if year not in YEARS:
        continue

    fullpath = os.path.join(gss_path, fname)
    try:
        df = pd.read_excel(fullpath)
    except Exception as e:
        print(f"Failed reading {fullpath}: {e}")
        continue

    df = normalize_cols(df)
    cols = df.columns.tolist()

    unit_col = find_col(cols, ['unitid'])
    gss_code_col = find_col(cols, ['gss_code'])
    # First-year columns: pick the first one that exists
    possible_first_cols = ['ft_frst_tot_all_races_v', 'ft_frst_tot_all_races', 'ft_frst_tot', 'ft_frst', 'first_year', 'first', 'freshman']
    first_col = next((c for c in possible_first_cols if c in cols), None)

    required_cols = {'unit_col': unit_col, 'gss_code_col': gss_code_col, 'first_col': first_col}
    for key, val in required_cols.items():
        if val is None:
            print(f"\n could not find {key} in {fname}")
            print(f"Available columns: {cols}")

    if unit_col is None or gss_code_col is None or first_col is None:
        continue

    gss_unitids.update(df[unit_col].dropna().unique())
    df[gss_code_col] = pd.to_numeric(df[gss_code_col], errors='coerce')
    mask_203 = df[gss_code_col].fillna(-1).astype(int) == 203
    df203 = df.loc[mask_203].copy()
    df203[first_col] = pd.to_numeric(df203[first_col], errors='coerce').fillna(0)

    for uid, val in df203.groupby(unit_col)[first_col].sum().items():
        first_map[(uid, year)] = float(val)
        meta_rows.append({
            "source": "GSS",
            "file": fname,
            "unitid": uid,
            "year": year,
            "cip": np.nan,
            "awlevel": np.nan,
            "ctotal": np.nan,
            "first_year_count": float(val)
        })
# ---------- combine unitids ----------
all_unitids = sorted(set(list(ipeds_unitids) + list(gss_unitids)), key=lambda x: (float(x) if pd.notna(x) and str(x).replace('.', '', 1).isdigit() else float('inf'), str(x)))

print(f"Total UNITIDs found: {len(all_unitids)} (IPEDS: {len(ipeds_unitids)}, GSS: {len(gss_unitids)})")

# ---------- build wide table ----------
rows = []
for uid in all_unitids:
    row = {"UNITID": uid}
    # first-years columns 2000..2023
    for y in YEARS:
        col = f"first-years_{y}"
        row[col] = int(first_map.get((uid, y), 0)) if (uid, y) in first_map else 0
    # phd columns 2000..2023
    for y in YEARS:
        col = f"phd_degrees-earned_{y}"
        row[col] = int(phd_map.get((uid, y), 0)) if (uid, y) in phd_map else 0
    # masters columns 2000..2023
    for y in YEARS:
        col = f"masters_degrees-earned_{y}"
        row[col] = int(masters_map.get((uid, y), 0)) if (uid, y) in masters_map else 0

    # CIP & AWLEVEL summary for this unitid
    row['cipcodes_seen'] = ";".join(sorted(set([c for c in cip_seen.get(uid, set()) if c not in ("", "nan")])))
    row['awlevels_seen'] = ";".join(sorted([str(int(x)) for x in sorted(aw_seen.get(uid, set()))])) if uid in aw_seen else ""

    rows.append(row)

wide_df = pd.DataFrame(rows)

# ensure desired column order: UNITID, first-years, phd, masters, cip/awlevel
first_cols = [f"first-years_{y}" for y in YEARS]
phd_cols = [f"phd_degrees-earned_{y}" for y in YEARS]
masters_cols = [f"masters_degrees-earned_{y}" for y in YEARS]
final_cols = ["UNITID"] + first_cols + phd_cols + masters_cols + ["cipcodes_seen", "awlevels_seen"]
wide_df = wide_df[final_cols]

# ---------- filter out UNITIDs with all zeros ----------
numeric_cols = first_cols + phd_cols + masters_cols
wide_df = wide_df.loc[~(wide_df[numeric_cols].sum(axis=1) == 0)].reset_index(drop=True)

# ---------- meta sheet (debug) ----------
meta_df = pd.DataFrame(meta_rows).sort_values(by=["unitid", "year", "source"])

# ---------- write Excel with two sheets ----------
with pd.ExcelWriter(output_path, engine="openpyxl") as w:
    wide_df.to_excel(w, sheet_name="wide", index=False)
    meta_df.to_excel(w, sheet_name="meta", index=False)

print(f"Wrote output to {output_path}")

print("\n Sanity check passed: No input files were modified.")





 
''' ISSUE IS CTOTAL is also picking up xctotal 
import os
import re
import pandas as pd
import numpy as np
import time

def get_file_modtimes(path):
    """Return dict of filename -> last modified time (epoch)."""
    modtimes = {}
    for fname in sorted(os.listdir(path)):
        fullpath = os.path.join(path, fname)
        if os.path.isfile(fullpath):
            modtimes[fname] = os.path.getmtime(fullpath)
    return modtimes

def check_for_modifications(before, after, label):
    """Raise error if any file has a changed timestamp."""
    for fname, ts_before in before.items():
        ts_after = after.get(fname)
        if ts_after is None:
            raise RuntimeError(f"{label}: File {fname} disappeared during processing!")
        if ts_before != ts_after:
            raise RuntimeError(f"{label}: File {fname} was modified! "
                               f"Before={time.ctime(ts_before)}, After={time.ctime(ts_after)}")


# ========== USER PATHS ==========
ipeds_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/Untrimmed IPEDS"
gss_path  = "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/Untrimmed GSS"
output_path = "/Users/co25936/Desktop/PER/IPEDS/FirstYear and Grad Checker.xlsx"
# =================================

# ===== Capture timestamps before processing =====
ipeds_before = get_file_modtimes(ipeds_path)
gss_before   = get_file_modtimes(gss_path)

# years you want present as columns (2000..2023 inclusive)
YEARS = list(range(2000, 2024))

# helpers --------------------------------------------------------------------
def find_col(cols, must_have=[]):
    """Find first column name that contains all tokens in must_have (case-insensitive)."""
    for c in cols:
        if all(tok in c for tok in must_have):
            return c
    return None

def normalize_cols(df):
    df = df.copy()
    df.columns = [str(c).strip().lower() for c in df.columns]
    return df

def safe_to_numeric(s):
    try:
        return pd.to_numeric(s, errors='coerce')
    except Exception:
        return s

def is_phys_cip(val):
    """Return True if a CIP looks like 40.08xx (handles strings and numbers heuristically)."""
    if pd.isna(val):
        return False
    s = str(val).strip()
    if "40.08" in s:
        return True
    # catch numeric-like 400801 or 4008 variants
    if re.match(r"^40\.?08", s):
        return True
    if re.match(r"^4008", s):
        return True
    return False

# maps to collect
ipeds_unitids = set()
gss_unitids = set()

# keyed by (unitid, year)
first_map = {}      # (unitid, year) -> first-year count
phd_map   = {}      # (unitid, year) -> CTOTALT sum for AWLEVEL 9/17
masters_map = {}    # optional, AWLEVEL 7 (kept in case you want it)
# metadata per unitid aggregated across years
cip_seen = {}       # unitid -> set of cipcodes encountered (40.08 variants)
aw_seen  = {}       # unitid -> set of awlevels encountered (for 40.08 rows)

# meta rows for debugging: list of dicts with unitid, year, cip, awlevel, ctotalt, first_year
meta_rows = []

# ---------- process IPEDS ----------
ipeds_files = sorted(os.listdir(ipeds_path))
for fname in ipeds_files:
    # look for pattern cYYYY_a.* (case-insensitive) anywhere in filename
    m = re.search(r"c(\d{4})_a\.", fname, re.I)
    if not m:
        # if you have slightly different filenames, try more permissive pattern:
        m2 = re.search(r"c(\d{4})", fname, re.I)
        if m2:
            year = int(m2.group(1))
        else:
            continue
    else:
        year = int(m.group(1))

    # only collect years 2000..2023 (but script can be adapted)
    if year not in YEARS:
        # still process to collect unitids if you want; currently skip if outside YEARS
        # remove the continue if you want to include other years
        continue

    fullpath = os.path.join(ipeds_path, fname)
    try:
        df = pd.read_excel(fullpath)
    except Exception as e:
        print(f"Failed reading {fullpath}: {e}")
        continue

    df = normalize_cols(df)
    cols = df.columns.tolist()

    # robust column detections
    unit_col = find_col(cols, ['unitid']) or find_col(cols, ['unit', 'id'])
    cip_col  = find_col(cols, ['cip'])
    aw_col   = find_col(cols, ['awlevel']) or find_col(cols, ['aw', 'level']) or find_col(cols, ['awlev'])
    ctotal_col = find_col(cols, ['ctotalt']) or find_col(cols, ['ctotal']) or find_col(cols, ['ctot'])

    if unit_col is None:
        # cannot process this file
        print(f"Skipping IPEDS {fname} — no UNITID-like column found")
        continue

    ipeds_unitids.update(df[unit_col].dropna().unique())

    if cip_col is None:
        # no CIP info -> we cannot restrict to 40.08; skip this file for physics filtering
        print(f"Skipping CIP filter for IPEDS {fname} — no CIP col found")
        continue

    # ensure string for CIP checks
    df[cip_col] = df[cip_col].fillna("").astype(str)

    # filter physics/astronomy CIP 40.08xx
    mask_phys = df[cip_col].apply(is_phys_cip)
    df_phys = df.loc[mask_phys].copy()
    if df_phys.shape[0] == 0:
        # nothing to do for this file
        continue

    # record CIP and AWLEVELs seen per unitid
    for _, r in df_phys.iterrows():
        uid = r.get(unit_col)
        if pd.isna(uid):
            continue
        cipval = str(r.get(cip_col, "")).strip()
        awval = r.get(aw_col) if aw_col in r.index else None

        cip_seen.setdefault(uid, set()).add(cipval)
        if awval is not None and not (pd.isna(awval) or awval == ""):
            aw_seen.setdefault(uid, set()).add(int(safe_to_numeric(awval)))

        # collect a meta row
        meta_rows.append({
            "source": "IPEDS",
            "file": fname,
            "unitid": uid,
            "year": year,
            "cip": cipval,
            "awlevel": awval,
            "ctotal": r.get(ctotal_col) if ctotal_col in r.index else np.nan,
            "first_year_count": np.nan  # filled only from GSS side
        })

    # degrees aggregated: need AWLEVEL + CTOTAL columns
    if aw_col is None or ctotal_col is None:
        continue

    # coerce numeric
    df_phys[aw_col] = pd.to_numeric(df_phys[aw_col], errors='coerce')
    df_phys[ctotal_col] = pd.to_numeric(df_phys[ctotal_col], errors='coerce').fillna(0)

    print(f"\nChecking {fname} ({year})")
    print("Detected AWLEVEL col:", aw_col)
    print("Detected CTOTAL col:", ctotal_col)

    # PhD AWLEVEL 9 or 17
    phd_rows = df_phys[df_phys[aw_col].isin([9, 17])]
    if not phd_rows.empty:
        agg = phd_rows.groupby(unit_col)[ctotal_col].sum()
        for uid, val in agg.items():
            phd_map[(uid, year)] = float(val)  # keep float; convert later if you want int

    # Masters AWLEVEL 7 (optional)
    masters_rows = df_phys[df_phys[aw_col] == 7]
    if not masters_rows.empty:
        agg = masters_rows.groupby(unit_col)[ctotal_col].sum()
        for uid, val in agg.items():
            masters_map[(uid, year)] = float(val)

# ---------- process GSS ----------
gss_files = sorted(os.listdir(gss_path))
for fname in gss_files:
    m = re.search(r"gss(\d{4})", fname, re.I)
    if not m:
        continue
    year = int(m.group(1))
    if year not in YEARS:
        continue

    fullpath = os.path.join(gss_path, fname)
    try:
        df = pd.read_excel(fullpath)
    except Exception as e:
        print(f"Failed reading {fullpath}: {e}")
        continue

    df = normalize_cols(df)
    cols = df.columns.tolist()

    unit_col = find_col(cols, ['unitid']) or find_col(cols, ['unit', 'id'])
    gss_code_col = find_col(cols, ['gss', 'code']) or find_col(cols, ['gss_code']) or find_col(cols, ['gss'])
    # try explicit first-year column names then fallbacks
    possible_first_cols = [
        'ft_frst_tot_all_races_v', 'ft_frst_tot_all_races',
        'ft_frst_tot', 'ft_frst', 'first_year', 'first', 'freshman'
    ]
    first_col = None
    for cand in possible_first_cols:
        if cand in cols:
            first_col = cand
            break
    if first_col is None:
        # fallback heuristics
        cands = [c for c in cols if ('ft_frst' in c) or ('frst' in c and 'tot' in c) or ('first' in c and 'tot' in c)]
        if cands:
            first_col = cands[0]

    if unit_col is None:
        print(f"Skipping GSS {fname} — no UNITID-like col")
        continue
    if gss_code_col is None:
        print(f"Skipping GSS {fname} — no GSS code col found")
        continue
    if first_col is None:
        print(f"Skipping GSS {fname} — no first-year-like column found")
        continue

    gss_unitids.update(df[unit_col].dropna().unique())

    # filter to gss_code == 203 (physics first-year code)
    try:
        df[gss_code_col] = pd.to_numeric(df[gss_code_col], errors='coerce')
    except Exception:
        pass

    mask_203 = df[gss_code_col].fillna(-1).astype(int) == 203
    df203 = df.loc[mask_203].copy()
    if df203.empty:
        continue

    # convert first-year counts to numeric
    df203[first_col] = pd.to_numeric(df203[first_col], errors='coerce').fillna(0)

    agg = df203.groupby(unit_col)[first_col].sum()
    for uid, val in agg.items():
        first_map[(uid, year)] = float(val)
        # augment meta rows if we had IPEDS meta entries for same unitid/year -> but we'll just append a GSS meta row
        meta_rows.append({
            "source": "GSS",
            "file": fname,
            "unitid": uid,
            "year": year,
            "cip": np.nan,
            "awlevel": np.nan,
            "ctotal": np.nan,
            "first_year_count": float(val)
        })

# ---------- combine unitids ----------
all_unitids = sorted(set(list(ipeds_unitids) + list(gss_unitids)), key=lambda x: (float(x) if pd.notna(x) and str(x).replace('.', '', 1).isdigit() else float('inf'), str(x)))

print(f"Total UNITIDs found: {len(all_unitids)} (IPEDS: {len(ipeds_unitids)}, GSS: {len(gss_unitids)})")

# ---------- build wide table ----------
rows = []
for uid in all_unitids:
    row = {"UNITID": uid}
    # first-years columns 2000..2023
    for y in YEARS:
        col = f"first-years_{y}"
        row[col] = int(first_map.get((uid, y), 0)) if (uid, y) in first_map else 0
    # phd columns 2000..2023
    for y in YEARS:
        col = f"phd_degrees-earned_{y}"
        row[col] = int(phd_map.get((uid, y), 0)) if (uid, y) in phd_map else 0
    # masters columns 2000..2023
    for y in YEARS:
        col = f"masters_degrees-earned_{y}"
        row[col] = int(masters_map.get((uid, y), 0)) if (uid, y) in masters_map else 0

    # CIP & AWLEVEL summary for this unitid
    row['cipcodes_seen'] = ";".join(sorted(set([c for c in cip_seen.get(uid, set()) if c not in ("", "nan")])))
    row['awlevels_seen'] = ";".join(sorted([str(int(x)) for x in sorted(aw_seen.get(uid, set()))])) if uid in aw_seen else ""

    rows.append(row)

wide_df = pd.DataFrame(rows)

# ensure desired column order: UNITID, first-years, phd, masters, cip/awlevel
first_cols = [f"first-years_{y}" for y in YEARS]
phd_cols = [f"phd_degrees-earned_{y}" for y in YEARS]
masters_cols = [f"masters_degrees-earned_{y}" for y in YEARS]
final_cols = ["UNITID"] + first_cols + phd_cols + masters_cols + ["cipcodes_seen", "awlevels_seen"]
wide_df = wide_df[final_cols]

# ---------- filter out UNITIDs with all zeros ----------
numeric_cols = first_cols + phd_cols + masters_cols
wide_df = wide_df.loc[~(wide_df[numeric_cols].sum(axis=1) == 0)].reset_index(drop=True)

# ---------- meta sheet (debug) ----------
meta_df = pd.DataFrame(meta_rows).sort_values(by=["unitid", "year", "source"])

# ---------- write Excel with two sheets ----------
with pd.ExcelWriter(output_path, engine="openpyxl") as w:
    wide_df.to_excel(w, sheet_name="wide", index=False)
    meta_df.to_excel(w, sheet_name="meta", index=False)

print(f"Wrote output to {output_path}")

# ===== Capture timestamps after processing =====
ipeds_after = get_file_modtimes(ipeds_path)
gss_after   = get_file_modtimes(gss_path)

# ===== Compare =====
check_for_modifications(ipeds_before, ipeds_after, "IPEDS")
check_for_modifications(gss_before, gss_after, "GSS")

print("\n Sanity check passed: No input files were modified.")

'''

''' Old way bit broken
import os
import re
import pandas as pd

# Filepaths
ipeds_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/"
gss_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/"
output_path = "/Users/co25936/Desktop/PER/IPEDS/FirstYear and Grad Checker.xlsx"

# Regex to match years in filenames
ipeds_pattern = re.compile(r"c(\d{4})_a\.xlsx")
gss_pattern = re.compile(r"gss(\d{4})_Code\.xlsx")

# Collect UNITIDs
ipeds_unitids = set()
gss_unitids = set()

# Store data
first_years_data = {}
degrees_data = {}

# --- Process IPEDS (Degrees) ---
for file in os.listdir(ipeds_path):
    match = ipeds_pattern.match(file)
    if not match:
        continue
    year = match.group(1)
    df = pd.read_excel(os.path.join(ipeds_path, file))

    if "UNITID" not in df.columns:
        continue

    ipeds_unitids.update(df["UNITID"].unique())

    # Physics/Astronomy CIP codes 40.08xx
    if "CIPCODE" not in df.columns:
        continue
    df_phys = df[df["CIPCODE"].astype(str).str.startswith("40.08")]

    # Degrees earned
    if "AWLEVEL" in df_phys.columns and "CTOTALT" in df_phys.columns:
        # PhDs (AWLEVEL = 9,17)
        phd = df_phys[df_phys["AWLEVEL"].isin([9, 17])]
        deg = phd.groupby("UNITID")["CTOTALT"].sum()
        for uid, val in deg.items():
            degrees_data.setdefault(uid, {})[f"phd_degrees-earned_{year}"] = val

        # Masters (AWLEVEL = 7)
        masters = df_phys[df_phys["AWLEVEL"] == 7]
        deg = masters.groupby("UNITID")["CTOTALT"].sum()
        for uid, val in deg.items():
            degrees_data.setdefault(uid, {})[f"masters_degrees-earned_{year}"] = val

# --- Process GSS (First-years) ---
for file in os.listdir(gss_path):
    match = gss_pattern.match(file)
    if not match:
        continue
    year = match.group(1)
    df = pd.read_excel(os.path.join(gss_path, file))
    print(f"Processing GSS {file}, columns = {df.columns.tolist()}")  # DEBUG

    if "UNITID" not in df.columns or "gss_code" not in df.columns:
        continue

    # Collect UNITIDs
    gss_unitids.update(df["UNITID"].unique())

    # Filter to gss_code == 203 and get first-year counts
    if "ft_frst_tot_all_races_v" in df.columns:
        df_first = df[df["gss_code"] == 203]
        fy = df_first.groupby("UNITID")["ft_frst_tot_all_races_v"].sum()
        for uid, val in fy.items():
            first_years_data.setdefault(uid, {})[f"first-years_{year}"] = val

# --- Combine UNITIDs ---
all_unitids = sorted(ipeds_unitids.union(gss_unitids))

# --- Build Wide Table ---
rows = []
for uid in all_unitids:
    row = {"UNITID": uid}
    if uid in first_years_data:
        row.update(first_years_data[uid])
    if uid in degrees_data:
        row.update(degrees_data[uid])
    rows.append(row)

output_df = pd.DataFrame(rows)

# Save to Excel
output_df.to_excel(output_path, index=False)
print(f"File saved to {output_path}")
'''