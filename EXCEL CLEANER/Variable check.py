#read through the First Year and Crad Checker excel sheet and check each column to make sure it makes sense
# recomendation from nick create a new column and use -1 for <0, 0 for = 0 and 1 for > 0 when calculating the difference 
# Need to fix blanks as both NaN's and 0's (fixed)
# now for logic checks 
# Var list is the follwoning
'''
Variable	                how its broken up 								
dr_ft_frst_tot_all_races_v =	dr_ft_frst_tot_black_v +dr_ft_frst_tot_indian_v	+ dr_ft_frst_tot_asian_v + dr_ft_frst_tot_pacific_v + dr_ft_frst_tot_white_v +dr_ft_frst_tot_hisp_v + dr_ft_frst_tot_multi_v +dr_ft_frst_tot_unk_v + dr_ft_frst_tot_forgn_v
dr_ft_frst_tot_all_races_v =	dr_ft_frst_men_all_races_v + dr_ft_frst_wmen_all_races_v							
dr_ft_frst_tot_black_v =	dr_ft_frst_men_black_v + dr_ft_frst_wmen_black_v							
dr_ft_frst_tot_indian_v =	dr_ft_frst_men_indian_v	+ dr_ft_frst_wmen_indian_v							
dr_ft_frst_tot_asian_v =	dr_ft_frst_men_asian_v	+ dr_ft_frst_wmen_asian_v							
dr_ft_frst_tot_pacific_v =	dr_ft_frst_men_pacific_v + dr_ft_frst_wmen_pacific_v							
dr_ft_frst_tot_white_v =	dr_ft_frst_men_white_v + dr_ft_frst_wmen_white_v							
dr_ft_frst_tot_hisp_v =	dr_ft_frst_men_hisp_v + dr_ft_frst_wmen_hisp_v							
dr_ft_frst_tot_multi_v =	dr_ft_frst_men_multi_v + dr_ft_frst_wmen_multi_v							
dr_ft_frst_tot_unk_v =	dr_ft_frst_men_unk_v + dr_ft_frst_wmen_unk_v							
dr_ft_frst_tot_forgn_v =	dr_ft_frst_men_forgn_v + dr_ft_frst_wmen_forgn_v							
									
ma_ft_tot_all_races_v =	ma_ft_frst_men_all_races_v	+ ma_ft_frst_wmen_all_races_v							
ma_ft_frst_tot_black_v = 	ma_ft_frst_men_black_v	+ ma_ft_frst_wmen_black_v							
ma_ft_frst_tot_indian_v =	ma_ft_frst_men_indian_v + ma_ft_frst_wmen_indian_v							
ma_ft_frst_tot_asian_v =	ma_ft_frst_men_asian_v	+ ma_ft_frst_wmen_asian_v							
ma_ft_frst_tot_pacific_v =	ma_ft_frst_men_pacific_v + ma_ft_frst_wmen_pacific_v							
ma_ft_frst_tot_white_v =	ma_ft_frst_men_white_v + ma_ft_frst_wmen_white_v							
ma_ft_frst_tot_hisp_v =	ma_ft_frst_men_hisp_v + ma_ft_frst_wmen_hisp_v							
ma_ft_frst_tot_multi_v =	ma_ft_frst_men_multi_v	+ ma_ft_frst_wmen_multi_v							
ma_ft_frst_tot_unk_v =	ma_ft_frst_men_unk_v + ma_ft_frst_wmen_unk_v							
ma_ft_frst_tot_forgn_v =	ma_ft_frst_men_forgn_v + ma_ft_frst_wmen_forgn_v							
ma_ft_frst_men_all_races_v =	ma_ft_frst_men_black_v +	ma_ft_frst_men_indian_v	+ ma_ft_frst_men_asian_v +	ma_ft_frst_men_pacific_v +	ma_ft_frst_men_white_v +	ma_ft_frst_men_hisp_v +	ma_ft_frst_men_multi_v +	ma_ft_frst_men_unk_v +	ma_ft_frst_men_forgn_v
dr_ft_frst_men_all_races_v =	dr_ft_frst_men_black_v +	dr_ft_frst_men_indian_v +	dr_ft_frst_men_asian_v +	dr_ft_frst_men_pacific_v + 	dr_ft_frst_men_white_v +	dr_ft_frst_men_hisp_v +	dr_ft_frst_men_multi_v +	dr_ft_frst_men_unk_v +	dr_ft_frst_men_forgn_v
ma_ft_frst_wmen_all_races_v =	ma_ft_frst_wmen_black_v	+ ma_ft_frst_wmen_indian_v +	ma_ft_frst_wmen_asian_v +	ma_ft_frst_wmen_pacific_v +	ma_ft_frst_wmen_white_v +	ma_ft_frst_wmen_hisp_v +	ma_ft_frst_wmen_multi_v +	ma_ft_frst_wmen_unk_v +	ma_ft_frst_wmen_forgn_v
dr_ft_frst_wmen_all_races_v =	dr_ft_frst_wmen_black_v	+ dr_ft_frst_wmen_indian_v +	dr_ft_frst_wmen_asian_v	 + dr_ft_frst_wmen_pacific_v +	dr_ft_frst_wmen_white_v	+ dr_ft_frst_wmen_hisp_v +	dr_ft_frst_wmen_multi_v	+ dr_ft_frst_wmen_unk_v	+ dr_ft_frst_wmen_forgn_v
 'ma_ft_frst_tot_all_races_v' =	ma_ft_frst_men_all_races_v + ma_ft_frst_wmen_all_races_v							
 'dr_ft_frst_tot_all_races_v' =	dr_ft_frst_men_all_races_v	+ dr_ft_frst_wmen_all_races_v							
ma_ft_men_all_races_v =	ma_ft_men_black_v + ma_ft_men_indian_v	+ ma_ft_men_asian_v +	ma_ft_men_pacific_v +	ma_ft_men_white_v + ma_ft_men_hisp_v +	ma_ft_men_multi_v +	ma_ft_men_unk_v	+ ma_ft_men_forgn_v
dr_ft_men_all_races_v =	dr_ft_men_black_v + dr_ft_men_indian_v	+ dr_ft_men_asian_v	+ dr_ft_men_pacific_v	+ dr_ft_men_white_v	+ dr_ft_men_hisp_v +	dr_ft_men_multi_v +	dr_ft_men_unk_v	+ dr_ft_men_forgn_v
ma_ft_wmen_all_races_v =	ma_ft_wmen_black_v + ma_ft_wmen_indian_v	+ ma_ft_wmen_asian_v + ma_ft_wmen_pacific_v +	ma_ft_wmen_white_v +	ma_ft_wmen_hisp_v +	ma_ft_wmen_multi_v +	ma_ft_wmen_unk_v +	ma_ft_wmen_forgn_v
dr_ft_wmen_all_races_v =	dr_ft_wmen_black_v + dr_ft_wmen_indian_v +	dr_ft_wmen_asian_v + dr_ft_wmen_pacific_v +	dr_ft_wmen_white_v +	dr_ft_wmen_hisp_v +	dr_ft_wmen_multi_v +	dr_ft_wmen_unk_v +	dr_ft_wmen_forgn_v
ma_ft_tot_all_races_v =	ma_ft_tot_black_v +	ma_ft_tot_indian_v +	ma_ft_tot_asian_v +	ma_ft_tot_pacific_v +	ma_ft_tot_white_v +	ma_ft_tot_hisp_v +	ma_ft_tot_multi_v +	ma_ft_tot_unk_v +	ma_ft_tot_forgn_v
dr_ft_tot_all_races_v =	dr_ft_tot_black_v +	dr_ft_tot_indian_v +	dr_ft_tot_asian_v +	dr_ft_tot_pacific_v	+ dr_ft_tot_white_v	+ dr_ft_tot_hisp_v +	dr_ft_tot_multi_v +	dr_ft_tot_unk_v	+ dr_ft_tot_forgn_v
ft_frst_men_all_races_v =	ma_ft_frst_men_all_races_v + dr_ft_frst_men_all_races_v							
 'ft_frst_men_all_races_v' =	ft_frst_men_black_v +	ft_frst_men_indian_v +	ft_frst_men_asian_v	+ ft_frst_men_pacific_v +ft_frst_men_white_v + ft_frst_men_hisp_v +	ft_frst_men_multi_v	+ ft_frst_men_unk_v	+ ft_frst_men_forgn_v
 'ft_frst_wmen_all_races_v' =	ma_ft_frst_wmen_all_races_v	+ dr_ft_frst_wmen_all_races_v							
 'ft_frst_wmen_all_races_v' =	ft_frst_wmen_black_v +	ft_frst_wmen_indian_v +	ft_frst_wmen_asian_v +	ft_frst_wmen_pacific_v + ft_frst_wmen_white_v + ft_frst_wmen_hisp_v + ft_frst_wmen_multi_v + ft_frst_wmen_unk_v	+ ft_frst_wmen_forgn_v
"ft_tot_all_races_v" =	"ft_tot_black_v" +"ft_tot_indian_v"	+ "ft_tot_asian_v" + "ft_tot_pacific_v" + "ft_tot_white_v" + "ft_tot_hisp_v" +"ft_tot_multi_v" + "ft_tot_unk_v"	 + "ft_tot_forgn_v"
"ft_frst_tot_all_races_v" =	"ft_frst_tot_black_v" + "ft_frst_tot_indian_v" +	"ft_frst_tot_asian_v" +	"ft_frst_tot_pacific_v"	+ "ft_frst_tot_white_v" + "ft_frst_tot_hisp_v"	+ "ft_frst_tot_multi_v" +"ft_frst_tot_unk_v" + "ft_frst_tot_forgn_v"
"CTOTALT" =	CTOTALM + CTOTALW							
"CTOTALT" =	'CRACE17' + CRACE18' +	CRACE19' +	'CRACE20' +	CRACE21' +	'CRACE22' +	CUNKNT'		
"CTOTALT" =	'CNRALT' +	'CBKAAT' +	CNHPIT' +	CASIAT' +	'CHISPT' +	CWHITT' + CUNKNT' + C2MORT'	

'''

