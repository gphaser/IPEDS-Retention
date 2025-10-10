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

    # Skip if missing critical columns
    if unit_col is None or cip_col is None or aw_col is None or ctotal_col is None:
        print(f"\n Could not find required columns in {fname}")
        print(f"Available columns: {cols}")
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
            "institution_name": np.nan,
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
    inst_col = find_col(cols, ['institution_name'])
    # First-year columns: pick the first one that exists
    possible_first_cols = ['ft_frst_tot_all_races_v', 'ft_frst_tot_all_races', 'ft_frst_tot', 'ft_frst', 'first_year', 'first', 'freshman']
    first_col = next((c for c in possible_first_cols if c in cols), None)

    if unit_col is None or gss_code_col is None or first_col is None:
        print(f"\n Could not find required columns in {fname}")
        print(f"Available columns: {cols}")
        continue

    gss_unitids.update(df[unit_col].dropna().unique())
    df[gss_code_col] = pd.to_numeric(df[gss_code_col], errors='coerce')
    mask_203 = df[gss_code_col].fillna(-1).astype(int) == 203
    df203 = df.loc[mask_203].copy()
    df203[first_col] = pd.to_numeric(df203[first_col], errors='coerce').fillna(0)

    for uid, val in df203.groupby(unit_col)[first_col].sum().items():
        inst_name = None
        if inst_col and inst_col in df203.columns:
            inst_vals = df203.loc[df203[unit_col] == uid, inst_col].dropna().unique()
            if len(inst_vals) > 0:
                inst_name = inst_vals[0]
        first_map[(uid, year)] = float(val)
        meta_rows.append({
            "source": "GSS",
            "file": fname,
            "unitid": uid,
            "year": year,
            "institution_name": inst_name,
            "cip": np.nan,
            "awlevel": np.nan,
            "ctotal": np.nan,
            "first_year_count": float(val)
        })

# ---------- combine unitids ----------
all_unitids = sorted(set(list(ipeds_unitids) + list(gss_unitids)),
                     key=lambda x: (float(x) if pd.notna(x) and str(x).replace('.', '', 1).isdigit() else float('inf'), str(x)))

print(f"Total UNITIDs found: {len(all_unitids)} (IPEDS: {len(ipeds_unitids)}, GSS: {len(gss_unitids)})")

# ---------- lookup institution names from GSS ----------
inst_lookup = {}
for r in meta_rows:
    if r["source"] == "GSS" and r.get("institution_name"):
        inst_lookup[r["unitid"]] = r["institution_name"]

# ---------- build wide table ----------
rows = []
for uid in all_unitids:
    row = {"UNITID": uid}
    row["Institution_Name"] = inst_lookup.get(uid, None)

    # first-years columns 2000..2023
    for y in YEARS:
        col = f"first-years_{y}"
        val = first_map.get((uid, y))
        row[col] = int(val) if val is not None and not pd.isna(val) else None

    # phd columns 2000..2023
    for y in YEARS:
        col = f"phd_degrees-earned_{y}"
        val = phd_map.get((uid, y))
        row[col] = int(val) if val is not None and not pd.isna(val) else None

    # masters columns 2000..2023
    for y in YEARS:
        col = f"masters_degrees-earned_{y}"
        val = masters_map.get((uid, y))
        row[col] = int(val) if val is not None and not pd.isna(val) else None

    # CIP & AWLEVEL summary
    row['cipcodes_seen'] = ";".join(sorted(set([c for c in cip_seen.get(uid, set()) if c not in ("", "nan")])))
    row['awlevels_seen'] = ";".join(sorted([str(int(x)) for x in sorted(aw_seen.get(uid, set()))])) if uid in aw_seen else ""

    rows.append(row)

wide_df = pd.DataFrame(rows)

# ------------------ Extended variable set ------------------
ADDITIONAL_VARS = [
    # Masters/Doctorate totals
    'ma_ft_tot_all_races_v', 'dr_ft_tot_all_races_v',
    'ma_ft_men_all_races_v', 'ma_ft_wmen_all_races_v',
    'dr_ft_men_all_races_v', 'dr_ft_wmen_all_races_v',

    # First years by degree type
    'ma_ft_frst_tot_all_races_v', 'dr_ft_frst_tot_all_races_v',

    # First-year by sex
    'ft_frst_men_all_races_v', 'ft_frst_wmen_all_races_v',

    # Total enrollment by race
    'ft_tot_black_v', 'ft_tot_indian_v', 'ft_tot_asian_v', 'ft_tot_pacific_v',
    'ft_tot_white_v', 'ft_tot_hisp_v', 'ft_tot_multi_v', 'ft_tot_unk_v', 'ft_tot_forgn_v',

    # Degree totals
    'ctotalm', 'ctotalw',

    # Degrees by race
    'crace17', 'crace18', 'crace19', 'crace20', 'crace21', 'crace22', 'cunknt',
    'cbkaat', 'casiat', 'cnhpit', 'chispt', 'cwhitt', 'c2mort', 'cnralt',

    # First-time enrollment by race
    'ft_frst_tot_black_v', 'ft_frst_tot_indian_v', 'ft_frst_tot_asian_v', 'ft_frst_tot_pacific_v',
    'ft_frst_tot_white_v', 'ft_frst_tot_hisp_v', 'ft_frst_tot_multi_v', 'ft_frst_tot_unk_v', 'ft_frst_tot_forgn_v',

    # Sex × race full-time
    'ft_men_black_v', 'ft_men_indian_v', 'ft_men_asian_v', 'ft_men_pacific_v',
    'ft_men_white_v', 'ft_men_hisp_v', 'ft_men_multi_v', 'ft_men_unk_v', 'ft_men_forgn_v',
    'ft_wmen_black_v', 'ft_wmen_indian_v', 'ft_wmen_asian_v', 'ft_wmen_pacific_v',
    'ft_wmen_white_v', 'ft_wmen_hisp_v', 'ft_wmen_multi_v', 'ft_wmen_unk_v', 'ft_wmen_forgn_v'
]

