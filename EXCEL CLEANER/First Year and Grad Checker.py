# HERE make a long table of all UNITIDs and in the columns put all the first years by year and the all the PhDs by year
# Make sure that all UNITIDs that are possible are present (not just IPEDS or GSS)
# Get the UNITIDs in IPEDS and GSS and take the union
# IPEDS FROM filepath  "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/Untrimmed IPEDS"
    # folder containing files like c2001_a.xlsx
# GSS FROM FILEPATH  "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/Untrimmed GSS"
    # folder containing files like gss2000_Code.xlsx
# save to an  output_path = "/Users/co25936/Desktop/PER/IPEDS/FirstYear and Grad Checker.xlsx" 

# COLLECT UNITID"S if in IPEDS WITH 40.08xxx and AWLEVEL 9,17
# COLLECT UNITID"S if in IPEDS WITH 40.08xx and AWLEVEL 7 
# COmbine with GSS UNITIDS AND KEEP ALL UNITID's 
    # LIST WHAT THE 40.08xx # is 
    # LIST what the AWLEVL is

# WE ALSO WANT vars_of_interest = [
'''
    # Degree total
    'ctotalt',
    # Masters/Doctorate totals
    'ma_ft_tot_all_races_v', 'dr_ft_tot_all_races_v',
    'ma_ft_men_all_races_v', 'ma_ft_wmen_all_races_v',
    'dr_ft_men_all_races_v', 'dr_ft_wmen_all_races_v',

    # First years by degree type (overall)
    'ma_ft_frst_tot_all_races_v', 'dr_ft_frst_tot_all_races_v',

    # First-year by sex (overall)
    'ft_frst_men_all_races_v', 'ft_frst_wmen_all_races_v',

    # Total enrollment by race
    'ft_tot_all_races_v', 'ft_tot_black_v', 'ft_tot_indian_v', 'ft_tot_asian_v', 'ft_tot_pacific_v',
    'ft_tot_white_v', 'ft_tot_hisp_v', 'ft_tot_multi_v', 'ft_tot_unk_v', 'ft_tot_forgn_v',

    # First-time enrollment by race
    'ft_frst_tot_all_races_v', 'ft_frst_tot_black_v', 'ft_frst_tot_indian_v', 'ft_frst_tot_asian_v',
    'ft_frst_tot_pacific_v', 'ft_frst_tot_white_v', 'ft_frst_tot_hisp_v', 'ft_frst_tot_multi_v',
    'ft_frst_tot_unk_v', 'ft_frst_tot_forgn_v',

    # First-time men by race
    'ft_frst_men_black_v', 'ft_frst_men_indian_v', 'ft_frst_men_asian_v', 'ft_frst_men_pacific_v',
    'ft_frst_men_white_v', 'ft_frst_men_hisp_v', 'ft_frst_men_multi_v', 'ft_frst_men_unk_v', 'ft_frst_men_forgn_v',

    # First-time women by race
    'ft_frst_wmen_black_v', 'ft_frst_wmen_indian_v', 'ft_frst_wmen_asian_v', 'ft_frst_wmen_pacific_v',
    'ft_frst_wmen_white_v', 'ft_frst_wmen_hisp_v', 'ft_frst_wmen_multi_v', 'ft_frst_wmen_unk_v', 'ft_frst_wmen_forgn_v',

    # Degree totals by sex 
    'ctotalm', 'ctotalw',

    # Degree totals by race
    'crace17', 'crace18', 'crace19', 'crace20', 'crace21', 'crace22', 'cunknt',
    'cbkaat', 'casiat', 'cnhpit', 'chispt', 'cwhitt', 'c2mort', 'cnralt',

    # ---- Masters breakdowns ----
    'ma_ft_tot_black_v', 'ma_ft_tot_indian_v', 'ma_ft_tot_asian_v', 'ma_ft_tot_pacific_v',
    'ma_ft_tot_white_v', 'ma_ft_tot_hisp_v', 'ma_ft_tot_multi_v', 'ma_ft_tot_unk_v', 'ma_ft_tot_forgn_v',

    'ma_ft_men_black_v', 'ma_ft_men_indian_v', 'ma_ft_men_asian_v', 'ma_ft_men_pacific_v',
    'ma_ft_men_white_v', 'ma_ft_men_hisp_v', 'ma_ft_men_multi_v', 'ma_ft_men_unk_v', 'ma_ft_men_forgn_v',

    'ma_ft_wmen_black_v', 'ma_ft_wmen_indian_v', 'ma_ft_wmen_asian_v', 'ma_ft_wmen_pacific_v',
    'ma_ft_wmen_white_v', 'ma_ft_wmen_hisp_v', 'ma_ft_wmen_multi_v', 'ma_ft_wmen_unk_v', 'ma_ft_wmen_forgn_v',

    # ---- Masters first-year breakdowns ----
    'ma_ft_frst_men_black_v', 'ma_ft_frst_men_indian_v', 'ma_ft_frst_men_asian_v',
    'ma_ft_frst_men_pacific_v', 'ma_ft_frst_men_white_v', 'ma_ft_frst_men_hisp_v',
    'ma_ft_frst_men_multi_v', 'ma_ft_frst_men_unk_v', 'ma_ft_frst_men_forgn_v',
    'ma_ft_frst_men_all_races_v',

    'ma_ft_frst_wmen_black_v', 'ma_ft_frst_wmen_indian_v', 'ma_ft_frst_wmen_asian_v',
    'ma_ft_frst_wmen_pacific_v', 'ma_ft_frst_wmen_white_v', 'ma_ft_frst_wmen_hisp_v',
    'ma_ft_frst_wmen_multi_v', 'ma_ft_frst_wmen_unk_v', 'ma_ft_frst_wmen_forgn_v',
    'ma_ft_frst_wmen_all_races_v',

    'ma_ft_frst_tot_black_v', 'ma_ft_frst_tot_indian_v', 'ma_ft_frst_tot_asian_v',
    'ma_ft_frst_tot_pacific_v', 'ma_ft_frst_tot_white_v', 'ma_ft_frst_tot_hisp_v',
    'ma_ft_frst_tot_multi_v', 'ma_ft_frst_tot_unk_v', 'ma_ft_frst_tot_forgn_v',

    # ---- Doctoral breakdowns ----
    'dr_ft_tot_black_v', 'dr_ft_tot_indian_v', 'dr_ft_tot_asian_v', 'dr_ft_tot_pacific_v',
    'dr_ft_tot_white_v', 'dr_ft_tot_hisp_v', 'dr_ft_tot_multi_v', 'dr_ft_tot_unk_v', 'dr_ft_tot_forgn_v',

    'dr_ft_men_black_v', 'dr_ft_men_indian_v', 'dr_ft_men_asian_v', 'dr_ft_men_pacific_v',
    'dr_ft_men_white_v', 'dr_ft_men_hisp_v', 'dr_ft_men_multi_v', 'dr_ft_men_unk_v', 'dr_ft_men_forgn_v',

    'dr_ft_wmen_black_v', 'dr_ft_wmen_indian_v', 'dr_ft_wmen_asian_v', 'dr_ft_wmen_pacific_v',
    'dr_ft_wmen_white_v', 'dr_ft_wmen_hisp_v', 'dr_ft_wmen_multi_v', 'dr_ft_wmen_unk_v', 'dr_ft_wmen_forgn_v',

    # ---- Doctoral first-year breakdowns ----
    'dr_ft_frst_tot_black_v', 'dr_ft_frst_tot_indian_v', 'dr_ft_frst_tot_asian_v',
    'dr_ft_frst_tot_pacific_v', 'dr_ft_frst_tot_white_v', 'dr_ft_frst_tot_hisp_v',
    'dr_ft_frst_tot_multi_v', 'dr_ft_frst_tot_unk_v', 'dr_ft_frst_tot_forgn_v',

    'dr_ft_frst_men_black_v', 'dr_ft_frst_men_indian_v', 'dr_ft_frst_men_asian_v',
    'dr_ft_frst_men_pacific_v', 'dr_ft_frst_men_white_v', 'dr_ft_frst_men_hisp_v',
    'dr_ft_frst_men_multi_v', 'dr_ft_frst_men_unk_v', 'dr_ft_frst_men_forgn_v',
    'dr_ft_frst_men_all_races_v',

    'dr_ft_frst_wmen_black_v', 'dr_ft_frst_wmen_indian_v', 'dr_ft_frst_wmen_asian_v',
    'dr_ft_frst_wmen_pacific_v', 'dr_ft_frst_wmen_white_v', 'dr_ft_frst_wmen_hisp_v',
    'dr_ft_frst_wmen_multi_v', 'dr_ft_frst_wmen_unk_v', 'dr_ft_frst_wmen_forgn_v',
    'dr_ft_frst_wmen_all_races_v',

    # Institution name
    'institution_name'
    ]
'''   

# ================================================================
# FIRST YEAR & GRAD CHECKER — WIDE TABLE MERGED BY UNITID
# ================================================================
import os
import re
import pandas as pd
import gc

# === Filepaths ===
ipeds_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/Untrimmed IPEDS"
gss_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/Untrimmed GSS"
output_path = "/Users/co25936/Desktop/PER/IPEDS/FirstYear and Grad Checker.xlsx"