# ISUE fixed

# =============================================================================
# VARIABLE BREAKDOWN REFERENCE
# =============================================================================
# 
# Source file:
#   /Users/co25936/Desktop/PER/IPEDS/FirstYear and Grad Checker.xlsx
#   (Variables found in Row 1)
# 
# -----------------------------------------------------------------------------
# DOCTORAL - FULL-TIME - FIRST-TIME
# -----------------------------------------------------------------------------
# dr_ft_frst_tot_all_races_v = dr_ft_frst_tot_black_v + dr_ft_frst_tot_indian_v + dr_ft_frst_tot_asian_v
#                            + dr_ft_frst_tot_pacific_v + dr_ft_frst_tot_white_v + dr_ft_frst_tot_hisp_v
#                            + dr_ft_frst_tot_multi_v + dr_ft_frst_tot_unk_v + dr_ft_frst_tot_forgn_v
#
# dr_ft_frst_tot_all_races_v = dr_ft_frst_men_all_races_v + dr_ft_frst_wmen_all_races_v
# dr_ft_frst_tot_black_v      = dr_ft_frst_men_black_v    + dr_ft_frst_wmen_black_v
# dr_ft_frst_tot_indian_v     = dr_ft_frst_men_indian_v   + dr_ft_frst_wmen_indian_v
# dr_ft_frst_tot_asian_v      = dr_ft_frst_men_asian_v    + dr_ft_frst_wmen_asian_v
# dr_ft_frst_tot_pacific_v    = dr_ft_frst_men_pacific_v  + dr_ft_frst_wmen_pacific_v
# dr_ft_frst_tot_white_v      = dr_ft_frst_men_white_v    + dr_ft_frst_wmen_white_v
# dr_ft_frst_tot_hisp_v       = dr_ft_frst_men_hisp_v     + dr_ft_frst_wmen_hisp_v
# dr_ft_frst_tot_multi_v      = dr_ft_frst_men_multi_v    + dr_ft_frst_wmen_multi_v
# dr_ft_frst_tot_unk_v        = dr_ft_frst_men_unk_v      + dr_ft_frst_wmen_unk_v
# dr_ft_frst_tot_forgn_v      = dr_ft_frst_men_forgn_v    + dr_ft_frst_wmen_forgn_v
#
# -----------------------------------------------------------------------------
# MASTER'S - FULL-TIME - FIRST-TIME
# -----------------------------------------------------------------------------
# ma_ft_tot_all_races_v     = ma_ft_frst_men_all_races_v + ma_ft_frst_wmen_all_races_v
# ma_ft_frst_tot_black_v    = ma_ft_frst_men_black_v     + ma_ft_frst_wmen_black_v
# ma_ft_frst_tot_indian_v   = ma_ft_frst_men_indian_v    + ma_ft_frst_wmen_indian_v
# ma_ft_frst_tot_asian_v    = ma_ft_frst_men_asian_v     + ma_ft_frst_wmen_asian_v
# ma_ft_frst_tot_pacific_v  = ma_ft_frst_men_pacific_v   + ma_ft_frst_wmen_pacific_v
# ma_ft_frst_tot_white_v    = ma_ft_frst_men_white_v     + ma_ft_frst_wmen_white_v
# ma_ft_frst_tot_hisp_v     = ma_ft_frst_men_hisp_v      + ma_ft_frst_wmen_hisp_v
# ma_ft_frst_tot_multi_v    = ma_ft_frst_men_multi_v     + ma_ft_frst_wmen_multi_v
# ma_ft_frst_tot_unk_v      = ma_ft_frst_men_unk_v       + ma_ft_frst_wmen_unk_v
# ma_ft_frst_tot_forgn_v    = ma_ft_frst_men_forgn_v     + ma_ft_frst_wmen_forgn_v
#
# ma_ft_frst_men_all_races_v = ma_ft_frst_men_black_v + ma_ft_frst_men_indian_v + ma_ft_frst_men_asian_v
#                            + ma_ft_frst_men_pacific_v + ma_ft_frst_men_white_v + ma_ft_frst_men_hisp_v
#                            + ma_ft_frst_men_multi_v + ma_ft_frst_men_unk_v + ma_ft_frst_men_forgn_v
#
# dr_ft_frst_men_all_races_v = dr_ft_frst_men_black_v + dr_ft_frst_men_indian_v + dr_ft_frst_men_asian_v
#                            + dr_ft_frst_men_pacific_v + dr_ft_frst_men_white_v + dr_ft_frst_men_hisp_v
#                            + dr_ft_frst_men_multi_v + dr_ft_frst_men_unk_v + dr_ft_frst_men_forgn_v
#
# ma_ft_frst_wmen_all_races_v = ma_ft_frst_wmen_black_v + ma_ft_frst_wmen_indian_v + ma_ft_frst_wmen_asian_v
#                             + ma_ft_frst_wmen_pacific_v + ma_ft_frst_wmen_white_v + ma_ft_frst_wmen_hisp_v
#                             + ma_ft_frst_wmen_multi_v + ma_ft_frst_wmen_unk_v + ma_ft_frst_wmen_forgn_v
#
# dr_ft_frst_wmen_all_races_v = dr_ft_frst_wmen_black_v + dr_ft_frst_wmen_indian_v + dr_ft_frst_wmen_asian_v
#                             + dr_ft_frst_wmen_pacific_v + dr_ft_frst_wmen_white_v + dr_ft_frst_wmen_hisp_v
#                             + dr_ft_frst_wmen_multi_v + dr_ft_frst_wmen_unk_v + dr_ft_frst_wmen_forgn_v
#
# -----------------------------------------------------------------------------
# FULL-TIME - MEN & WOMEN (ALL RACES)
# -----------------------------------------------------------------------------
# ma_ft_men_all_races_v = ma_ft_men_black_v + ma_ft_men_indian_v + ma_ft_men_asian_v
#                        + ma_ft_men_pacific_v + ma_ft_men_white_v + ma_ft_men_hisp_v
#                        + ma_ft_men_multi_v + ma_ft_men_unk_v + ma_ft_men_forgn_v
#
# dr_ft_men_all_races_v = dr_ft_men_black_v + dr_ft_men_indian_v + dr_ft_men_asian_v
#                        + dr_ft_men_pacific_v + dr_ft_men_white_v + dr_ft_men_hisp_v
#                        + dr_ft_men_multi_v + dr_ft_men_unk_v + dr_ft_men_forgn_v
#
# ma_ft_wmen_all_races_v = ma_ft_wmen_black_v + ma_ft_wmen_indian_v + ma_ft_wmen_asian_v
#                         + ma_ft_wmen_pacific_v + ma_ft_wmen_white_v + ma_ft_wmen_hisp_v
#                         + ma_ft_wmen_multi_v + ma_ft_wmen_unk_v + ma_ft_wmen_forgn_v
#
# dr_ft_wmen_all_races_v = dr_ft_wmen_black_v + dr_ft_wmen_indian_v + dr_ft_wmen_asian_v
#                         + dr_ft_wmen_pacific_v + dr_ft_wmen_white_v + dr_ft_wmen_hisp_v
#                         + dr_ft_wmen_multi_v + dr_ft_wmen_unk_v + dr_ft_wmen_forgn_v
#
# -----------------------------------------------------------------------------
# FULL-TIME - TOTALS BY RACE
# -----------------------------------------------------------------------------
# ma_ft_tot_all_races_v = ma_ft_tot_black_v + ma_ft_tot_indian_v + ma_ft_tot_asian_v
#                        + ma_ft_tot_pacific_v + ma_ft_tot_white_v + ma_ft_tot_hisp_v
#                        + ma_ft_tot_multi_v + ma_ft_tot_unk_v + ma_ft_tot_forgn_v
#
# dr_ft_tot_all_races_v = dr_ft_tot_black_v + dr_ft_tot_indian_v + dr_ft_tot_asian_v
#                        + dr_ft_tot_pacific_v + dr_ft_tot_white_v + dr_ft_tot_hisp_v
#                        + dr_ft_tot_multi_v + dr_ft_tot_unk_v + dr_ft_tot_forgn_v
#
# -----------------------------------------------------------------------------
# COMBINED FULL-TIME - FIRST-TIME (MEN & WOMEN)
# -----------------------------------------------------------------------------
# ft_frst_men_all_races_v   = ma_ft_frst_men_all_races_v + dr_ft_frst_men_all_races_v
# ft_frst_men_all_races_v   = ft_frst_men_black_v + ft_frst_men_indian_v + ft_frst_men_asian_v
#                           + ft_frst_men_pacific_v + ft_frst_men_white_v + ft_frst_men_hisp_v
#                           + ft_frst_men_multi_v + ft_frst_men_unk_v + ft_frst_men_forgn_v
#
# ft_frst_wmen_all_races_v  = ma_ft_frst_wmen_all_races_v + dr_ft_frst_wmen_all_races_v
# ft_frst_wmen_all_races_v  = ft_frst_wmen_black_v + ft_frst_wmen_indian_v + ft_frst_wmen_asian_v
#                           + ft_frst_wmen_pacific_v + ft_frst_wmen_white_v + ft_frst_wmen_hisp_v
#                           + ft_frst_wmen_multi_v + ft_frst_wmen_unk_v + ft_frst_wmen_forgn_v
#
# -----------------------------------------------------------------------------
# TOTALS
# -----------------------------------------------------------------------------
# ft_tot_all_races_v       = ft_tot_black_v + ft_tot_indian_v + ft_tot_asian_v
#                          + ft_tot_pacific_v + ft_tot_white_v + ft_tot_hisp_v
#                          + ft_tot_multi_v + ft_tot_unk_v + ft_tot_forgn_v
#
# ft_frst_tot_all_races_v  = ft_frst_tot_black_v + ft_frst_tot_indian_v + ft_frst_tot_asian_v
#                          + ft_frst_tot_pacific_v + ft_frst_tot_white_v + ft_frst_tot_hisp_v
#                          + ft_frst_tot_multi_v + ft_frst_tot_unk_v + ft_frst_tot_forgn_v
#
# CTOTALT = CTOTALM + CTOTALW
# CTOTALT = CRACE17 + CRACE18 + CRACE19 + CRACE20 + CRACE21 + CRACE22 + CUNKNT
# CTOTALT = CNRALT + CBKAAT + CNHPIT + CASIAT + CHISPT + CWHITT + CUNKNT + C2MORT
# =============================================================================


