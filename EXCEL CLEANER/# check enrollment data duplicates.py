# check enrollment data duplicates 
import pandas as pd

# Step 0: Load your data
input_path = "/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_COMBINED_WIDE.xlsx"
df = pd.read_excel(input_path) 


# Step 1: Identify all columns containing ft_tot or ft_frst
ft_cols = [col for col in df.columns if 'ft_tot' in col or 'ft_frst' in col]

# Step 2: Find unitids with multiple awlevels (at least 7 and 17)
unis_with_both = df.groupby('unitid')['awlevel'].nunique()
unis_with_both = unis_with_both[unis_with_both > 1].index  # can adjust if you want specifically 7 & 17

# Step 3: Filter DataFrame
df_check = df[df['unitid'].isin(unis_with_both)]

# Step 4: Compare ft columns per UNITID
mismatched_cols_per_unit = {}

for unit in df_check['unitid'].unique():
    unit_df = df_check[df_check['unitid'] == unit][ft_cols]
    # Compare all rows: if all rows are identical, difference will be 0
    if (unit_df.nunique() > 1).any():
        mismatched_cols = unit_df.columns[unit_df.nunique() > 1].tolist()
    else:
        mismatched_cols = []
    mismatched_cols_per_unit[unit] = mismatched_cols

# Step 5: Create summary DataFrame
summary_df = pd.DataFrame({
    'mismatched_columns': mismatched_cols_per_unit
})
summary_df.index.name = 'unitid'
summary_df['all_ft_equal'] = summary_df['mismatched_columns'].apply(lambda x: len(x) == 0)

# Step 6: Show only unitids with mismatches
mismatches_only = summary_df[~summary_df['all_ft_equal']]

print("Summary of unitids with mismatched ft columns:")
print(mismatches_only)