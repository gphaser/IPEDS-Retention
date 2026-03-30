# LONG IPEDS COMBINED
import pandas as pd
import numpy as np
import os

# ==============================================================
# STEP 1: Load Long IPEDS Data
# ==============================================================

input_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/IPEDS_combined_file.xlsx"
df = pd.read_excel(input_path)

# Standardize column names (optional)
df.columns = df.columns.str.strip()

id_cols = ["unitid", "year", "awlevel"]

# ==============================================================
# STEP 2: Identify Numeric Columns
# ==============================================================

numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
numeric_cols = [col for col in numeric_cols if col not in id_cols]

# ==============================================================
# STEP 3: Check for duplicates
# ==============================================================

dup_check = df.duplicated(subset=id_cols, keep=False)
print(f"⚠️ Total duplicate rows (UNITID+Year+AWLEVEL): {dup_check.sum()}")

if dup_check.any():
    # Extract all duplicates
    duplicates_df = df[dup_check].sort_values(id_cols)
    
    # Optional: print first 10 to console
    print("First 10 duplicate rows:")
    print(duplicates_df.head(10))
    
    # Save all duplicates to Excel
    duplicates_path = "/Users/co25936/Desktop/PER/IPEDS/IPEDS_Duplicates_list.xlsx"
    duplicates_df.to_excel(duplicates_path, index=False)
    print(f"✅ All duplicates saved to: {duplicates_path}")
else:
    print("✅ No duplicates found.")


# ==============================================================
# STEP 4: Determine safe vs unsafe numeric columns
# ==============================================================

grouped = df.groupby(id_cols)[numeric_cols]

# Count unique values per group
nunique_per_group = grouped.nunique()

# Safe columns: no more than 1 unique value per UNITID+Year+AWLEVEL
safe_cols = [col for col in numeric_cols if (nunique_per_group[col] <= 1).all()]

# Unsafe columns: more than 1 unique value somewhere
unsafe_cols = [col for col in numeric_cols if (nunique_per_group[col] > 1).any()]

print(f"✅ Safe columns (duplicates identical): {safe_cols}")
print(f"❌ Unsafe columns (conflicting duplicates): {unsafe_cols}")

# ==============================================================
# STEP 5: Aggregate duplicates
# ==============================================================

# Safe columns: take the first value
df_safe = df.groupby(id_cols, as_index=False)[safe_cols].first()

# Unsafe columns: sum counts across duplicates
df_unsafe = df.groupby(id_cols, as_index=False)[unsafe_cols].sum()

# Merge back together
df_clean = pd.merge(df_safe, df_unsafe, on=id_cols, how="left")

# ==============================================================
# STEP 6: Verify duplicates resolved
# ==============================================================

remaining_dupes = df_clean.duplicated(subset=id_cols).sum()
print(f"Remaining duplicates after aggregation: {remaining_dupes}")

if remaining_dupes == 0:
    print("✅ All duplicates resolved.")
else:
    print("⚠️ Some duplicates still remain! Investigate further.")

# ==============================================================
# STEP 7: Pivot to wide format safely
# ==============================================================

value_cols = [col for col in df_clean.columns if col not in id_cols]

df_wide = df_clean.pivot_table(
    index="unitid",
    columns=["year", "awlevel"],
    values=value_cols,
    aggfunc="first"  # safe now, no duplicates remain
)

# Flatten column names
df_wide.columns = [f"{col}_{year}_aw{aw}" for col, year, aw in df_wide.columns]
df_wide = df_wide.reset_index()

# ==============================================================
# STEP 8: Save final wide dataset
# ==============================================================

output_path = "/Users/co25936/Desktop/PER/IPEDS/IPEDS_WIDE_SAFE.xlsx"
df_wide.to_excel(output_path, index=False)
print(f"✅ Wide dataset saved to: {output_path}")

'''

import pandas as pd
import numpy as np
import os

input_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/IPEDS_combined_file.xlsx"
output_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/IPEDS_combined_file_LONG.xlsx"

df = pd.read_excel(input_path) 
# ==============================================================
# LONG → WIDE
# ==============================================================

id_col = "UNITID"
time_cols = ["Year", "AWLEVEL"]

value_cols = [col for col in df.columns if col not in [id_col] + time_cols]

df_wide = df.pivot_table(
    index=id_col,
    columns=time_cols,
    values=value_cols,
    aggfunc="first"   # safe since you already cleaned duplicates
)

# Flatten column names
df_wide.columns = [
    f"{var}_{year}_aw{aw}"
    for var, year, aw in df_wide.columns
]

df_wide = df_wide.reset_index()

# Save
output_path = "/Users/co25936/Desktop/PER/IPEDS/IPEDS_WIDE.xlsx"
df_wide.to_excel(output_path, index=False)

print("✅ Converted to wide format.")

'''