import pandas as pd
import numpy as np
import re

# --- File paths ---
data_path = "/Users/co25936/Desktop/PER/IPEDS/FirstYear and Grad Checker.xlsx"
output_path = "/Users/co25936/Desktop/PER/IPEDS/Variable_Check.xlsx"
relationships_path = "/Users/co25936/Desktop/PER/IPEDS/variable relationships.txt"

# --- Load data ---
df = pd.read_excel(data_path)
col_map = {col.lower(): col for col in df.columns}
df_lower = df.rename(columns=str.lower)

# Confirm UNITID column exists
if "unitid" not in df_lower.columns:
    raise ValueError("'UNITID' column not found in your Excel file. Please verify the column name.")

# --- Filter to years 2010–2023 ---
df_lower = df_lower[(df_lower["year"] >= 2017)].copy()
# --- Load relationships text ---
with open(relationships_path, "r") as f:
    relationships_text = f.read()

# --- Parse relationships (multiple per variable) ---
pattern = r'["\']?([\w\d_]+)["\']?\s*=\s*(.+)'
variable_map = {}

for line in relationships_text.splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue

    match = re.match(pattern, line)
    if not match:
        continue

    total_var, rhs = match.groups()
    components = re.findall(r'["\']?([\w\d_]+)["\']?', rhs)
    components = [c for c in components if c.lower() != total_var.lower()]

    total_var_lc = total_var.lower()
    if total_var_lc not in variable_map:
        variable_map[total_var_lc] = []
    variable_map[total_var_lc].append([c.lower() for c in components])

