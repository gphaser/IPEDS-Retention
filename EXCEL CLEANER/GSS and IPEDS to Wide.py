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
# STEP 4.5: Distribute values from blank AWLEVEL rows ( NOT WORKIN AHHHHH) 
# ==============================================================

# Separate blank and non-blank AWLEVEL rows
df_blank = df[df['awlevel'].isna()]
df_nonblank = df[df['awlevel'].notna()]

id_cols = ['unitid', 'year', 'awlevel']
value_cols = [col for col in df.columns if col not in id_cols]

# Loop through each unitid-year where a blank row exists
for (unitid, year), blank_group in df_blank.groupby(['unitid', 'year']):
    blank_row = blank_group.iloc[0]  # assume 1 blank row per unitid-year
    mask = (df_nonblank['unitid'] == unitid) & (df_nonblank['year'] == year)

    for col in value_cols:
        df_nonblank.loc[mask, col] = df_nonblank.loc[mask, col].combine_first(
            pd.Series(blank_row[col], index=df_nonblank.loc[mask].index)
        )

# Combine back into a single dataframe
df = df_nonblank.copy()

print("✅ Step 4.5 complete: values from blank AWLEVEL distributed")

# ==============================================================
# STEP 5: Convert to Wide Format
# ==============================================================

df_wide = df.set_index(['unitid', 'awlevel', 'year']).unstack('year')

# Flatten column names
df_wide.columns = [f"{col[0]}_{col[1]}" for col in df_wide.columns]

df_wide = df_wide.reset_index()

# ==============================================================
# STEP 6: Merge Back Single gss_code
# ==============================================================

df_wide = df_wide.merge(gss_lookup, on='unitid', how='left')


# ==============================================================
# STEP 7: Add in variable to count number of missing data points
# ==============================================================

#DataFrame
df_wide_blanks = df_wide

# Select columns that match your patterns
cols_to_check = [col for col in df_wide_blanks.columns if col.startswith(('CTOTALT', 'ft_tot_all_races', 'ft_frst_total_all_races'))]

# Create a new column counting missing values across those columns
df_wide_blanks['MISSING_COUNT'] = df_wide_blanks[cols_to_check].isnull().sum(axis=1)

# Filter rows based on missing_count (use this if we want to elimiate rows in the code)
filtered_df = df_wide_blanks[df_wide_blanks['MISSING_COUNT'] > 10]




# ==============================================================
# STEP 7.5: Keep Only Years >= 2010
# ==============================================================

df_wide_trim = df_wide[[col for col in df_wide.columns if not col.endswith(tuple(str(y) for y in range(1900, 2010)))]]

# ==============================================================
# STEP 8: Save Output
# ==============================================================

# Original wide file (all years that passed earlier filters)
df_wide_blanks.to_excel(output_path, index=False)

# Trimmed file (2010+ only)
output_trimmed_path = "/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_COMBINED_WIDE_trimmed.xlsx"

#file with the trimed years 
df_wide_trim.to_excel(output_trimmed_path, index=False)

print("✅ Wide format file saved to:", output_path)
print("✅ Trimmed (2010+) file saved to:", output_trimmed_path)



