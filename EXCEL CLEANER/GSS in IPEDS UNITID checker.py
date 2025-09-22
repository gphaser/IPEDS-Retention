# CHECK UNITID"S FROM LIST OF GSS ONLY FROM PhD Completion checker
# SEE IF UNITID IS IN IPEDS DATA AT ALL
# SEE IF IN IPEDS WITH 40.08xxx designation (between 40.08 and 40.0899)
# See if in IPEDS WITH 40.08xxx and AWLEVEL 9,17
# See if in IPEDS WITH 40.08xx and AWLEVEL 7 
# Export to excel with numbers


import pandas as pd
import os

# === USER INPUTS ===
GSS_FILE = "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/GSS_combined_file.xlsx"   # change to .csv if needed
IPEDS_FOLDER = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/"         # folder containing files like c2001_a.xlsx
OUTPUT_FILE = "/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_check.xlsx"

# === LOAD GSS FILE ===
if GSS_FILE.endswith(".csv"):
    gss = pd.read_csv(GSS_FILE, dtype={"UNITID": str})
else:
    gss = pd.read_excel(GSS_FILE, dtype={"UNITID": str})

if "UNITID" not in gss.columns or "Year" not in gss.columns:
    raise ValueError("GSS file must contain UNITID and Year columns")

# === LOAD & COMBINE IPEDS FILES ===
ipeds_list = []
for f in os.listdir(IPEDS_FOLDER):
    if not (f.endswith(".csv") or f.endswith(".xlsx")):
        continue
    if not f.startswith("c"):
        continue

    year_str = f[1:5]
    if not year_str.isdigit():
        continue
    year = int(year_str)

    file_path = os.path.join(IPEDS_FOLDER, f)
    if f.endswith(".csv"):
        df = pd.read_csv(file_path, dtype={"UNITID": str})
    else:
        df = pd.read_excel(file_path, dtype={"UNITID": str})

    df["Year"] = year
    ipeds_list.append(df)

if not ipeds_list:
    raise ValueError("No valid IPEDS files found in folder")

ipeds = pd.concat(ipeds_list, ignore_index=True)

# Ensure required columns exist
required_cols = {"UNITID", "CIPCODE", "AWLEVEL", "Year"}
missing = required_cols - set(ipeds.columns)
if missing:
    raise ValueError(f"IPEDS missing required columns: {missing}")

ipeds["CIPCODE"] = ipeds["CIPCODE"].astype(str).str.strip()

# === PROCESS Year BY Year and Write to Excel ===
with pd.ExcelWriter(OUTPUT_FILE, engine="xlsxwriter") as writer:
    for year in sorted(gss["Year"].unique()):
        gss_year = gss[gss["Year"] == year][["UNITID", "Year"]].drop_duplicates()
        ipeds_year = ipeds[ipeds["Year"] == year]

        # 1. In IPEDS at all
        gss_year["In_IPEDS"] = gss_year["UNITID"].isin(ipeds_year["UNITID"]).astype(int)

        # 2. In IPEDS with CIP 40.08xxx
        ipeds_408 = ipeds_year[ipeds_year["CIPCODE"].str.startswith("40.08")]
        gss_year["In_40.08xxx"] = gss_year["UNITID"].isin(ipeds_408["UNITID"]).astype(int)

        # 3. In 40.08xxx with AWLEVEL 9 or 17
        ipeds_408_aw917 = ipeds_408[ipeds_408["AWLEVEL"].isin([9, 17])]
        gss_year["In_40.08xxx_AW_9_17"] = gss_year["UNITID"].isin(ipeds_408_aw917["UNITID"]).astype(int)

        # 4. In 40.08xxx with AWLEVEL 7
        ipeds_408_aw7 = ipeds_408[ipeds_408["AWLEVEL"] == 7]
        gss_year["In_40.08xxx_AW_7"] = gss_year["UNITID"].isin(ipeds_408_aw7["UNITID"]).astype(int)

        # Add final row with column sums
        sums = gss_year.drop(columns=["UNITID", "Year"]).sum(numeric_only=True)
        sums_row = pd.DataFrame([["TOTAL", year] + sums.tolist()],
                                columns=gss_year.columns)
        gss_year = pd.concat([gss_year, sums_row], ignore_index=True)

        # Write each year’s sheet
        gss_year.to_excel(writer, sheet_name=str(year), index=False)