# --- Perform checks ---
results = []
row_diff_data = pd.DataFrame(index=df_lower.index)  # to store row-level diffs

for total_var, list_of_equations in variable_map.items():
    for i, components in enumerate(list_of_equations, 1):
        # Identify missing columns
        missing_cols = [c for c in [total_var] + components if c not in df_lower.columns]
        if missing_cols:
            results.append({
                "Variable": total_var,
                "Equation #": i,
                "Components": ", ".join(components),
                "Status": "MISSING COLUMNS",
                "Missing Columns": ", ".join(missing_cols),
                "Total Difference": np.nan,
            })
            continue

        # Compute signed difference
        df_lower["check_sum"] = df_lower[components].sum(axis=1)
        diff = df_lower[total_var] - df_lower["check_sum"]

        # Save row-level signed differences
        diff_col_name = f"diff_{total_var}_eq{i}"
        row_diff_data[diff_col_name] = diff

        # Check pass/fail using absolute tolerance
        pass_check = diff.abs().max() < 1e-6

        results.append({
            "Variable": total_var,
            "Equation #": i,
            "Components": ", ".join(components),
            "Status": "PASS" if pass_check else "FAIL",
            "Missing Columns": "",
            "Total Difference": diff.sum(),  # signed sum
        })

# --- Add UNITID as first column ---
row_diff_data.insert(0, "UNITID", df_lower["unitid"].values)
row_diff_data.insert(1, "Year", df_lower["year"].values)