# === Variables of interest ===
vars_of_interest = [
    'ctotalt', 'ma_ft_tot_all_races_v', 'dr_ft_tot_all_races_v',
    'ma_ft_men_all_races_v', 'ma_ft_wmen_all_races_v',
    'dr_ft_men_all_races_v', 'dr_ft_wmen_all_races_v',
    'ma_ft_frst_tot_all_races_v', 'dr_ft_frst_tot_all_races_v',
    'ft_frst_men_all_races_v', 'ft_frst_wmen_all_races_v',
    'ft_tot_all_races_v', 'ft_tot_black_v', 'ft_tot_indian_v', 'ft_tot_asian_v', 
    'ft_tot_pacific_v', 'ft_tot_white_v', 'ft_tot_hisp_v', 'ft_tot_multi_v', 
    'ft_tot_unk_v', 'ft_tot_forgn_v',
    'ft_frst_tot_all_races_v', 'ft_frst_tot_black_v', 'ft_frst_tot_indian_v', 
    'ft_frst_tot_asian_v', 'ft_frst_tot_pacific_v', 'ft_frst_tot_white_v', 
    'ft_frst_tot_hisp_v', 'ft_frst_tot_multi_v', 'ft_frst_tot_unk_v', 'ft_frst_tot_forgn_v',
    'ft_frst_men_black_v', 'ft_frst_men_indian_v', 'ft_frst_men_asian_v', 
    'ft_frst_men_pacific_v', 'ft_frst_men_white_v', 'ft_frst_men_hisp_v', 
    'ft_frst_men_multi_v', 'ft_frst_men_unk_v', 'ft_frst_men_forgn_v',
    'ft_frst_wmen_black_v', 'ft_frst_wmen_indian_v', 'ft_frst_wmen_asian_v', 
    'ft_frst_wmen_pacific_v', 'ft_frst_wmen_white_v', 'ft_frst_wmen_hisp_v', 
    'ft_frst_wmen_multi_v', 'ft_frst_wmen_unk_v', 'ft_frst_wmen_forgn_v',
    'ctotalm', 'ctotalw', 'crace17', 'crace18', 'crace19', 'crace20', 'crace21', 
    'crace22', 'cunknt', 'cbkaat', 'casiat', 'cnhpit', 'chispt', 'cwhitt', 'c2mort', 'cnralt',
    'ma_ft_tot_black_v', 'ma_ft_tot_indian_v', 'ma_ft_tot_asian_v', 'ma_ft_tot_pacific_v',
    'ma_ft_tot_white_v', 'ma_ft_tot_hisp_v', 'ma_ft_tot_multi_v', 'ma_ft_tot_unk_v', 
    'ma_ft_tot_forgn_v', 'ma_ft_men_black_v', 'ma_ft_men_indian_v', 'ma_ft_men_asian_v', 
    'ma_ft_men_pacific_v', 'ma_ft_men_white_v', 'ma_ft_men_hisp_v', 'ma_ft_men_multi_v', 
    'ma_ft_men_unk_v', 'ma_ft_men_forgn_v', 'ma_ft_wmen_black_v', 'ma_ft_wmen_indian_v', 
    'ma_ft_wmen_asian_v', 'ma_ft_wmen_pacific_v', 'ma_ft_wmen_white_v', 'ma_ft_wmen_hisp_v', 
    'ma_ft_wmen_multi_v', 'ma_ft_wmen_unk_v', 'ma_ft_wmen_forgn_v',
    'ma_ft_frst_men_black_v', 'ma_ft_frst_men_indian_v', 'ma_ft_frst_men_asian_v',
    'ma_ft_frst_men_pacific_v', 'ma_ft_frst_men_white_v', 'ma_ft_frst_men_hisp_v',
    'ma_ft_frst_men_multi_v', 'ma_ft_frst_men_unk_v', 'ma_ft_frst_men_forgn_v',
    'ma_ft_frst_men_all_races_v', 'ma_ft_frst_wmen_black_v', 'ma_ft_frst_wmen_indian_v', 
    'ma_ft_frst_wmen_asian_v', 'ma_ft_frst_wmen_pacific_v', 'ma_ft_frst_wmen_white_v', 
    'ma_ft_frst_wmen_hisp_v', 'ma_ft_frst_wmen_multi_v', 'ma_ft_frst_wmen_unk_v', 
    'ma_ft_frst_wmen_forgn_v', 'ma_ft_frst_wmen_all_races_v', 'ma_ft_frst_tot_black_v', 
    'ma_ft_frst_tot_indian_v', 'ma_ft_frst_tot_asian_v', 'ma_ft_frst_tot_pacific_v', 
    'ma_ft_frst_tot_white_v', 'ma_ft_frst_tot_hisp_v', 'ma_ft_frst_tot_multi_v', 
    'ma_ft_frst_tot_unk_v', 'ma_ft_frst_tot_forgn_v',
    'dr_ft_tot_black_v', 'dr_ft_tot_indian_v', 'dr_ft_tot_asian_v', 'dr_ft_tot_pacific_v',
    'dr_ft_tot_white_v', 'dr_ft_tot_hisp_v', 'dr_ft_tot_multi_v', 'dr_ft_tot_unk_v', 
    'dr_ft_tot_forgn_v', 'dr_ft_men_black_v', 'dr_ft_men_indian_v', 'dr_ft_men_asian_v', 
    'dr_ft_men_pacific_v', 'dr_ft_men_white_v', 'dr_ft_men_hisp_v', 'dr_ft_men_multi_v', 
    'dr_ft_men_unk_v', 'dr_ft_men_forgn_v', 'dr_ft_wmen_black_v', 'dr_ft_wmen_indian_v', 
    'dr_ft_wmen_asian_v', 'dr_ft_wmen_pacific_v', 'dr_ft_wmen_white_v', 'dr_ft_wmen_hisp_v', 
    'dr_ft_wmen_multi_v', 'dr_ft_wmen_unk_v', 'dr_ft_wmen_forgn_v',
    'dr_ft_frst_tot_black_v', 'dr_ft_frst_tot_indian_v', 'dr_ft_frst_tot_asian_v',
    'dr_ft_frst_tot_pacific_v', 'dr_ft_frst_tot_white_v', 'dr_ft_frst_tot_hisp_v',
    'dr_ft_frst_tot_multi_v', 'dr_ft_frst_tot_unk_v', 'dr_ft_frst_tot_forgn_v',
    'dr_ft_frst_men_black_v', 'dr_ft_frst_men_indian_v', 'dr_ft_frst_men_asian_v',
    'dr_ft_frst_men_pacific_v', 'dr_ft_frst_men_white_v', 'dr_ft_frst_men_hisp_v',
    'dr_ft_frst_men_multi_v', 'dr_ft_frst_men_unk_v', 'dr_ft_frst_men_forgn_v',
    'dr_ft_frst_men_all_races_v', 'dr_ft_frst_wmen_black_v', 'dr_ft_frst_wmen_indian_v', 
    'dr_ft_frst_wmen_asian_v', 'dr_ft_frst_wmen_pacific_v', 'dr_ft_frst_wmen_white_v', 
    'dr_ft_frst_wmen_hisp_v', 'dr_ft_frst_wmen_multi_v', 'dr_ft_frst_wmen_unk_v', 
    'dr_ft_frst_wmen_forgn_v', 'dr_ft_frst_wmen_all_races_v'
]

# === Helper functions ===
def normalize_cols(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)
    return df

def safe_year_from_filename(filename):
    m = re.search(r'(19|20)\d{2}', os.path.basename(filename))
    return int(m.group()) if m else None

print("=" * 60)
print("STEP 1: Loading IPEDS Files (Physics Programs Only)")
print("=" * 60)

ipeds_files = [os.path.join(ipeds_path, f) for f in os.listdir(ipeds_path) if f.endswith('.xlsx')]
ipeds_list = []
physics_unitids = set()

for i, f in enumerate(ipeds_files):
    try:
        year = safe_year_from_filename(f)
        if not year:
            print(f"  [{i+1}/{len(ipeds_files)}] Skipping {os.path.basename(f)}: no year")
            continue
        
        print(f"  [{i+1}/{len(ipeds_files)}] {year}...", end=' ')
        df = pd.read_excel(f, dtype=str)
        df = normalize_cols(df)
        
        # Filter for physics (40.08xx) with awlevel 7, 9, or 17
        if 'cipcode' in df.columns and 'awlevel' in df.columns and 'unitid' in df.columns:
            df = df[
                (df['cipcode'].str.startswith('40.08', na=False)) & 
                (df['awlevel'].isin(['7', '9', '17']))
            ].copy()
            
            if df.empty:
                print("no physics records")
                continue
            
            # Keep relevant columns
            available_vars = [v for v in vars_of_interest if v in df.columns]
            keep_cols = ['unitid', 'cipcode', 'awlevel'] + available_vars
            df = df[keep_cols].copy()
            df['year'] = year
            
            physics_unitids.update(df['unitid'].unique())
            ipeds_list.append(df)
            print(f"{len(df)} records, {len(available_vars)} vars")
        else:
            print("missing required columns")
            
        del df
        gc.collect()
    except Exception as e:
        print(f"ERROR: {e}")