print(f"Done! Results saved to {OUTPUT_FILE}")









''' OLD WAY
import pandas as pd
import os

# === USER INPUTS ===
GSS_FILE = "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/GSS_combined_file.xlsx"   # change to .csv if needed
IPEDS_FOLDER = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/"         # folder containing files like c2001_a.xlsx
OUTPUT_FILE = "/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_check.xlsx"

# === LOAD GSS FILE ===
if GSS_FILE.endswith(".csv"):
    gss = pd.read_csv(GSS_FILE, dtype={"UNITID": str})
else:
    gss = pd.read_excel(GSS_FILE, dtype={"UNITID": str})

if "UNITID" not in gss.columns or "Year" not in gss.columns:
    raise ValueError("GSS file must contain UNITID and Year columns")

# === LOAD & COMBINE IPEDS FILES ===
ipeds_list = []
for f in os.listdir(IPEDS_FOLDER):
    if not (f.endswith(".csv") or f.endswith(".xlsx")):
        continue
    if not f.startswith("c"):
        continue

    year_str = f[1:5]
    if not year_str.isdigit():
        continue
    year = int(year_str)

    file_path = os.path.join(IPEDS_FOLDER, f)
    if f.endswith(".csv"):
        df = pd.read_csv(file_path, dtype={"UNITID": str})
    else:
        df = pd.read_excel(file_path, dtype={"UNITID": str})

    df["Year"] = year
    ipeds_list.append(df)

if not ipeds_list:
    raise ValueError("No valid IPEDS files found in folder")

ipeds = pd.concat(ipeds_list, ignore_index=True)

# Ensure required columns exist
required_cols = {"UNITID", "CIPCODE", "AWLEVEL", "Year"}
missing = required_cols - set(ipeds.columns)
if missing:
    raise ValueError(f"IPEDS missing required columns: {missing}")

ipeds["CIPCODE"] = ipeds["CIPCODE"].astype(str).str.strip()

# === PROCESS Year BY Year ===
all_results = []
for year in sorted(gss["Year"].unique()):
    gss_year = gss[gss["Year"] == year][["UNITID", "Year"]].drop_duplicates()
    ipeds_year = ipeds[ipeds["Year"] == year]

    # 1. In IPEDS at all
    gss_year["In_IPEDS"] = gss_year["UNITID"].isin(ipeds_year["UNITID"]).astype(int)

    # 2. In IPEDS with CIP 40.08xxx
    ipeds_408 = ipeds_year[ipeds_year["CIPCODE"].str.startswith("40.08")]
    gss_year["In_40.08xxx"] = gss_year["UNITID"].isin(ipeds_408["UNITID"]).astype(int)

    # 3. In 40.08xxx with AWLEVEL 9 or 17
    ipeds_408_aw917 = ipeds_408[ipeds_408["AWLEVEL"].isin([9, 17])]
    gss_year["In_40.08xxx_AW_9_17"] = gss_year["UNITID"].isin(ipeds_408_aw917["UNITID"]).astype(int)

    # 4. In 40.08xxx with AWLEVEL 7
    ipeds_408_aw7 = ipeds_408[ipeds_408["AWLEVEL"] == 7]
    gss_year["In_40.08xxx_AW_7"] = gss_year["UNITID"].isin(ipeds_408_aw7["UNITID"]).astype(int)

    all_results.append(gss_year)

# Combine all years together
final = pd.concat(all_results, ignore_index=True)

# === EXPORT TO EXCEL ===
final.to_excel(OUTPUT_FILE, index=False)
print(f"Done! Results saved to {OUTPUT_FILE}")
''' 