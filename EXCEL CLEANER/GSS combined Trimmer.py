# Goal adress the duplicats in GSS code by manual exception
# need to adress the UNITID's by hand
'''
unitid 110635  
    2008
        Sent by both the grad school and post doc office 
        Only grad school has values 
    2009
        Same error in 2009                
unitid 139658 
    2021   
        Issue due to medical physics being included as the wrong gss code 
            For ft_tot_all_races_v
                Keep the row with 58      
    2022    
        Issue due to medical physics being included as the wrong gss code 
            For ft_tot_all_races_v
            Keep the row with 56                
    2023  
        Issue due to medical physics being included as the wrong gss code 
        For ft_tot_all_races_v
            Keep the row with 63                
unitid 212054 
    2000     
        Issue due to medical physics being included as the wrong gss code 
            For ft_tot_all_races_v
                Keep the row with 13 
                Remove the row with 4        
unitid 230728 
    2009  
        Sent by both the grad school and post doc office 
        Only grad school has value         
unitid 234030
    2017
        Issue due to medical physics being included as the wrong gss code 
            For ft_tot_all_races_v
                Keep the row with 10
'''
import pandas as pd
import numpy as np

# ==============================================================
# STEP 1: Load Data
# ==============================================================

input_file = '/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/GSS_combined_file.xlsx'
output_file = '/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/GSS_combined_file_cleaned.xlsx'

df = pd.read_excel(input_file)

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# ==============================================================
# STEP 2: Helper Function
# ==============================================================

def keep_row_with_value(df, unitid, year, column, value):
    mask = (df['unitid'] == unitid) & (df['year'] == year)
    subset = df[mask]

    if not subset.empty:
        keep = subset[subset[column] == value]
        df = df[~mask]  # remove all rows for that group
        df = pd.concat([df, keep], ignore_index=True)

    return df

def keep_non_zero(df, unitid, year, column):
    mask = (df['unitid'] == unitid) & (df['year'] == year)
    subset = df[mask]

    if not subset.empty:
        keep = subset[subset[column] > 0]

        # Safety check
        if keep.empty:
            print(f"⚠️ No non-zero row found for UNITID {unitid}, YEAR {year}")
        else:
            df = df[~mask]
            df = pd.concat([df, keep], ignore_index=True)

    return df

# ==============================================================
# STEP 3: Apply Manual Fixes the format can be extended for 
# ==============================================================

# ---- UNITID 110635 (2008, 2009) -> keep row with non-0 values
df = keep_non_zero(df, 110635, 2008, 'ft_tot_all_races_v')
df = keep_non_zero(df, 110635, 2009, 'ft_tot_all_races_v')

# ---- UNITID 139658 -> keep the unitid with specific value for a column (we used ft_tot_all_races_v because it was different for the duplicates)
df = keep_row_with_value(df, 139658, 2021, 'ft_tot_all_races_v', 58)
df = keep_row_with_value(df, 139658, 2022, 'ft_tot_all_races_v', 56)
df = keep_row_with_value(df, 139658, 2023, 'ft_tot_all_races_v', 63)

# ---- UNITID 212054
df = keep_row_with_value(df, 212054, 2000, 'ft_tot_all_races_v', 13)

# ---- UNITID 230728 (2009)
df = keep_non_zero(df, 230728, 2009, 'ft_tot_all_races_v')

# ---- UNITID 234030
df = keep_row_with_value(df, 234030, 2017, 'ft_tot_all_races_v', 10)



# ==============================================================
# STEP 4: Final Deduplication Check
# ==============================================================

dupes = df[df.duplicated(subset=['unitid', 'year'], keep=False)]

if not dupes.empty:
    print("⚠️ Remaining duplicates found:")
    print(dupes.sort_values(['unitid', 'year']).head())
else:
    print("✅ No duplicate UNITID-Year rows remain")

# ==============================================================
# STEP 5: Save Cleaned File
# ==============================================================

df.to_excel(output_file, index=False)

print("✅ Cleaned GSS file saved to:", output_file)