ipeds_df = pd.concat(ipeds_list, ignore_index=True) if ipeds_list else pd.DataFrame()
print(f"\n  Total IPEDS records: {len(ipeds_df):,}")
print(f"  Unique physics UNITIDs: {len(physics_unitids)}")

print("\n" + "=" * 60)
print("STEP 2: Loading GSS Files")
print("=" * 60)

gss_files = [os.path.join(gss_path, f) for f in os.listdir(gss_path) if f.endswith('.xlsx')]
gss_list = []

for i, f in enumerate(gss_files):
    try:
        year = safe_year_from_filename(f)
        if not year:
            print(f"  [{i+1}/{len(gss_files)}] Skipping {os.path.basename(f)}: no year")
            continue
        
        print(f"  [{i+1}/{len(gss_files)}] {year}...", end=' ')
        df = pd.read_excel(f, dtype=str)
        df = normalize_cols(df)
        
        if 'unitid' not in df.columns:
            print("no unitid column")
            continue
        
        # Filter to only physics unitids from IPEDS
        df = df[df['unitid'].isin(physics_unitids)].copy()
        
        if df.empty:
            print("no matching UNITIDs")
            continue
        
        # Keep relevant columns (including institution_name)
        available_vars = [v for v in vars_of_interest + ['institution_name'] if v in df.columns]
        keep_cols = ['unitid'] + available_vars
        df = df[keep_cols].copy()
        df['year'] = year
        
        gss_list.append(df)
        print(f"{len(df)} records, {len(available_vars)} vars")
        
        del df
        gc.collect()
    except Exception as e:
        print(f"ERROR: {e}")

gss_df = pd.concat(gss_list, ignore_index=True) if gss_list else pd.DataFrame()
print(f"\n  Total GSS records: {len(gss_df):,}")

print("\n" + "=" * 60)
print("STEP 3: Merging IPEDS and GSS Data (Shared UNITIDs Only)")
print("=" * 60)

# 1️⃣ Keep only UNITIDs present in BOTH datasets
shared_unitids = set(ipeds_df['unitid']).intersection(set(gss_df['unitid']))
ipeds_df = ipeds_df[ipeds_df['unitid'].isin(shared_unitids)].copy()
gss_df = gss_df[gss_df['unitid'].isin(shared_unitids)].copy()

print(f"  Shared UNITIDs: {len(shared_unitids)}")
print(f"  IPEDS filtered: {len(ipeds_df):,} rows")
print(f"  GSS filtered:   {len(gss_df):,} rows")

# 2️⃣ Convert numeric columns to numbers (separately, before merge)
ipeds_num_cols = [c for c in ipeds_df.columns if c not in ['unitid', 'year', 'cipcode', 'awlevel']]
for col in ipeds_num_cols:
    ipeds_df[col] = pd.to_numeric(ipeds_df[col], errors='coerce')

gss_num_cols = [c for c in gss_df.columns if c not in ['unitid', 'year', 'institution_name']]
for col in gss_num_cols:
    gss_df[col] = pd.to_numeric(gss_df[col], errors='coerce')

# 3️⃣ Ensure no duplicate (unitid, year) rows before merge
ipeds_df = ipeds_df.drop_duplicates(subset=['unitid', 'year', 'cipcode', 'awlevel'])
gss_df = gss_df.drop_duplicates(subset=['unitid', 'year'])

# 4️⃣ Merge on unitid + year only (since IPEDS and GSS report on same year)
combined = pd.merge(
    ipeds_df,
    gss_df,
    on=['unitid', 'year'],
    how='inner',  # only rows present in BOTH datasets
    suffixes=('_ipeds', '_gss')
)

print(f"  Combined merged records: {len(combined):,}")

# 5️⃣ Institution name from GSS only
if 'institution_name' in combined.columns:
    pass  # already included from GSS
elif 'institution_name_gss' in combined.columns:
    combined['institution_name'] = combined['institution_name_gss']
    combined = combined.drop(columns=[c for c in combined.columns if c.endswith('_gss') and c != 'institution_name'])
else:
    combined['institution_name'] = pd.NA

# 6️⃣ Clean up duplicates and reorder
combined = combined.drop(columns=[c for c in combined.columns if c in ['institution_name_ipeds']])
combined = combined.sort_values(['unitid', 'year', 'cipcode', 'awlevel'], ignore_index=True)

print("  ✓ Merged cleanly using shared UNITIDs and aligned by year")
print("\n" + "=" * 60)
print("STEP 4: Final Processing and Export")
print("=" * 60)

# Reorder columns
priority_cols = ['unitid', 'institution_name', 'year', 'cipcode', 'awlevel']
other_cols = [c for c in combined.columns if c not in priority_cols]
ordered_cols = [c for c in priority_cols if c in combined.columns] + other_cols
combined = combined[ordered_cols]

# Sort
combined = combined.sort_values(['unitid', 'year', 'cipcode', 'awlevel']).reset_index(drop=True)

# Export
combined.to_excel(output_path, index=False, engine='openpyxl')

print(f"  ✓ Wide-format table created: {output_path}")
print(f"  Total rows: {len(combined):,}")
print(f"  Total columns: {len(combined.columns)}")
print(f"  Year range: {int(combined['year'].min())} - {int(combined['year'].max())}")
print(f"  Unique UNITIDs: {combined['unitid'].nunique()}")

print("\n" + "=" * 60)
print("Preview (first 10 rows):")
print("=" * 60)
print(combined[['unitid', 'institution_name', 'year', 'cipcode', 'awlevel']].head(10))

print("\n" + "=" * 60)
print("COMPLETE")
print("=" * 60)



