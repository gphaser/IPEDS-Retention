# Reformat the GSS and IPEDS COMBINED FILE into LONG FORMAT
# goal takethe GSS and IPEDS combined file and go from Uniit ides each haveing a row for each year 
# have 1 row for each UNITID with all the data
# NEED TO ADRESS THE DUPLICATES IN THE DATA where some Columns are duplicated across AWLEVEL but others vary (ft and ft_first year duplicate and Total is unique

#Code to try and adress the duplicates and non uninque data that exists for some years

import pandas as pd
import numpy as np
import os

# ==============================================================
# STEP 1: Load Data
# ==============================================================

input_path = '/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_Combined_file.xlsx'
output_path = "/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_COMBINED_LONG.xlsx"

df = pd.read_excel(input_path)

# ==============================================================
# STEP 2: Define Column Groups
# ==============================================================

ft_cols = [
    col for col in df.columns
    if col.startswith('ft_tot')
    or col.startswith('ft_frst_tot')
    or col.startswith('dr_ft_tot')
    or col.startswith('dr_ft_frst_tot')
    or col.startswith('ma_ft_tot')
    or col.startswith('ma_ft_frst_tot')
]

id_cols = ['UNITID', 'Year', 'AWLEVEL']

other_cols = [col for col in df.columns if col not in id_cols + ft_cols]


# due to not all data being true duplicates 
check = df.groupby(['UNITID', 'Year'])[ft_cols].nunique()

safe_ft_cols = [col for col in ft_cols if (check[col] <= 1).all()]
unsafe_ft_cols = [col for col in ft_cols if (check[col] > 1).any()]

print("Safe to collapse:", safe_ft_cols)
print("Must keep AWLEVEL:", unsafe_ft_cols)

df_ft_safe = df.groupby(['UNITID', 'Year'], as_index=False)[safe_ft_cols].first()

other_cols = other_cols + unsafe_ft_cols

ft_cols = safe_ft_cols # put here to do the check

# CHECK .first is ok 
check = df.groupby(['UNITID', 'Year'])[ft_cols].nunique()

problems = check[(check > 1).any(axis=1)]
print(problems)

# ==============================================================
# STEP 3: Collapse FT columns (duplicate across AWLEVEL)
# ==============================================================

df_ft = df_ft_safe

# ==============================================================
# STEP 4: Clean AWLEVEL data (remove true duplicates if any)
# ==============================================================

df_aw = df[['UNITID', 'Year', 'AWLEVEL'] + other_cols]

# If duplicates exist, resolve them safely
df_aw = df_aw.groupby(['UNITID', 'Year', 'AWLEVEL'], as_index=False).first()

# ==============================================================
# STEP 5: Pivot AWLEVEL-dependent columns
# ==============================================================

df_aw_wide = df_aw.pivot(index='UNITID', columns=['Year', 'AWLEVEL'])

df_aw_wide.columns = [
    f"{col}_{year}_aw{aw}" for col, year, aw in df_aw_wide.columns
]

df_aw_wide = df_aw_wide.reset_index()

# ==============================================================
# STEP 6: Pivot FT columns (no AWLEVEL)
# ==============================================================

df_ft_wide = df_ft.pivot(index='UNITID', columns='Year')

df_ft_wide.columns = [
    f"{col}_{year}" for col, year in df_ft_wide.columns
]

df_ft_wide = df_ft_wide.reset_index()

# ==============================================================
# STEP 7: Merge Final Dataset
# ==============================================================

df_final = pd.merge(df_aw_wide, df_ft_wide, on='UNITID', how='left')

# ==============================================================
# STEP 8: Save
# ==============================================================

df_final.to_excel(output_path, index=False)

print("✅ Finished: Data reshaped and saved.")