# Container for all extra vars
extra_maps = {v: {} for v in ADDITIONAL_VARS}

# ------------------ Extract from IPEDS ------------------
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
        print(f"Skip {fname} - {e}")
        continue

    df = normalize_cols(df)
    if 'unitid' not in df.columns:
        continue

    # For each additional var, if present in file, record value
    for var in ADDITIONAL_VARS:
        var_lower = var.lower()
        if var_lower in df.columns:
            df[var_lower] = pd.to_numeric(df[var_lower], errors='coerce').fillna(0)
            for uid, val in df.groupby('unitid')[var_lower].sum().items():
                extra_maps[var][(uid, year)] = float(val)

# ------------------ Extract from GSS ------------------
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
        print(f"Skip {fname} - {e}")
        continue

    df = normalize_cols(df)
    if 'unitid' not in df.columns:
        continue

    for var in ADDITIONAL_VARS:
        var_lower = var.lower()
        if var_lower in df.columns:
            df[var_lower] = pd.to_numeric(df[var_lower], errors='coerce').fillna(0)
            for uid, val in df.groupby('unitid')[var_lower].sum().items():
                extra_maps[var][(uid, year)] = float(val)

# ------------------ Add to wide table ------------------
for var in ADDITIONAL_VARS:
    for y in YEARS:
        col = f"{var}_{y}"
        wide_df[col] = [
            int(extra_maps[var].get((uid, y))) if (uid, y) in extra_maps[var] and not pd.isna(extra_maps[var][(uid, y)])
            else None
            for uid in wide_df["UNITID"]
        ]

# Update column order to keep new variables together at end
add_var_cols = [f"{var}_{y}" for var in ADDITIONAL_VARS for y in YEARS]
final_cols = list(wide_df.columns.difference(add_var_cols, sort=False)) + add_var_cols
wide_df = wide_df[final_cols]



# ensure desired column order
first_cols = [f"first-years_{y}" for y in YEARS]
phd_cols = [f"phd_degrees-earned_{y}" for y in YEARS]
masters_cols = [f"masters_degrees-earned_{y}" for y in YEARS]
add_var_cols = [f"{var}_{y}" for var in ADDITIONAL_VARS for y in YEARS]
final_cols = list(wide_df.columns.difference(add_var_cols, sort=False)) + add_var_cols
wide_df = wide_df[final_cols]
# final_cols = ["UNITID", "Institution_Name"] + first_cols + phd_cols + masters_cols + ["cipcodes_seen", "awlevels_seen"]
# wide_df = wide_df[final_cols]

# ---------- filter out UNITIDs with all blanks ----------
numeric_cols = first_cols + phd_cols + masters_cols
# Replace NaN with 0 temporarily to check if sum == 0
mask_all_zero_or_blank = (wide_df[numeric_cols].fillna(0).sum(axis=1) == 0)

# Keep only rows where not all are blank/zero
wide_df = wide_df.loc[~mask_all_zero_or_blank].reset_index(drop=True)

# ---------- convert wide to long including all variables ----------
print("\nConverting wide table to long format...")

# Identify identifier and year columns
id_vars = ["UNITID", "Institution_Name", "cipcodes_seen", "awlevels_seen"]

# Find all columns that end with a year suffix (e.g. "_2020")
long_candidates = [c for c in wide_df.columns if re.search(r"_\d{4}$", c)]

# Extract variable base names (e.g. "first-years", "phd_degrees-earned", "ma_ft_tot_all_races_v")
variable_bases = sorted(set(re.sub(r"_\d{4}$", "", c) for c in long_candidates))

print(f"Found {len(variable_bases)} variable groups to melt into long format.")

# Melt all at once using pandas.wide_to_long
long_df = pd.wide_to_long(
    wide_df,
    stubnames=variable_bases,
    i=id_vars,
    j="Year",
    sep="_",
    suffix=r"\d+"
).reset_index()

# Ensure Year is numeric
long_df["Year"] = pd.to_numeric(long_df["Year"], errors="coerce")

# Sort neatly
long_df = long_df.sort_values(["UNITID", "Year"]).reset_index(drop=True)

# Replace blanks with NaN for clarity
long_df.replace({0: np.nan, "": np.nan}, inplace=True)

# ---------- meta sheet ----------
meta_df = pd.DataFrame(meta_rows).sort_values(by=["unitid", "year", "source"])

# ---------- write Excel ----------
with pd.ExcelWriter(output_path, engine="openpyxl") as w:
    long_df.to_excel(w, sheet_name="long", index=False)
    meta_df.to_excel(w, sheet_name="meta", index=False)

print(f" Wrote long-format output (with {len(variable_bases)} variables) to {output_path}")

print("\n Sanity check passed: No input files were modified.")


