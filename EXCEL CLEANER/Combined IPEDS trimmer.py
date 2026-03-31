import pandas as pd
import numpy as np

# ==============================================================
# STEP 1: Load Data
# ==============================================================

input_file = '/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/IPEDS_combined_file.xlsx'
output_file = '/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/IPEDS_combined_file_cleaned.xlsx'

df = pd.read_excel(input_file)

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# ==============================================================
# STEP 2: Identify Key Columns
# ==============================================================

group_cols = ['unitid', 'cipcode', 'year', 'awlevel']

# ==============================================================
# STEP 3: Separate Numeric vs Non-Numeric Columns
# ==============================================================

numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

# Remove grouping columns from numeric list
numeric_cols = [col for col in numeric_cols if col not in group_cols]

non_numeric_cols = [col for col in df.columns if col not in numeric_cols + group_cols]

# ==============================================================
# STEP 4: Aggregate Data (SUM numeric, KEEP first for others)
# ==============================================================

df_clean = df.groupby(group_cols, as_index=False).agg(
    {**{col: 'sum' for col in numeric_cols},
     **{col: 'first' for col in non_numeric_cols}}
)

# ==============================================================
# STEP 5: (Optional) Drop MAJORNUM since it's no longer needed
# ==============================================================

if 'majornum' in df_clean.columns:
    df_clean = df_clean.drop(columns=['majornum'])

# ==============================================================
# STEP 6: Save Cleaned File
# ==============================================================

df_clean.to_excel(output_file, index=False)

print("✅ Cleaned IPEDS file saved to:", output_file)