'''
Code to adress duplicates
import pandas as pd
import numpy as np
import os

# ==============================================================
# STEP 1: Load Data
# ==============================================================

input_path = '/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_Combined_file.xlsx'
output_path = "/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_COMBINED_LONG.xlsx"

df = pd.read_excel(input_path)

# ==============================================================
# STEP 2: Define Column Groups
# ==============================================================

ft_cols = [
    col for col in df.columns
    if col.startswith('ft_tot')
    or col.startswith('ft_frst_tot')
    or col.startswith('dr_ft_frst_tot')
    or col.startswith('ma_ft_frst_tot')
]

id_cols = ['UNITID', 'Year', 'AWLEVEL']

other_cols = [col for col in df.columns if col not in id_cols + ft_cols]

# CHECK .first is ok 
check = df.groupby(['UNITID', 'Year'])[ft_cols].nunique()

problems = check[(check > 1).any(axis=1)]
print(problems)

# ==============================================================
# STEP 3: Collapse FT columns (duplicate across AWLEVEL)
# ==============================================================

df_ft = df.groupby(['UNITID', 'Year'], as_index=False)[ft_cols].first()

# ==============================================================
# STEP 4: Clean AWLEVEL data (remove true duplicates if any)
# ==============================================================

df_aw = df[['UNITID', 'Year', 'AWLEVEL'] + other_cols]

# If duplicates exist, resolve them safely
df_aw = df_aw.groupby(['UNITID', 'Year', 'AWLEVEL'], as_index=False).first()

# ==============================================================
# STEP 5: Pivot AWLEVEL-dependent columns
# ==============================================================

df_aw_wide = df_aw.pivot(index='UNITID', columns=['Year', 'AWLEVEL'])

df_aw_wide.columns = [
    f"{col}_{year}_aw{aw}" for col, year, aw in df_aw_wide.columns
]

df_aw_wide = df_aw_wide.reset_index()

# ==============================================================
# STEP 6: Pivot FT columns (no AWLEVEL)
# ==============================================================

df_ft_wide = df_ft.pivot(index='UNITID', columns='Year')

df_ft_wide.columns = [
    f"{col}_{year}" for col, year in df_ft_wide.columns
]

df_ft_wide = df_ft_wide.reset_index()

# ==============================================================
# STEP 7: Merge Final Dataset
# ==============================================================

df_final = pd.merge(df_aw_wide, df_ft_wide, on='UNITID', how='left')

# ==============================================================
# STEP 8: Save
# ==============================================================

df_final.to_excel(output_path, index=False)

print("✅ Finished: Data reshaped and saved.")

''' 


'''
Code to try and adress the duplicates and non uninque data that exists for some years

import pandas as pd
import numpy as np
import os

# ==============================================================
# STEP 1: Load Data
# ==============================================================

input_path = '/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_Combined_file.xlsx'
output_path = "/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_COMBINED_LONG.xlsx"

df = pd.read_excel(input_path)

# ==============================================================
# STEP 2: Define Column Groups
# ==============================================================

ft_cols = [
    col for col in df.columns
    if col.startswith('ft_tot')
    or col.startswith('ft_frst_tot')
    or col.startswith('dr_ft_tot')
    or col.startswith('dr_ft_frst_tot')
    or col.startswith('ma_ft_tot')
    or col.startswith('ma_ft_frst_tot')
]

id_cols = ['UNITID', 'Year', 'AWLEVEL']

other_cols = [col for col in df.columns if col not in id_cols + ft_cols]


# due to not all data being true duplicates 
check = df.groupby(['UNITID', 'Year'])[ft_cols].nunique()

safe_ft_cols = [col for col in ft_cols if (check[col] <= 1).all()]
unsafe_ft_cols = [col for col in ft_cols if (check[col] > 1).any()]

print("Safe to collapse:", safe_ft_cols)
print("Must keep AWLEVEL:", unsafe_ft_cols)

df_ft_safe = df.groupby(['UNITID', 'Year'], as_index=False)[safe_ft_cols].first()

other_cols = other_cols + unsafe_ft_cols

ft_cols = safe_ft_cols # put here to do the check

# CHECK .first is ok 
check = df.groupby(['UNITID', 'Year'])[ft_cols].nunique()

problems = check[(check > 1).any(axis=1)]
print(problems)

# ==============================================================
# STEP 3: Collapse FT columns (duplicate across AWLEVEL)
# ==============================================================

df_ft = df_ft_safe

# ==============================================================
# STEP 4: Clean AWLEVEL data (remove true duplicates if any)
# ==============================================================

df_aw = df[['UNITID', 'Year', 'AWLEVEL'] + other_cols]

# If duplicates exist, resolve them safely
df_aw = df_aw.groupby(['UNITID', 'Year', 'AWLEVEL'], as_index=False).first()

# ==============================================================
# STEP 5: Pivot AWLEVEL-dependent columns
# ==============================================================

df_aw_wide = df_aw.pivot(index='UNITID', columns=['Year', 'AWLEVEL'])

df_aw_wide.columns = [
    f"{col}_{year}_aw{aw}" for col, year, aw in df_aw_wide.columns
]

df_aw_wide = df_aw_wide.reset_index()

# ==============================================================
# STEP 6: Pivot FT columns (no AWLEVEL)
# ==============================================================

df_ft_wide = df_ft.pivot(index='UNITID', columns='Year')

df_ft_wide.columns = [
    f"{col}_{year}" for col, year in df_ft_wide.columns
]

df_ft_wide = df_ft_wide.reset_index()

# ==============================================================
# STEP 7: Merge Final Dataset
# ==============================================================

df_final = pd.merge(df_aw_wide, df_ft_wide, on='UNITID', how='left')

# ==============================================================
# STEP 8: Save
# ==============================================================

df_final.to_excel(output_path, index=False)

print("✅ Finished: Data reshaped and saved.")

'''