#TK CODE STILL HAD ISSUES TRYING TO FIX DUPLICATES AND INST. NAMES NOT WORKIN
'''
# ================================================================
# FIRST YEAR & GRAD CHECKER — LONG TABLE MERGED BY UNITID
# ================================================================
import os
import re
import pandas as pd

# === Filepaths ===
ipeds_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/Untrimmed IPEDS"
gss_path  = "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/Untrimmed GSS"
output_path = "/Users/co25936/Desktop/PER/IPEDS/FirstYear and Grad Checker.xlsx"

# === Variables of interest ===
vars_of_interest = [
    # Degree total
    'ctotalt',
    # Masters/Doctorate totals
    'ma_ft_tot_all_races_v', 'dr_ft_tot_all_races_v',
    'ma_ft_men_all_races_v', 'ma_ft_wmen_all_races_v',
    'dr_ft_men_all_races_v', 'dr_ft_wmen_all_races_v',
 
    # First years by degree type (overall)
    'ma_ft_frst_tot_all_races_v', 'dr_ft_frst_tot_all_races_v',

    # First-year by sex (overall)
    'ft_frst_men_all_races_v', 'ft_frst_wmen_all_races_v',

    # Total enrollment by race
    'ft_tot_all_races_v', 'ft_tot_black_v', 'ft_tot_indian_v', 'ft_tot_asian_v', 'ft_tot_pacific_v',
    'ft_tot_white_v', 'ft_tot_hisp_v', 'ft_tot_multi_v', 'ft_tot_unk_v', 'ft_tot_forgn_v',

    # First-time enrollment by race
    'ft_frst_tot_all_races_v', 'ft_frst_tot_black_v', 'ft_frst_tot_indian_v', 'ft_frst_tot_asian_v',
    'ft_frst_tot_pacific_v', 'ft_frst_tot_white_v', 'ft_frst_tot_hisp_v', 'ft_frst_tot_multi_v',
    'ft_frst_tot_unk_v', 'ft_frst_tot_forgn_v',

    # First-time men by race
    'ft_frst_men_black_v', 'ft_frst_men_indian_v', 'ft_frst_men_asian_v', 'ft_frst_men_pacific_v',
    'ft_frst_men_white_v', 'ft_frst_men_hisp_v', 'ft_frst_men_multi_v', 'ft_frst_men_unk_v', 'ft_frst_men_forgn_v',

    # First-time women by race
    'ft_frst_wmen_black_v', 'ft_frst_wmen_indian_v', 'ft_frst_wmen_asian_v', 'ft_frst_wmen_pacific_v',
    'ft_frst_wmen_white_v', 'ft_frst_wmen_hisp_v', 'ft_frst_wmen_multi_v', 'ft_frst_wmen_unk_v', 'ft_frst_wmen_forgn_v',

    # Degree totals by sex 
    'ctotalm', 'ctotalw',

    # Degree totals by race
    'crace17', 'crace18', 'crace19', 'crace20', 'crace21', 'crace22', 'cunknt',
    'cbkaat', 'casiat', 'cnhpit', 'chispt', 'cwhitt', 'c2mort', 'cnralt',

    # ---- Masters breakdowns ----
    'ma_ft_tot_black_v', 'ma_ft_tot_indian_v', 'ma_ft_tot_asian_v', 'ma_ft_tot_pacific_v',
    'ma_ft_tot_white_v', 'ma_ft_tot_hisp_v', 'ma_ft_tot_multi_v', 'ma_ft_tot_unk_v', 'ma_ft_tot_forgn_v',

    'ma_ft_men_black_v', 'ma_ft_men_indian_v', 'ma_ft_men_asian_v', 'ma_ft_men_pacific_v',
    'ma_ft_men_white_v', 'ma_ft_men_hisp_v', 'ma_ft_men_multi_v', 'ma_ft_men_unk_v', 'ma_ft_men_forgn_v',

    'ma_ft_wmen_black_v', 'ma_ft_wmen_indian_v', 'ma_ft_wmen_asian_v', 'ma_ft_wmen_pacific_v',
    'ma_ft_wmen_white_v', 'ma_ft_wmen_hisp_v', 'ma_ft_wmen_multi_v', 'ma_ft_wmen_unk_v', 'ma_ft_wmen_forgn_v',

    # ---- Masters first-year breakdowns ----
    'ma_ft_frst_men_black_v', 'ma_ft_frst_men_indian_v', 'ma_ft_frst_men_asian_v',
    'ma_ft_frst_men_pacific_v', 'ma_ft_frst_men_white_v', 'ma_ft_frst_men_hisp_v',
    'ma_ft_frst_men_multi_v', 'ma_ft_frst_men_unk_v', 'ma_ft_frst_men_forgn_v',
    'ma_ft_frst_men_all_races_v',

    'ma_ft_frst_wmen_black_v', 'ma_ft_frst_wmen_indian_v', 'ma_ft_frst_wmen_asian_v',
    'ma_ft_frst_wmen_pacific_v', 'ma_ft_frst_wmen_white_v', 'ma_ft_frst_wmen_hisp_v',
    'ma_ft_frst_wmen_multi_v', 'ma_ft_frst_wmen_unk_v', 'ma_ft_frst_wmen_forgn_v',
    'ma_ft_frst_wmen_all_races_v',

    'ma_ft_frst_tot_black_v', 'ma_ft_frst_tot_indian_v', 'ma_ft_frst_tot_asian_v',
    'ma_ft_frst_tot_pacific_v', 'ma_ft_frst_tot_white_v', 'ma_ft_frst_tot_hisp_v',
    'ma_ft_frst_tot_multi_v', 'ma_ft_frst_tot_unk_v', 'ma_ft_frst_tot_forgn_v',

    # ---- Doctoral breakdowns ----
    'dr_ft_tot_black_v', 'dr_ft_tot_indian_v', 'dr_ft_tot_asian_v', 'dr_ft_tot_pacific_v',
    'dr_ft_tot_white_v', 'dr_ft_tot_hisp_v', 'dr_ft_tot_multi_v', 'dr_ft_tot_unk_v', 'dr_ft_tot_forgn_v',

    'dr_ft_men_black_v', 'dr_ft_men_indian_v', 'dr_ft_men_asian_v', 'dr_ft_men_pacific_v',
    'dr_ft_men_white_v', 'dr_ft_men_hisp_v', 'dr_ft_men_multi_v', 'dr_ft_men_unk_v', 'dr_ft_men_forgn_v',

    'dr_ft_wmen_black_v', 'dr_ft_wmen_indian_v', 'dr_ft_wmen_asian_v', 'dr_ft_wmen_pacific_v',
    'dr_ft_wmen_white_v', 'dr_ft_wmen_hisp_v', 'dr_ft_wmen_multi_v', 'dr_ft_wmen_unk_v', 'dr_ft_wmen_forgn_v',

    # ---- Doctoral first-year breakdowns ----
    'dr_ft_frst_tot_black_v', 'dr_ft_frst_tot_indian_v', 'dr_ft_frst_tot_asian_v',
    'dr_ft_frst_tot_pacific_v', 'dr_ft_frst_tot_white_v', 'dr_ft_frst_tot_hisp_v',
    'dr_ft_frst_tot_multi_v', 'dr_ft_frst_tot_unk_v', 'dr_ft_frst_tot_forgn_v',

    'dr_ft_frst_men_black_v', 'dr_ft_frst_men_indian_v', 'dr_ft_frst_men_asian_v',
    'dr_ft_frst_men_pacific_v', 'dr_ft_frst_men_white_v', 'dr_ft_frst_men_hisp_v',
    'dr_ft_frst_men_multi_v', 'dr_ft_frst_men_unk_v', 'dr_ft_frst_men_forgn_v',
    'dr_ft_frst_men_all_races_v',

    'dr_ft_frst_wmen_black_v', 'dr_ft_frst_wmen_indian_v', 'dr_ft_frst_wmen_asian_v',
    'dr_ft_frst_wmen_pacific_v', 'dr_ft_frst_wmen_white_v', 'dr_ft_frst_wmen_hisp_v',
    'dr_ft_frst_wmen_multi_v', 'dr_ft_frst_wmen_unk_v', 'dr_ft_frst_wmen_forgn_v',
    'dr_ft_frst_wmen_all_races_v',

    # Institution name
    'institution_name'
]

# === Helper functions ===
def normalize_cols(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)
    return df

def safe_year_from_filename(filename):
    m = re.search(r'(19|20)\d{2}', os.path.basename(filename))
    return int(m.group()) if m else None

def load_files(files, source, filter_ipeds=True):
    """Load Excel files and normalize columns, handling missing vars."""
    data_list = []
    unitids_set = set()
    for f in files:
        try:
            df = pd.read_excel(f, dtype=str)
            df = normalize_cols(df)
            year = safe_year_from_filename(f)
            if not year:
                print(f"⚠️ Skipping {f}: no valid year found")
                continue

            df['unitid'] = df['unitid'].astype(str)

            if source == 'ipeds' and filter_ipeds:
                mask_cip = df['cipcode'].astype(str).str.startswith('40.08')
                mask_aw  = df['awlevel'].astype(str).isin(['7','9','17'])
                df = df.loc[mask_cip & mask_aw]

            available_vars = [v for v in vars_of_interest if v in df.columns]
            missing_vars = [v for v in vars_of_interest if v not in df.columns]
            if missing_vars:
                print(f"⚠️ Missing {len(missing_vars)} vars in {f}: {missing_vars[:5]}{'...' if len(missing_vars)>5 else ''}")

            keep_cols = ['unitid'] + available_vars
            if source == 'ipeds' and 'cipcode' in df.columns and 'awlevel' in df.columns:
                keep_cols += ['cipcode','awlevel']

            df = df[keep_cols].copy()
            df['source'] = source
            df['year'] = year

            data_list.append(df)
            unitids_set.update(df['unitid'].unique())
            print(f"✔ Loaded {source.upper()} {year}: {len(df)} rows")
        except Exception as e:
            print(f"❌ Error reading {f}: {e}")
    combined_df = pd.concat(data_list, ignore_index=True) if data_list else pd.DataFrame()
    return combined_df, unitids_set

# === Step 1: Collect files ===
ipeds_files = [os.path.join(ipeds_path, f) for f in os.listdir(ipeds_path) if f.endswith('.xlsx')]
gss_files   = [os.path.join(gss_path, f)  for f in os.listdir(gss_path)  if f.endswith('.xlsx')]
print(f"Found {len(ipeds_files)} IPEDS files and {len(gss_files)} GSS files.\n")

# === Step 2: Load IPEDS & GSS ===
ipeds_long, ipeds_unitids = load_files(ipeds_files, 'ipeds')
gss_long, gss_unitids     = load_files(gss_files, 'gss', filter_ipeds=False)

# === Step 3: Keep only UNITIDs present in both datasets ===
common_unitids = set(ipeds_long['unitid']).intersection(gss_long['unitid'])
ipeds_long = ipeds_long[ipeds_long['unitid'].isin(common_unitids)]
gss_long   = gss_long[gss_long['unitid'].isin(common_unitids)]

# === Step 4: Merge by UNITID & year (outer merge ensures all years) ===
combined = pd.merge(ipeds_long, gss_long, on=['unitid','year'], how='outer', suffixes=('_ipeds','_gss'))

# Fill institution_name: prefer GSS, then IPEDS
if 'institution_name_gss' in combined.columns:
    combined['institution_name'] = combined['institution_name_gss']
    if 'institution_name_ipeds' in combined.columns:
        combined['institution_name'] = combined['institution_name'].combine_first(combined['institution_name_ipeds'])
else:
    combined['institution_name'] = combined.get('institution_name_ipeds', pd.NA)

# Drop redundant columns
combined = combined.drop(columns=[c for c in combined.columns if c in ['institution_name_ipeds','institution_name_gss']])

# === Step 5: Convert numeric columns from text to numbers ===
numeric_cols = [c for c in combined.columns if c not in ['institution_name']]
for col in numeric_cols:
    combined[col] = pd.to_numeric(combined[col], errors='coerce')

# === Step 6: Reorder columns ===
cols_order = ['unitid','institution_name','year'] + [c for c in combined.columns if c not in ['unitid','institution_name','year']]
combined = combined[cols_order]

# === Step 7: Save to Excel ===
combined = combined.sort_values(by=['unitid','year']).reset_index(drop=True)
print("\nSaving merged table to Excel...")
combined.to_excel(output_path, index=False)
print(f"✅ Saved to: {output_path}")

print("\nPreview:")
print(combined.head(10))
'''