# --- Save results ---
check_df = pd.DataFrame(results)

with pd.ExcelWriter(output_path) as writer:
    check_df.to_excel(writer, sheet_name="Variable_Check", index=False)
    row_diff_data.to_excel(writer, sheet_name="Row_Differences", index=False)

print(f"Variable check completed with signed and total differences.\nResults saved to:\n{output_path}")




'''
import pandas as pd
import numpy as np
import re

# --- File paths ---
data_path = "/Users/co25936/Desktop/PER/IPEDS/FirstYear and Grad Checker.xlsx"
output_path = "/Users/co25936/Desktop/PER/IPEDS/Variable_Check.xlsx"
relationships_path = "/Users/co25936/Desktop/PER/IPEDS/variable relationships.txt"

# --- Load data ---
df = pd.read_excel(data_path)
col_map = {col.lower(): col for col in df.columns}
df_lower = df.rename(columns=str.lower)

# --- Load relationships text ---
with open(relationships_path, "r") as f:
    relationships_text = f.read()

# --- Parse relationships (multiple per variable) ---
pattern = r'["\']?([\w\d_]+)["\']?\s*=\s*(.+)'
variable_map = {}

for line in relationships_text.splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue

    match = re.match(pattern, line)
    if not match:
        continue

    total_var, rhs = match.groups()
    components = re.findall(r'["\']?([\w\d_]+)["\']?', rhs)
    components = [c for c in components if c.lower() != total_var.lower()]

    total_var_lc = total_var.lower()
    if total_var_lc not in variable_map:
        variable_map[total_var_lc] = []
    variable_map[total_var_lc].append([c.lower() for c in components])

# --- Perform checks ---
results = []

for total_var, list_of_equations in variable_map.items():
    for i, components in enumerate(list_of_equations, 1):
        # Identify missing columns
        missing_cols = [c for c in [total_var] + components if c not in df_lower.columns]
        if missing_cols:
            results.append({
                "Variable": total_var,
                "Equation #": i,
                "Components": ", ".join(components),
                "Status": "MISSING COLUMNS",
                "Missing Columns": ", ".join(missing_cols),
                "Max Diff": np.nan,
            })
            continue

        # Compute difference
        df_lower["check_sum"] = df_lower[components].sum(axis=1)

        # Signed difference: positive if total > sum(components), negative otherwise
        diff = df_lower[total_var] - df_lower["check_sum"]

        # Pass if all differences are close to zero
        pass_check = diff.abs().max() < 1e-6

        results.append({
            "Variable": total_var,
            "Equation #": i,
            "Components": ", ".join(components),
            "Status": "PASS" if pass_check else "FAIL",
            "Missing Columns": "",
            "Max Diff": diff.max(),
        })

# --- Save results ---
check_df = pd.DataFrame(results)
with pd.ExcelWriter(output_path) as writer:
    check_df.to_excel(writer, sheet_name="Variable_Check", index=False)

print(f"✅ Variable check completed with multiple equations per variable.\nResults saved to:\n{output_path}")
'''