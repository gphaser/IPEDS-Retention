# Reformat the GSS and IPEDS COMBINED FILE into Wide FORMAT
# goal takethe GSS and IPEDS combined file and go from Uniit ides each haveing a row for each year 
# have 1 row for each UNITID with all the data
# Need to manualy filter out the bad casses  using the missing vals

import pandas as pd
import numpy as np

# ==============================================================
# STEP 1: Load Data
# ==============================================================

input_path = '/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_Combined_file.xlsx'
output_path = "/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_COMBINED_WIDE.xlsx"

df = pd.read_excel(input_path)

# Clean column names
df.columns = df.columns.str.strip()

# ==============================================================
# STEP 2: Fix Duplicate Columns
# ==============================================================

for col in df.columns:
    if col.endswith('.1'):
        base_col = col[:-2]
        if base_col in df.columns:
            df[base_col] = df[base_col].combine_first(df[col])

# Drop the .1 columns
df = df.loc[:, ~df.columns.str.endswith('.1')]

# ==============================================================
# STEP 3: Ensure One Row per UNITID-Year
# ==============================================================

dupes = df[df.duplicated(subset=['unitid', 'year', 'awlevel'], keep=False)]

if not dupes.empty:
    print("⚠️ Found duplicates at UNITID-Year-AWLEVEL. Collapsing...")
    df = df.groupby(['unitid', 'year', 'awlevel'], as_index=False).first()

# ==============================================================
# STEP 4: Create Single gss_code per UNITID
# ==============================================================

# Optional: Check for inconsistencies
check = df.groupby('unitid')['gss_code'].nunique()
problem_ids = check[check > 1]

if len(problem_ids) > 0:
    print("⚠️ Warning: Some UNITIDs have multiple gss_code values")
    print(problem_ids.head())

# Use most frequent value (mode) per UNITID
gss_lookup = (
    df.groupby('unitid')['gss_code']
    .agg(lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan)
    .reset_index()
)

# Drop gss_code before reshaping
df = df.drop(columns=['gss_code'])

print( "WORKING!")
# ==============================================================
# STEP 4.5: Distribute values from blank AWLEVEL rows 
# check 119678 2010,2011, 2012 should go 4,4,4 curently goes 4, ,4
# ==============================================================
# ==============================================================
# (WORKING WOOO! ))
# ==============================================================


df.replace(r'^\s*$', np.nan, regex=True, inplace=True)

df_blank = df[df['awlevel'].isna()]
df_nonblank = df[df['awlevel'].notna()]

id_cols = ['unitid', 'year', 'awlevel']
value_cols = [col for col in df.columns if col not in id_cols]

# Step 1: Get valid AWLEVELs per UNITID
awlevel_map = (
    df_nonblank.groupby('unitid')['awlevel']
    .unique()
    .to_dict()
)

new_rows = []

# Step 2: Expand blank rows into correct AWLEVELs
for (unitid, year), group in df_blank.groupby(['unitid', 'year']):
    
    if unitid not in awlevel_map:
        continue  # skip if no known structure
    
    valid_awlevels = awlevel_map[unitid]
    base_row = group.iloc[0]

    for aw in valid_awlevels:
        new_row = base_row.copy()
        new_row['awlevel'] = aw
        new_rows.append(new_row)

# Convert new rows to DF
df_new = pd.DataFrame(new_rows)

# Step 3: Combine everything
df_combined = pd.concat([df_nonblank, df_new], ignore_index=True)

# Step 4: Fill within (unitid, year, awlevel)
df_combined = df_combined.sort_values(['unitid','year','awlevel'])

df_combined[value_cols] = df_combined.groupby(
    ['unitid','year','awlevel']
)[value_cols].transform(lambda x: x.ffill().bfill())

df = df_combined.copy()

print("Step 4.5 COMPLETE: AWLEVEL structure preserved correctly")
result = df.groupby('unitid')['awlevel'].nunique().value_counts()
print(result)

# ==============================================================
# STEP 5: Convert to Wide Format
# ==============================================================

df_wide = df.set_index(['unitid', 'awlevel', 'year']).unstack('year')

# Flatten column names
df_wide.columns = [
    f"{col[0]}_{int(col[1])}" if pd.notna(col[1]) else col[0]
    for col in df_wide.columns
]

df_wide = df_wide.reset_index()

# ==============================================================
# STEP 6: Merge Back Single gss_code
# ==============================================================

df_wide = df_wide.merge(gss_lookup, on='unitid', how='left')


# ==============================================================
# STEP 6.5: Keep Only Years >= 2010
# ==============================================================

# Trim years < 2010
df_wide_trim = df_wide[[
    col for col in df_wide.columns
    if not (
        col.split('_')[-1].isdigit() and
        int(col.split('_')[-1]) < 2010
    )
]]


# ==============================================================
# STEP 7: Add in variable to count number of missing data points
# ==============================================================

# DataFrame
df_wide_blanks = df_wide_trim.copy()

# Column groups
ctotalt_cols = [col for col in df_wide_blanks.columns if col.startswith('ctotalt_')]
ft_tot_cols = [col for col in df_wide_blanks.columns if col.startswith('ft_tot_all_races_')]
ft_frst_cols = [col for col in df_wide_blanks.columns if col.startswith('ft_frst_tot_all_races_')]

# Count missing values across years
df_wide_blanks['MISSING_CTOTALT'] = df_wide_blanks[ctotalt_cols].isnull().sum(axis=1)
df_wide_blanks['MISSING_ft_tot'] = df_wide_blanks[ft_tot_cols].isnull().sum(axis=1)
df_wide_blanks['MISSING_ft_frst'] = df_wide_blanks[ft_frst_cols].isnull().sum(axis=1)

# Total missing across all groups
cols_to_check = ctotalt_cols + ft_tot_cols + ft_frst_cols
df_wide_blanks['MISSING_COUNT'] = df_wide_blanks[cols_to_check].isnull().sum(axis=1)


# ==============================================================
# STEP 7.5: Filter bad rows with exceptions
# ==============================================================

exception_ids = [207971, 445188]

mask = (
    (
        (df_wide_blanks['MISSING_CTOTALT'] >= 5) |
        (df_wide_blanks['MISSING_ft_tot'] >= 5) |
        (df_wide_blanks['MISSING_ft_frst'] >= 5)
    )
    &
    (~df_wide_blanks['unitid'].isin(exception_ids))
)

# Keep only GOOD rows
filtered_df = df_wide_blanks[~mask].copy()

print("Rows removed:", mask.sum())
print("Rows remaining:", len(filtered_df))



# ==============================================================
# STEP 8: Save Output
# ==============================================================

# Original wide file (all years that passed earlier filters)
df_wide.to_excel(output_path, index=False)

# Trimmed file output path (2010+ only)
output_trimmed_path = "/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_COMBINED_WIDE_trimmed.xlsx"

#file with the trimed years 
# df_wide_blanks.to_excel(output_trimmed_path, index=False)
filtered_df.to_excel(output_trimmed_path, index=False)

print("✅ Wide format file saved to:", output_path)
print("✅ Trimmed (2010+) file saved to:", output_trimmed_path)