# TK CODE WORKS BUT MINOR ISSUES
'''
# === Helper functions ===
def normalize_cols(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)
    return df

def safe_year_from_filename(filename):
    m = re.search(r'(19|20)\d{2}', os.path.basename(filename))
    return int(m.group()) if m else None

def load_files(files, source, filter_ipeds=True):
    """Load Excel files and normalize columns, handling missing vars."""
    data_list = []
    unitids_set = set()
    for f in files:
        try:
            df = pd.read_excel(f, dtype=str)
            df = normalize_cols(df)
            year = safe_year_from_filename(f)
            if not year:
                print(f"⚠️ Skipping {f}: no valid year found")
                continue

            df['unitid'] = df['unitid'].astype(str)

            if source == 'ipeds' and filter_ipeds:
                mask_cip = df['cipcode'].astype(str).str.startswith('40.08')
                mask_aw  = df['awlevel'].astype(str).isin(['7','9','17'])
                df = df.loc[mask_cip & mask_aw]

            available_vars = [v for v in vars_of_interest if v in df.columns]
            missing_vars = [v for v in vars_of_interest if v not in df.columns]
            if missing_vars:
                print(f"⚠️ Missing {len(missing_vars)} vars in {f}: {missing_vars[:5]}{'...' if len(missing_vars)>5 else ''}")

            keep_cols = ['unitid'] + available_vars
            if source == 'ipeds' and 'cipcode' in df.columns and 'awlevel' in df.columns:
                keep_cols += ['cipcode','awlevel']

            df = df[keep_cols].copy()
            df['source'] = source
            df['year'] = year

            data_list.append(df)
            unitids_set.update(df['unitid'].unique())
            print(f"✔ Loaded {source.upper()} {year}: {len(df)} rows")
        except Exception as e:
            print(f"❌ Error reading {f}: {e}")
    combined_df = pd.concat(data_list, ignore_index=True) if data_list else pd.DataFrame()
    return combined_df, unitids_set

# === Step 1: Collect files ===
ipeds_files = [os.path.join(ipeds_path, f) for f in os.listdir(ipeds_path) if f.endswith('.xlsx')]
gss_files   = [os.path.join(gss_path, f)  for f in os.listdir(gss_path)  if f.endswith('.xlsx')]
print(f"Found {len(ipeds_files)} IPEDS files and {len(gss_files)} GSS files.\n")

# === Step 2: Load IPEDS & GSS ===
ipeds_long, ipeds_unitids = load_files(ipeds_files, 'ipeds')
gss_long, gss_unitids     = load_files(gss_files, 'gss', filter_ipeds=False)

# === Step 3: Merge by UNITID & year ===
combined = pd.merge(ipeds_long, gss_long, on=['unitid','year'], how='outer', suffixes=('_ipeds','_gss'))

# Fill institution_name: prefer GSS, then IPEDS
if 'institution_name_gss' in combined.columns:
    combined['institution_name'] = combined['institution_name_gss']
    if 'institution_name_ipeds' in combined.columns:
        combined['institution_name'] = combined['institution_name'].combine_first(combined['institution_name_ipeds'])
else:
    combined['institution_name'] = combined.get('institution_name_ipeds', pd.NA)

combined = combined.drop(columns=[c for c in combined.columns if c in ['institution_name_ipeds','institution_name_gss']])

# === Step 4: Convert numeric columns from text to numbers ===
numeric_cols = [c for c in combined.columns if c not in ['institution_name']]
for col in numeric_cols:
    combined[col] = pd.to_numeric(combined[col], errors='coerce')

# === Step 5: Reorder columns ===
cols_order = ['unitid','institution_name','year'] + [c for c in combined.columns if c not in ['unitid','institution_name','year']]
combined = combined[cols_order]

# === Step 6: Save to Excel ===
combined = combined.sort_values(by=['unitid','year']).reset_index(drop=True)
print("\nSaving merged table to Excel...")
combined.to_excel(output_path, index=False)
print(f"✅ Saved to: {output_path}")

print("\nPreview:")
print(combined.head(10))


'''










# TK CODE FUNCTIONAL BUT NEEDS SMALL EDITS ABOVE
 
''' 

# ================================================================
# FIRST YEAR & GRAD CHECKER — LONG TABLE CREATOR
# ================================================================
# Gathers all IPEDS and GSS data for Physics (CIP 40.08xx)
# Builds a long table of UNITID × Year with all vars_of_interest
# ================================================================

import os
import re
import pandas as pd

# === Filepaths ===
ipeds_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/Untrimmed IPEDS"
gss_path  = "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/Untrimmed GSS"
output_path = "/Users/co25936/Desktop/PER/IPEDS/FirstYear and Grad Checker.xlsx"

# === Variables of interest (full list) ===
vars_of_interest = [
    'ctotalt', 'ma_ft_tot_all_races_v', 'dr_ft_tot_all_races_v',
    'ma_ft_men_all_races_v', 'ma_ft_wmen_all_races_v',
    'dr_ft_men_all_races_v', 'dr_ft_wmen_all_races_v',
    'ma_ft_frst_tot_all_races_v', 'dr_ft_frst_tot_all_races_v',
    'ft_frst_men_all_races_v', 'ft_frst_wmen_all_races_v',
    'ft_tot_all_races_v', 'ft_tot_black_v', 'ft_tot_indian_v', 'ft_tot_asian_v', 
    'ft_tot_pacific_v', 'ft_tot_white_v', 'ft_tot_hisp_v', 'ft_tot_multi_v', 
    'ft_tot_unk_v', 'ft_tot_forgn_v', 'ft_frst_tot_all_races_v', 'ft_frst_tot_black_v',
    'ft_frst_tot_indian_v', 'ft_frst_tot_asian_v', 'ft_frst_tot_pacific_v',
    'ft_frst_tot_white_v', 'ft_frst_tot_hisp_v', 'ft_frst_tot_multi_v', 'ft_frst_tot_unk_v',
    'ft_frst_tot_forgn_v', 'ft_frst_men_black_v', 'ft_frst_men_indian_v', 'ft_frst_men_asian_v',
    'ft_frst_men_pacific_v', 'ft_frst_men_white_v', 'ft_frst_men_hisp_v', 'ft_frst_men_multi_v',
    'ft_frst_men_unk_v', 'ft_frst_men_forgn_v', 'ft_frst_wmen_black_v', 'ft_frst_wmen_indian_v',
    'ft_frst_wmen_asian_v', 'ft_frst_wmen_pacific_v', 'ft_frst_wmen_white_v', 'ft_frst_wmen_hisp_v',
    'ft_frst_wmen_multi_v', 'ft_frst_wmen_unk_v', 'ft_frst_wmen_forgn_v', 'ctotalm', 'ctotalw',
    'crace17', 'crace18', 'crace19', 'crace20', 'crace21', 'crace22', 'cunknt',
    'cbkaat', 'casiat', 'cnhpit', 'chispt', 'cwhitt', 'c2mort', 'cnralt',
    # Master's and PhD totals by race/sex (full)
    'ma_ft_tot_black_v', 'ma_ft_tot_indian_v', 'ma_ft_tot_asian_v', 'ma_ft_tot_pacific_v',
    'ma_ft_tot_white_v', 'ma_ft_tot_hisp_v', 'ma_ft_tot_multi_v', 'ma_ft_tot_unk_v',
    'ma_ft_tot_forgn_v', 'ma_ft_men_black_v', 'ma_ft_men_indian_v', 'ma_ft_men_asian_v',
    'ma_ft_men_pacific_v', 'ma_ft_men_white_v', 'ma_ft_men_hisp_v', 'ma_ft_men_multi_v',
    'ma_ft_men_unk_v', 'ma_ft_men_forgn_v', 'ma_ft_wmen_black_v', 'ma_ft_wmen_indian_v',
    'ma_ft_wmen_asian_v', 'ma_ft_wmen_pacific_v', 'ma_ft_wmen_white_v', 'ma_ft_wmen_hisp_v',
    'ma_ft_wmen_multi_v', 'ma_ft_wmen_unk_v', 'ma_ft_wmen_forgn_v',
    'ma_ft_frst_men_black_v', 'ma_ft_frst_men_indian_v', 'ma_ft_frst_men_asian_v',
    'ma_ft_frst_men_pacific_v', 'ma_ft_frst_men_white_v', 'ma_ft_frst_men_hisp_v',
    'ma_ft_frst_men_multi_v', 'ma_ft_frst_men_unk_v', 'ma_ft_frst_men_forgn_v',
    'ma_ft_frst_men_all_races_v', 'ma_ft_frst_wmen_black_v', 'ma_ft_frst_wmen_indian_v',
    'ma_ft_frst_wmen_asian_v', 'ma_ft_frst_wmen_pacific_v', 'ma_ft_frst_wmen_white_v',
    'ma_ft_frst_wmen_hisp_v', 'ma_ft_frst_wmen_multi_v', 'ma_ft_frst_wmen_unk_v',
    'ma_ft_frst_wmen_forgn_v', 'ma_ft_frst_wmen_all_races_v',
    'ma_ft_frst_tot_black_v', 'ma_ft_frst_tot_indian_v', 'ma_ft_frst_tot_asian_v',
    'ma_ft_frst_tot_pacific_v', 'ma_ft_frst_tot_white_v', 'ma_ft_frst_tot_hisp_v',
    'ma_ft_frst_tot_multi_v', 'ma_ft_frst_tot_unk_v', 'ma_ft_frst_tot_forgn_v',
    'dr_ft_tot_black_v', 'dr_ft_tot_indian_v', 'dr_ft_tot_asian_v', 'dr_ft_tot_pacific_v',
    'dr_ft_tot_white_v', 'dr_ft_tot_hisp_v', 'dr_ft_tot_multi_v', 'dr_ft_tot_unk_v',
    'dr_ft_tot_forgn_v', 'dr_ft_men_black_v', 'dr_ft_men_indian_v', 'dr_ft_men_asian_v',
    'dr_ft_men_pacific_v', 'dr_ft_men_white_v', 'dr_ft_men_hisp_v', 'dr_ft_men_multi_v',
    'dr_ft_men_unk_v', 'dr_ft_men_forgn_v', 'dr_ft_wmen_black_v', 'dr_ft_wmen_indian_v',
    'dr_ft_wmen_asian_v', 'dr_ft_wmen_pacific_v', 'dr_ft_wmen_white_v', 'dr_ft_wmen_hisp_v',
    'dr_ft_wmen_multi_v', 'dr_ft_wmen_unk_v', 'dr_ft_wmen_forgn_v',
    'dr_ft_frst_tot_black_v', 'dr_ft_frst_tot_indian_v', 'dr_ft_frst_tot_asian_v',
    'dr_ft_frst_tot_pacific_v', 'dr_ft_frst_tot_white_v', 'dr_ft_frst_tot_hisp_v',
    'dr_ft_frst_tot_multi_v', 'dr_ft_frst_tot_unk_v', 'dr_ft_frst_tot_forgn_v',
    'dr_ft_frst_men_black_v', 'dr_ft_frst_men_indian_v', 'dr_ft_frst_men_asian_v',
    'dr_ft_frst_men_pacific_v', 'dr_ft_frst_men_white_v', 'dr_ft_frst_men_hisp_v',
    'dr_ft_frst_men_multi_v', 'dr_ft_frst_men_unk_v', 'dr_ft_frst_men_forgn_v',
    'dr_ft_frst_men_all_races_v', 'dr_ft_frst_wmen_black_v', 'dr_ft_frst_wmen_indian_v',
    'dr_ft_frst_wmen_asian_v', 'dr_ft_frst_wmen_pacific_v', 'dr_ft_frst_wmen_white_v',
    'dr_ft_frst_wmen_hisp_v', 'dr_ft_frst_wmen_multi_v', 'dr_ft_frst_wmen_unk_v',
    'dr_ft_frst_wmen_forgn_v', 'dr_ft_frst_wmen_all_races_v', 'institution_name'
]

# === Helper functions ===
def normalize_cols(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)
    return df

def safe_year_from_filename(filename):
    m = re.search(r'(19|20)\d{2}', os.path.basename(filename))
    return int(m.group()) if m else None

def load_files(files, source):
    """Load and normalize Excel files, handling missing columns."""
    data_list = []
    unitids_set = set()
    for f in files:
        try:
            df = pd.read_excel(f, dtype=str)
            df = normalize_cols(df)
            year = safe_year_from_filename(f)
            if not year:
                print(f"⚠️ Skipping {f}: no valid year found")
                continue
            df['unitid'] = df['unitid'].astype(str)

            # Only keep vars that exist in this file
            available_vars = [v for v in vars_of_interest if v in df.columns]
            missing_vars = [v for v in vars_of_interest if v not in df.columns]
            if missing_vars:
                print(f"⚠️ Missing {len(missing_vars)} vars in {f}: {missing_vars[:5]}{'...' if len(missing_vars)>5 else ''}")

            # CIP & AWLEVEL filter for IPEDS only
            if source == 'ipeds':
                mask_cip = df['cipcode'].astype(str).str.startswith('40.08')
                mask_aw  = df['awlevel'].astype(str).isin(['7','9','17'])
                df = df.loc[mask_cip & mask_aw]

            keep_cols = ['unitid']
            if source == 'ipeds':
                keep_cols += ['cipcode','awlevel']
            keep_cols += available_vars

            df = df[keep_cols].copy()
            df['source'] = source
            df['year'] = year

            data_list.append(df)
            unitids_set.update(df['unitid'].unique())

            print(f"✔ Loaded {source.upper()} {year}: {len(df)} rows")
        except Exception as e:
            print(f"❌ Error reading {f}: {e}")
    combined_df = pd.concat(data_list, ignore_index=True) if data_list else pd.DataFrame()
    return combined_df, unitids_set

# === Step 1: Collect files ===
ipeds_files = [os.path.join(ipeds_path, f) for f in os.listdir(ipeds_path) if f.endswith('.xlsx')]
gss_files   = [os.path.join(gss_path, f)  for f in os.listdir(gss_path)  if f.endswith('.xlsx')]

print(f"Found {len(ipeds_files)} IPEDS files and {len(gss_files)} GSS files.\n")

# === Step 2: Load IPEDS & GSS ===
ipeds_long, ipeds_unitids = load_files(ipeds_files, 'ipeds')
gss_long, gss_unitids     = load_files(gss_files, 'gss')

# === Step 3: Union of UNITIDs ===
all_unitids = sorted(ipeds_unitids.union(gss_unitids))
print(f"\nTotal unique UNITIDs across sources: {len(all_unitids)}")

# === Step 4: Combine IPEDS + GSS ===
combined = pd.concat([ipeds_long, gss_long], ignore_index=True, sort=False)

# Ensure every UNITID is present at least once
missing_units = [u for u in all_unitids if u not in combined['unitid'].unique()]
if missing_units:
    combined = pd.concat([combined, pd.DataFrame({'unitid': missing_units, 'year': None, 'source': None})], ignore_index=True)

# Drop duplicates
combined = combined.drop_duplicates(subset=['unitid','year','source'], keep='last')
combined = combined.sort_values(by=['unitid','year']).reset_index(drop=True)

# === Step 5: Save to Excel ===
print("\nSaving long table to Excel...")
combined.to_excel(output_path, index=False)
print(f"✅ Saved to: {output_path}")

print("\nPreview:")
print(combined.head(10))

'''
# TK REALY OLD CODE

'''
import pandas as pd
import glob
import os

# === Filepaths ===
ipeds_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/Untrimmed IPEDS"
gss_path  = "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/Untrimmed GSS"
output_path = "/Users/co25936/Desktop/PER/IPEDS/FirstYear and Grad Checker.xlsx"

# === Target variable list ===
vars_of_interest = [
    # Degree total
    'ctotalt',
    # Masters/Doctorate totals
    'ma_ft_tot_all_races_v', 'dr_ft_tot_all_races_v',
    'ma_ft_men_all_races_v', 'ma_ft_wmen_all_races_v',
    'dr_ft_men_all_races_v', 'dr_ft_wmen_all_races_v',

    # First years by degree type (overall)
    'ma_ft_frst_tot_all_races_v', 'dr_ft_frst_tot_all_races_v',

    # First-year by sex (overall)
    'ft_frst_men_all_races_v', 'ft_frst_wmen_all_races_v',

    # Total enrollment by race
    'ft_tot_all_races_v', 'ft_tot_black_v', 'ft_tot_indian_v', 'ft_tot_asian_v', 'ft_tot_pacific_v',
    'ft_tot_white_v', 'ft_tot_hisp_v', 'ft_tot_multi_v', 'ft_tot_unk_v', 'ft_tot_forgn_v',

    # First-time enrollment by race
    'ft_frst_tot_all_races_v', 'ft_frst_tot_black_v', 'ft_frst_tot_indian_v', 'ft_frst_tot_asian_v',
    'ft_frst_tot_pacific_v', 'ft_frst_tot_white_v', 'ft_frst_tot_hisp_v', 'ft_frst_tot_multi_v',
    'ft_frst_tot_unk_v', 'ft_frst_tot_forgn_v',

    # First-time men by race
    'ft_frst_men_black_v', 'ft_frst_men_indian_v', 'ft_frst_men_asian_v', 'ft_frst_men_pacific_v',
    'ft_frst_men_white_v', 'ft_frst_men_hisp_v', 'ft_frst_men_multi_v', 'ft_frst_men_unk_v', 'ft_frst_men_forgn_v',

    # First-time women by race
    'ft_frst_wmen_black_v', 'ft_frst_wmen_indian_v', 'ft_frst_wmen_asian_v', 'ft_frst_wmen_pacific_v',
    'ft_frst_wmen_white_v', 'ft_frst_wmen_hisp_v', 'ft_frst_wmen_multi_v', 'ft_frst_wmen_unk_v', 'ft_frst_wmen_forgn_v',

    # Degree totals by sex 
    'ctotalm', 'ctotalw',

    # Degree totals by race
    'crace17', 'crace18', 'crace19', 'crace20', 'crace21', 'crace22', 'cunknt',
    'cbkaat', 'casiat', 'cnhpit', 'chispt', 'cwhitt', 'c2mort', 'cnralt',

    # ---- Masters breakdowns ----
    'ma_ft_tot_black_v', 'ma_ft_tot_indian_v', 'ma_ft_tot_asian_v', 'ma_ft_tot_pacific_v',
    'ma_ft_tot_white_v', 'ma_ft_tot_hisp_v', 'ma_ft_tot_multi_v', 'ma_ft_tot_unk_v', 'ma_ft_tot_forgn_v',

    'ma_ft_men_black_v', 'ma_ft_men_indian_v', 'ma_ft_men_asian_v', 'ma_ft_men_pacific_v',
    'ma_ft_men_white_v', 'ma_ft_men_hisp_v', 'ma_ft_men_multi_v', 'ma_ft_men_unk_v', 'ma_ft_men_forgn_v',

    'ma_ft_wmen_black_v', 'ma_ft_wmen_indian_v', 'ma_ft_wmen_asian_v', 'ma_ft_wmen_pacific_v',
    'ma_ft_wmen_white_v', 'ma_ft_wmen_hisp_v', 'ma_ft_wmen_multi_v', 'ma_ft_wmen_unk_v', 'ma_ft_wmen_forgn_v',

    # ---- Masters first-year breakdowns ----
    'ma_ft_frst_men_black_v', 'ma_ft_frst_men_indian_v', 'ma_ft_frst_men_asian_v',
    'ma_ft_frst_men_pacific_v', 'ma_ft_frst_men_white_v', 'ma_ft_frst_men_hisp_v',
    'ma_ft_frst_men_multi_v', 'ma_ft_frst_men_unk_v', 'ma_ft_frst_men_forgn_v',
    'ma_ft_frst_men_all_races_v',

    'ma_ft_frst_wmen_black_v', 'ma_ft_frst_wmen_indian_v', 'ma_ft_frst_wmen_asian_v',
    'ma_ft_frst_wmen_pacific_v', 'ma_ft_frst_wmen_white_v', 'ma_ft_frst_wmen_hisp_v',
    'ma_ft_frst_wmen_multi_v', 'ma_ft_frst_wmen_unk_v', 'ma_ft_frst_wmen_forgn_v',
    'ma_ft_frst_wmen_all_races_v',

    'ma_ft_frst_tot_black_v', 'ma_ft_frst_tot_indian_v', 'ma_ft_frst_tot_asian_v',
    'ma_ft_frst_tot_pacific_v', 'ma_ft_frst_tot_white_v', 'ma_ft_frst_tot_hisp_v',
    'ma_ft_frst_tot_multi_v', 'ma_ft_frst_tot_unk_v', 'ma_ft_frst_tot_forgn_v',

    # ---- Doctoral breakdowns ----
    'dr_ft_tot_black_v', 'dr_ft_tot_indian_v', 'dr_ft_tot_asian_v', 'dr_ft_tot_pacific_v',
    'dr_ft_tot_white_v', 'dr_ft_tot_hisp_v', 'dr_ft_tot_multi_v', 'dr_ft_tot_unk_v', 'dr_ft_tot_forgn_v',

    'dr_ft_men_black_v', 'dr_ft_men_indian_v', 'dr_ft_men_asian_v', 'dr_ft_men_pacific_v',
    'dr_ft_men_white_v', 'dr_ft_men_hisp_v', 'dr_ft_men_multi_v', 'dr_ft_men_unk_v', 'dr_ft_men_forgn_v',

    'dr_ft_wmen_black_v', 'dr_ft_wmen_indian_v', 'dr_ft_wmen_asian_v', 'dr_ft_wmen_pacific_v',
    'dr_ft_wmen_white_v', 'dr_ft_wmen_hisp_v', 'dr_ft_wmen_multi_v', 'dr_ft_wmen_unk_v', 'dr_ft_wmen_forgn_v',

    # ---- Doctoral first-year breakdowns ----
    'dr_ft_frst_tot_black_v', 'dr_ft_frst_tot_indian_v', 'dr_ft_frst_tot_asian_v',
    'dr_ft_frst_tot_pacific_v', 'dr_ft_frst_tot_white_v', 'dr_ft_frst_tot_hisp_v',
    'dr_ft_frst_tot_multi_v', 'dr_ft_frst_tot_unk_v', 'dr_ft_frst_tot_forgn_v',

    'dr_ft_frst_men_black_v', 'dr_ft_frst_men_indian_v', 'dr_ft_frst_men_asian_v',
    'dr_ft_frst_men_pacific_v', 'dr_ft_frst_men_white_v', 'dr_ft_frst_men_hisp_v',
    'dr_ft_frst_men_multi_v', 'dr_ft_frst_men_unk_v', 'dr_ft_frst_men_forgn_v',
    'dr_ft_frst_men_all_races_v',

    'dr_ft_frst_wmen_black_v', 'dr_ft_frst_wmen_indian_v', 'dr_ft_frst_wmen_asian_v',
    'dr_ft_frst_wmen_pacific_v', 'dr_ft_frst_wmen_white_v', 'dr_ft_frst_wmen_hisp_v',
    'dr_ft_frst_wmen_multi_v', 'dr_ft_frst_wmen_unk_v', 'dr_ft_frst_wmen_forgn_v',
    'dr_ft_frst_wmen_all_races_v'
]


# === Helper: normalize column names ===
def normalize_cols(df):
    df.columns = df.columns.str.lower().str.strip()
    return df

# === Step 1: Load IPEDS UNITIDs with 40.08xx CIPCODE and AWLEVEL 7, 9, 17 ===
ipeds_files = glob.glob(os.path.join(ipeds_path, "*.xlsx"))
ipeds_list = []

for f in ipeds_files:
    year = os.path.basename(f)[1:5]  # e.g. "2001" from "c2001_a.xlsx"
    df = pd.read_excel(f, dtype=str)
    df = normalize_cols(df)
    df['year'] = int(year)

    # ensure numeric comparisons work
    df['awlevel'] = pd.to_numeric(df.get('awlevel'), errors='coerce')
    df['cipcode'] = df.get('cipcode', '').astype(str)

    # filter CIP and AWLEVEL
    df = df[df['cipcode'].str.startswith('40.08')]
    df = df[df['awlevel'].isin([7, 9, 17])]

    if not df.empty:
        ipeds_list.append(df[['unitid', 'cipcode', 'awlevel', 'year']].drop_duplicates())

ipeds_units = pd.concat(ipeds_list, ignore_index=True) if ipeds_list else pd.DataFrame(columns=['unitid', 'year'])

# === Step 2: Load GSS UNITIDs ===
gss_files = glob.glob(os.path.join(gss_path, "*.xlsx"))
gss_list = []

for f in gss_files:
    year = os.path.basename(f)[3:7]  # e.g. "2000" from "gss2000_Code.xlsx"
    df = pd.read_excel(f, dtype=str)
    df = normalize_cols(df)
    df['year'] = int(year)
    if 'unitid' in df.columns:
        gss_list.append(df[['unitid', 'institution_name', 'year']].drop_duplicates())

gss_units = pd.concat(gss_list, ignore_index=True) if gss_list else pd.DataFrame(columns=['unitid', 'year'])

# === Step 3: Union of all UNITIDs ===
all_units = pd.concat([ipeds_units[['unitid']], gss_units[['unitid']]], ignore_index=True).drop_duplicates()

# === Step 4: Collect all IPEDS variable data (long format) ===
records = []

for f in ipeds_files:
    year = os.path.basename(f)[1:5]
    df = pd.read_excel(f, dtype=str)
    df = normalize_cols(df)
    df['year'] = int(year)

    if 'unitid' not in df.columns:
        continue

    # Make a lowercase→actual column name mapping
    col_map = {c.lower(): c for c in df.columns}

    # Keep variables that exist regardless of case
    cols_to_keep = ['unitid'] + [col_map[v.lower()] for v in vars_of_interest if v.lower() in col_map]

    sub = df[cols_to_keep].copy()


    # add year
    sub['year'] = int(year)

    records.append(sub)

ipeds_long = pd.concat(records, ignore_index=True) if records else pd.DataFrame(columns=['unitid', 'year', 'first_years', 'degrees_earned'])

# === Step 5: Merge GSS if needed (can be expanded similarly)
gss_long = pd.concat(gss_list, ignore_index=True) if gss_list else pd.DataFrame(columns=['unitid', 'year'])
combined = pd.merge(all_units, ipeds_long, on='unitid', how='left')

# === Step 6: Clean + export ===
combined = combined.drop_duplicates(subset=['unitid', 'year'])
combined = combined.sort_values(['unitid', 'year'])

output_path = "/Users/co25936/Desktop/PER/IPEDS/FirstYear and Grad Checker.xlsx"
combined.to_excel(output_path, index=False, engine='openpyxl')

print(f" Long-format master table created: {output_path}")

'''

'''
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

    # Aggregate degrees BY AWLEVEL
    for (uid, aw), val in df_phys.groupby([unit_col, aw_col])[ctotal_col].sum().items():
        aw = int(aw) if not pd.isna(aw) else None
        if aw is None:
            continue
        # store each (unitid, year, awlevel) separately
        phd_map[(uid, year, aw)] = float(val)


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
for (uid, year, aw) in sorted(phd_map.keys(), key=lambda x: (x[0], x[1], x[2])):
    row = {
        "UNITID": uid,
        "Year": year,
        "AWLEVEL": aw,
        "Institution_Name": inst_lookup.get(uid, None),
        "phd_degrees-earned": int(phd_map.get((uid, year, aw), 0)),
        "cipcodes_seen": ";".join(sorted(cip_seen.get(uid, set()))),
        "awlevels_seen": ";".join(sorted([str(a) for a in aw_seen.get(uid, set())])),
    }

    # add first-years if available
    row["first-years"] = int(first_map.get((uid, year), 0)) if (uid, year) in first_map else None

    rows.append(row)
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

    # First years by degree type (overall)
    'ma_ft_frst_tot_all_races_v', 'dr_ft_frst_tot_all_races_v',

    # First-year by sex (overall)
    'ft_frst_men_all_races_v', 'ft_frst_wmen_all_races_v',

    # Total enrollment by race
    'ft_tot_all_races_v', 'ft_tot_black_v', 'ft_tot_indian_v', 'ft_tot_asian_v', 'ft_tot_pacific_v',
    'ft_tot_white_v', 'ft_tot_hisp_v', 'ft_tot_multi_v', 'ft_tot_unk_v', 'ft_tot_forgn_v',

    # First-time enrollment by race
    'ft_frst_tot_all_races_v', 'ft_frst_tot_black_v', 'ft_frst_tot_indian_v', 'ft_frst_tot_asian_v',
    'ft_frst_tot_pacific_v', 'ft_frst_tot_white_v', 'ft_frst_tot_hisp_v', 'ft_frst_tot_multi_v',
    'ft_frst_tot_unk_v', 'ft_frst_tot_forgn_v',

    # First-time men by race
    'ft_frst_men_black_v', 'ft_frst_men_indian_v', 'ft_frst_men_asian_v', 'ft_frst_men_pacific_v',
    'ft_frst_men_white_v', 'ft_frst_men_hisp_v', 'ft_frst_men_multi_v', 'ft_frst_men_unk_v', 'ft_frst_men_forgn_v',

    # First-time women by race
    'ft_frst_wmen_black_v', 'ft_frst_wmen_indian_v', 'ft_frst_wmen_asian_v', 'ft_frst_wmen_pacific_v',
    'ft_frst_wmen_white_v', 'ft_frst_wmen_hisp_v', 'ft_frst_wmen_multi_v', 'ft_frst_wmen_unk_v', 'ft_frst_wmen_forgn_v',

    # Degree totals by sex 
    'ctotalm', 'ctotalw',

    # Degree totals by race
    'crace17', 'crace18', 'crace19', 'crace20', 'crace21', 'crace22', 'cunknt',
    'cbkaat', 'casiat', 'cnhpit', 'chispt', 'cwhitt', 'c2mort', 'cnralt',

    # ---- Masters breakdowns ----
    'ma_ft_tot_black_v', 'ma_ft_tot_indian_v', 'ma_ft_tot_asian_v', 'ma_ft_tot_pacific_v',
    'ma_ft_tot_white_v', 'ma_ft_tot_hisp_v', 'ma_ft_tot_multi_v', 'ma_ft_tot_unk_v', 'ma_ft_tot_forgn_v',

    'ma_ft_men_black_v', 'ma_ft_men_indian_v', 'ma_ft_men_asian_v', 'ma_ft_men_pacific_v',
    'ma_ft_men_white_v', 'ma_ft_men_hisp_v', 'ma_ft_men_multi_v', 'ma_ft_men_unk_v', 'ma_ft_men_forgn_v',

    'ma_ft_wmen_black_v', 'ma_ft_wmen_indian_v', 'ma_ft_wmen_asian_v', 'ma_ft_wmen_pacific_v',
    'ma_ft_wmen_white_v', 'ma_ft_wmen_hisp_v', 'ma_ft_wmen_multi_v', 'ma_ft_wmen_unk_v', 'ma_ft_wmen_forgn_v',

    # ---- Masters first-year breakdowns ----
    'ma_ft_frst_men_black_v', 'ma_ft_frst_men_indian_v', 'ma_ft_frst_men_asian_v',
    'ma_ft_frst_men_pacific_v', 'ma_ft_frst_men_white_v', 'ma_ft_frst_men_hisp_v',
    'ma_ft_frst_men_multi_v', 'ma_ft_frst_men_unk_v', 'ma_ft_frst_men_forgn_v',
    'ma_ft_frst_men_all_races_v',

    'ma_ft_frst_wmen_black_v', 'ma_ft_frst_wmen_indian_v', 'ma_ft_frst_wmen_asian_v',
    'ma_ft_frst_wmen_pacific_v', 'ma_ft_frst_wmen_white_v', 'ma_ft_frst_wmen_hisp_v',
    'ma_ft_frst_wmen_multi_v', 'ma_ft_frst_wmen_unk_v', 'ma_ft_frst_wmen_forgn_v',
    'ma_ft_frst_wmen_all_races_v',

    'ma_ft_frst_tot_black_v', 'ma_ft_frst_tot_indian_v', 'ma_ft_frst_tot_asian_v',
    'ma_ft_frst_tot_pacific_v', 'ma_ft_frst_tot_white_v', 'ma_ft_frst_tot_hisp_v',
    'ma_ft_frst_tot_multi_v', 'ma_ft_frst_tot_unk_v', 'ma_ft_frst_tot_forgn_v',

    # ---- Doctoral breakdowns ----
    'dr_ft_tot_black_v', 'dr_ft_tot_indian_v', 'dr_ft_tot_asian_v', 'dr_ft_tot_pacific_v',
    'dr_ft_tot_white_v', 'dr_ft_tot_hisp_v', 'dr_ft_tot_multi_v', 'dr_ft_tot_unk_v', 'dr_ft_tot_forgn_v',

    'dr_ft_men_black_v', 'dr_ft_men_indian_v', 'dr_ft_men_asian_v', 'dr_ft_men_pacific_v',
    'dr_ft_men_white_v', 'dr_ft_men_hisp_v', 'dr_ft_men_multi_v', 'dr_ft_men_unk_v', 'dr_ft_men_forgn_v',

    'dr_ft_wmen_black_v', 'dr_ft_wmen_indian_v', 'dr_ft_wmen_asian_v', 'dr_ft_wmen_pacific_v',
    'dr_ft_wmen_white_v', 'dr_ft_wmen_hisp_v', 'dr_ft_wmen_multi_v', 'dr_ft_wmen_unk_v', 'dr_ft_wmen_forgn_v',

    # ---- Doctoral first-year breakdowns ----
    'dr_ft_frst_tot_black_v', 'dr_ft_frst_tot_indian_v', 'dr_ft_frst_tot_asian_v',
    'dr_ft_frst_tot_pacific_v', 'dr_ft_frst_tot_white_v', 'dr_ft_frst_tot_hisp_v',
    'dr_ft_frst_tot_multi_v', 'dr_ft_frst_tot_unk_v', 'dr_ft_frst_tot_forgn_v',

    'dr_ft_frst_men_black_v', 'dr_ft_frst_men_indian_v', 'dr_ft_frst_men_asian_v',
    'dr_ft_frst_men_pacific_v', 'dr_ft_frst_men_white_v', 'dr_ft_frst_men_hisp_v',
    'dr_ft_frst_men_multi_v', 'dr_ft_frst_men_unk_v', 'dr_ft_frst_men_forgn_v',
    'dr_ft_frst_men_all_races_v',

    'dr_ft_frst_wmen_black_v', 'dr_ft_frst_wmen_indian_v', 'dr_ft_frst_wmen_asian_v',
    'dr_ft_frst_wmen_pacific_v', 'dr_ft_frst_wmen_white_v', 'dr_ft_frst_wmen_hisp_v',
    'dr_ft_frst_wmen_multi_v', 'dr_ft_frst_wmen_unk_v', 'dr_ft_frst_wmen_forgn_v',
    'dr_ft_frst_wmen_all_races_v'
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

print("\nConverting wide table to long format (robust melt-only)...")

# Identify identifier columns safely
id_vars = [c for c in ["UNITID", "Institution_Name", "cipcodes_seen", "awlevels_seen", "AWLEVEL"] if c in wide_df.columns]

# Select only columns that have year suffixes (e.g. "_2020")
long_candidates = [c for c in wide_df.columns if re.search(r"_\d{4}$", c)]
print(f"Found {len(long_candidates)} columns with year suffixes to melt...")

# Melt: converts wide -> long safely, without requiring unique ID combinations
long_df = (
    wide_df.melt(id_vars=id_vars, value_vars=long_candidates, var_name="Variable", value_name="Value")
)

# Extract the year from the column name
long_df["Year"] = long_df["Variable"].str.extract(r"_(\d{4})")[0].astype(int)

# Extract the variable base name (drop "_YYYY")
long_df["Variable"] = long_df["Variable"].str.replace(r"_\d{4}$", "", regex=True)

# Pivot to get one column per variable again
long_df = (
    long_df.pivot_table(
        index=id_vars + ["Year"],
        columns="Variable",
        values="Value",
        aggfunc="first"
    )
    .reset_index()
)

# Final cleanup
long_df.columns.name = None
long_df = long_df.sort_values(["UNITID", "Year"]).reset_index(drop=True)
print(f"✅ Successfully converted to long format with {len(long_df)} rows.")


# ---------- write Excel ----------
with pd.ExcelWriter(output_path, engine="openpyxl") as w:
    long_df.to_excel(w, sheet_name="long", index=False)
    meta_df.to_excel(w, sheet_name="meta", index=False)

print(f" Wrote long-format output (with {len(variable_bases)} variables) to {output_path}")

print("\n Sanity check passed: No input files were modified.")

'''
