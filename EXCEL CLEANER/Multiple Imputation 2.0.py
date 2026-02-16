import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer

# ==============================================================
# STEP 1: Load and Impute Missing Values
# ==============================================================

input_path = '/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_Combined_file.xlsx'
#input_path = "/Users/co25936/Desktop/PER/IPEDS/complete_with_offsets_and_PA_noIPEDS_All_UNITIDS.xlsx"
output_path = "/Users/co25936/Desktop/PER/IPEDS/complete_with_imputation.xlsx"


# Load data
df = pd.read_excel(input_path)
df.columns = df.columns.str.strip().str.lower()


# Ensure required columns
required_cols = ["ctotalt"]
# required_cols = ["ctotalt", "first"]
if not set(required_cols).issubset(df.columns):
    raise ValueError("Missing required columns: 'CTOTALT' and/or 'first'.")

# Impute missing values for CTOTALT and first
imputer = IterativeImputer(random_state=42, max_iter=10, min_value=0)
impute_data = df[required_cols].copy()
imputed_values = imputer.fit_transform(impute_data)
# ROUND THE IMPUTED VALUES TO BE WHOLE NUMBERS
df_imputed = pd.DataFrame(np.round(imputed_values).astype(int), columns=required_cols)
df[required_cols] = df_imputed

df.to_excel(output_path, index=False)
print(f" MICE imputation complete. Saved file: {output_path}")

# ==============================================================
# STEP 2: Filter for 2010–2023
# ==============================================================

if "year" not in df.columns:
    raise ValueError("Column 'year' not found in dataset.")

df = df[(df["year"] >= 2010) & (df["year"] <= 2023)].copy()

import pandas as pd
import numpy as np
import os


# ==============================================================
# FILTER OUT MASTERS-ONLY INSTITUTIONS
# ==============================================================

# UNITIDs that ever grant PhDs (AWLEVEL 9 or 17)
phd_unitids = (
    df.loc[df["awlevel"].isin([9, 17]), "unitid"]
    .dropna()
    .unique()
)

# Keep only institutions that offer PhDs
df = df[df["unitid"].isin(phd_unitids)].copy()

print(f"Remaining institutions after PhD filter: {df['unitid'].nunique()}")


# ==============================================================
# Updated Categories with Total Variables
# ==============================================================
categories = {
    "Total": {
        "comp": "ctotalt", 
        "first": "ft_frst_tot_all_races_v",
        "total": "ft_tot_all_races_v",
        "awlevel": [7, 9, 17]
    },
    "Men": {
        "comp": "ctotalm", 
        "first": "ft_frst_men_all_races_v",
        "total": "ft_men_all_races_v",
        "awlevel": [7, 9, 17]
    },
    "Women": {
        "comp": "ctotalw", 
        "first": "ft_frst_wmen_all_races_v",
        "total": "ft_wmen_all_races_v",
        "awlevel": [7, 9, 17]
    },
    'Doctor': {
        "comp": "ctotalt", 
        "first": "dr_ft_frst_tot_all_races_v",
        "total": "dr_ft_tot_all_races_v",
        "awlevel": [9, 17]
    },
    "Men Doctor": {
        "comp": "ctotalm", 
        "first": "dr_ft_frst_men_all_races_v",
        "total": "dr_ft_men_all_races_v",
        "awlevel": [9, 17]
    },
    "Women Doctor": {
        "comp": "ctotalw", 
        "first": "dr_ft_frst_wmen_all_races_v",
        "total": "dr_ft_wmen_all_races_v",
        "awlevel": [9, 17]
    },

    "White": {
        "comp": "cwhitt", 
        "first": "ft_frst_tot_white_v",
        "total": "ft_tot_white_v",
        "awlevel": [7, 9, 17]
    },
    "Asian": {
        "comp": "casiat", 
        "first": "ft_frst_tot_asian_v",
        "total": "ft_tot_asian_v",
        "awlevel": [7, 9, 17]
    },
    "Black": {
        "comp": "cbkaat", 
        "first": "ft_frst_tot_black_v",
        "total": "ft_tot_black_v",
        "awlevel": [7, 9, 17]
    },
    "Hispanic": {
        "comp": "chispt", 
        "first": "ft_frst_tot_hisp_v",
        "total": "ft_tot_hisp_v",
        "awlevel": [7, 9, 17]
    },
   "Native Hawaiian /Pacific islander" : {
        "comp": "cnhpit", 
        "first": "ft_frst_tot_pacific_v",
        "total": "ft_tot_pacific_v",
        "awlevel": [7, 9, 17]
    },
    "2 or more"  : {
        "comp": "c2mort", 
        "first": "ft_frst_tot_multi_v",
        "total": "ft_tot_multi_v",
        "awlevel": [7, 9, 17]
    },
    "Unknown"  : {
        "comp": "cunknt", 
        "first": "ft_frst_tot_unk_v",
        "total": "ft_tot_unk_v",
        "awlevel": [7, 9, 17]
    },
    "Foreign"  : {
        "comp": "cnralt", 
        "first": "ft_frst_tot_forgn_v",
        "total": "ft_tot_forgn_v",
        "awlevel": [7, 9, 17]
    },
    "White Men": {
        "comp": "cwhitm", 
        "first": "ft_frst_men_white_v",
        "total": "ft_men_white_v",
        "awlevel": [7, 9, 17]
    },
    "Asian Men": {
        "comp": "casiam", 
        "first": "ft_frst_men_asian_v",
        "total": "ft_men_asian_v",
        "awlevel": [7, 9, 17]
    },
    "Black Men": {
        "comp": "cbkaam", 
        "first": "ft_frst_men_black_v",
        "total": "ft_men_black_v",
        "awlevel": [7, 9, 17]
    },
    "Hispanic Men": {
        "comp": "chispm", 
        "first": "ft_frst_men_hisp_v",
        "total": "ft_men_hisp_v",
        "awlevel": [7, 9, 17]
    },

   "Native Hawaiian /Pacific islander Men" : {
        "comp": "cnhpim", 
        "first": "ft_frst_men_pacific_v",
        "total": "ft_men_pacific_v",
        "awlevel": [7, 9, 17]
    },
    "2 or more Men"  : {
        "comp": "c2morm", 
        "first": "ft_frst_men_multi_v",
        "total": "ft_men_multi_v",
        "awlevel": [7, 9, 17]
    },
    "Unknown Men"  : {
        "comp": "cunknm", 
        "first": "ft_frst_men_unk_v",
        "total": "ft_men_unk_v",
        "awlevel": [7, 9, 17]
    },
    "Foreign Men"  : {
        "comp": "cnralm", 
        "first": "ft_frst_men_forgn_v",
        "total": "ft_men_forgn_v",
        "awlevel": [7, 9, 17]
    },
    "White Women": {
        "comp": "cwhitw", 
        "first": "ft_frst_wmen_white_v",
        "total": "ft_wmen_white_v",
        "awlevel": [7, 9, 17]
    },
    "Asian Women": {
        "comp": "casiaw", 
        "first": "ft_frst_wmen_asian_v",
        "total": "ft_wmen_asian_v",
        "awlevel": [7, 9, 17]
    },
    "Black Women": {
        "comp": "cbkaaw", 
        "first": "ft_frst_wmen_black_v",
        "total": "ft_wmen_black_v",
        "awlevel": [7, 9, 17]
    },
    "Hispanic Women": {
        "comp": "chispw", 
        "first": "ft_frst_wmen_hisp_v",
        "total": "ft_wmen_hisp_v",
        "awlevel": [7, 9, 17]
    },
   "Native Hawaiian /Pacific islander Women" : {
        "comp": "cnhpiw", 
        "first": "ft_frst_wmen_pacific_v",
        "total": "ft_wmen_pacific_v",
        "awlevel": [7, 9, 17]
    },
    "2 or more Women"  : {
        "comp": "c2morw", 
        "first": "ft_frst_wmen_multi_v",
        "total": "ft_wmen_multi_v",
        "awlevel": [7, 9, 17]
    },
    "Unknown Women"  : {
        "comp": "cunknw", 
        "first": "ft_frst_wmen_unk_v",
        "total": "ft_wmen_unk_v",
        "awlevel": [7, 9, 17]
    },
    "Foreign Women"  : {
        "comp": "cnralw", 
        "first": "ft_frst_wmen_forgn_v",
        "total": "ft_wmen_forgn_v",
        "awlevel": [7, 9, 17]
    },
    "White Doctor": {
        "comp": "cwhitt", 
        "first": "dr_ft_frst_tot_white_v",
        "total": "dr_ft_tot_white_v",
        "awlevel": [9, 17]
    },
    "Asian Doctor": {
        "comp": "casiat", 
        "first": "dr_ft_frst_tot_asian_v",
        "total": "dr_ft_tot_asian_v",
        "awlevel": [9, 17]
    },
    "Black Doctor": {
        "comp": "cbkaat", 
        "first": "dr_ft_frst_tot_black_v",
        "total": "dr_ft_tot_black_v",
        "awlevel": [9, 17]
    },
    "Hispanic Doctor": {
        "comp": "chispt", 
        "first": "dr_ft_frst_tot_hisp_v",
        "total": "dr_ft_tot_hisp_v",
        "awlevel": [9, 17]
    },
   "Native Hawaiian /Pacific islander Doctor" : {
        "comp": "cnhpit", 
        "first": "dr_ft_frst_tot_pacific_v",
        "total": "dr_ft_tot_pacific_v",
        "awlevel": [9, 17]
    },
    "2 or more Doctor"  : {
        "comp": "c2mort", 
        "first": "dr_ft_frst_tot_multi_v",
        "total": "dr_ft_tot_multi_v",
        "awlevel": [9, 17]
    },
    "Unknown Doctor"  : {
        "comp": "cunknt", 
        "first": "dr_ft_frst_tot_unk_v",
        "total": "dr_ft_tot_unk_v",
        "awlevel": [9, 17]
    },
    "Foreign Doctor"  : {
        "comp": "cnralt", 
        "first": "dr_ft_frst_tot_forgn_v",
        "total": "dr_ft_tot_forgn_v",
        "awlevel": [9, 17]
    },

    "White Men Doctor": {
        "comp": "cwhitm", 
        "first": "dr_ft_frst_men_white_v",
        "total": "dr_ft_men_white_v",
        "awlevel": [9, 17]
    },
    "Asian Men Doctor": {
        "comp": "casiam", 
        "first": "dr_ft_frst_men_asian_v",
        "total": "dr_ft_men_asian_v",
        "awlevel": [9, 17]
    },
    "Black Men Doctor": {
        "comp": "cbkaam", 
        "first": "dr_ft_frst_men_black_v",
        "total": "dr_ft_men_black_v",
        "awlevel": [9, 17]
    },
    "Hispanic Men Doctor": {
        "comp": "chispm", 
        "first": "dr_ft_frst_men_hisp_v",
        "total": "dr_ft_men_hisp_v",
        "awlevel": [9, 17]
    },
   "Native Hawaiian /Pacific islander Men Doctor" : {
        "comp": "cnhpim", 
        "first": "dr_ft_frst_men_pacific_v",
        "total": "dr_ft_men_pacific_v",
        "awlevel": [9, 17]
    },
    "2 or more Men Doctor"  : {
        "comp": "c2morm", 
        "first": "dr_ft_frst_men_multi_v",
        "total": "dr_ft_men_multi_v",
        "awlevel": [9, 17]
    },
    "Unknown Men Doctor"  : {
        "comp": "cunknm", 
        "first": "dr_ft_frst_men_unk_v",
        "total": "dr_ft_men_unk_v",
        "awlevel": [9, 17]
    },
    "Foreign Men Doctor"  : {
        "comp": "cnralm", 
        "first": "dr_ft_frst_men_forgn_v",
        "total": "dr_ft_men_forgn_v",
        "awlevel": [9, 17]
    },
    "White Women Doctor": {
        "comp": "cwhitw", 
        "first": "dr_ft_frst_wmen_white_v",
        "total": "dr_ft_wmen_white_v",
        "awlevel": [9, 17]
    },
    "Asian Women Doctor": {
        "comp": "casiaw", 
        "first": "dr_ft_frst_wmen_asian_v",
        "total": "dr_ft_wmen_asian_v",
        "awlevel": [9, 17]
    },
    "Black Women Doctor": {
        "comp": "cbkaaw", 
        "first": "dr_ft_frst_wmen_black_v",
        "total": "dr_ft_wmen_black_v",
        "awlevel": [9, 17]
    },
    "Hispanic Women Doctor": {
        "comp": "chispw", 
        "first": "dr_ft_frst_wmen_hisp_v",
        "total": "dr_ft_wmen_hisp_v",
        "awlevel": [9, 17]
    },
   "Native Hawaiian /Pacific islander Women Doctor" : {
        "comp": "cnhpiw", 
        "first": "dr_ft_frst_wmen_pacific_v",
        "total": "dr_ft_wmen_pacific_v",
        "awlevel": [9, 17]
    },
    "2 or more Women Doctor"  : {
        "comp": "c2morw", 
        "first": "dr_ft_frst_wmen_multi_v",
        "total": "dr_ft_wmen_multi_v",
        "awlevel": [9, 17]
    },
    "Unknown Women Doctor"  : {
        "comp": "cunknw", 
        "first": "dr_ft_frst_wmen_unk_v",
        "total": "dr_ft_wmen_unk_v",
        "awlevel": [9, 17]
    },
    "Foreign Women Doctor"  : {
        "comp": "cnralw", 
        "first": "dr_ft_frst_wmen_forgn_v",
        "total": "dr_ft_wmen_forgn_v",
        "awlevel": [9, 17]
    },


    'Masters': {
        "comp": "ctotalt", 
        "first": "ma_ft_frst_tot_all_races_v",
        "total": "ma_ft_tot_all_races_v",
        "awlevel": [7]
    },
    "White Masters": {
        "comp": "cwhitt", 
        "first": "ma_ft_frst_tot_white_v",
        "total": "ma_ft_tot_white_v",
        "awlevel": [7]
    },
    "Asian Masters": {
        "comp": "casiat", 
        "first": "ma_ft_frst_tot_asian_v",
        "total": "ma_ft_tot_asian_v",
        "awlevel": [7]
    },
    "Black Masters": {
        "comp": "cbkaat", 
        "first": "ma_ft_frst_tot_black_v",
        "total": "ma_ft_tot_black_v",
        "awlevel": [7]
    },
    "Hispanic Masters": {
        "comp": "chispt", 
        "first": "ma_ft_frst_tot_hisp_v",
        "total": "ma_ft_tot_hisp_v",
        "awlevel": [7]
    },
   "Native Hawaiian /Pacific islander Masters" : {
        "comp": "cnhpit", 
        "first": "ma_ft_frst_tot_pacific_v",
        "total": "ma_ft_tot_pacific_v",
        "awlevel": [7]
    },
    "2 or more Masters"  : {
        "comp": "c2mort", 
        "first": "ma_ft_frst_tot_multi_v",
        "total": "ma_ft_tot_multi_v",
        "awlevel": [7]
    },
    "Unknown Masters"  : {
        "comp": "cunknt", 
        "first": "ma_ft_frst_tot_unk_v",
        "total": "ma_ft_tot_unk_v",
        "awlevel": [7]
    },
    "Foreign Masters"  : {
        "comp": "cnralt", 
        "first": "ma_ft_frst_tot_forgn_v",
        "total": "ma_ft_tot_forgn_v",
        "awlevel": [7]
    },

    "White Men Masters": {
        "comp": "cwhitm", 
        "first": "ma_ft_frst_men_white_v",
        "total": "ma_ft_men_white_v",
        "awlevel": [7]
    },
    "Asian Men Masters": {
        "comp": "casiam", 
        "first": "ma_ft_frst_men_asian_v",
        "total": "ma_ft_men_asian_v",
        "awlevel": [7]
    },
    "Black Men Masters": {
        "comp": "cbkaam", 
        "first": "ma_ft_frst_men_black_v",
        "total": "ma_ft_men_black_v",
        "awlevel": [7]
    },
    "Hispanic Men Masters": {
        "comp": "chispm", 
        "first": "ma_ft_frst_men_hisp_v",
        "total": "ma_ft_men_hisp_v",
        "awlevel": [7]
    },

   "Native Hawaiian /Pacific islander Men Masters" : {
        "comp": "cnhpim", 
        "first": "ma_ft_frst_men_pacific_v",
        "total": "ma_ft_men_pacific_v",
        "awlevel": [7]
    },
    "2 or more Men Masters"  : {
        "comp": "c2morm", 
        "first": "ma_ft_frst_men_multi_v",
        "total": "ma_ft_men_multi_v",
        "awlevel": [7]
    },
    "Unknown Men Masters"  : {
        "comp": "cunknm", 
        "first": "ma_ft_frst_men_unk_v",
        "total": "ma_ft_men_unk_v",
        "awlevel": [7]
    },
    "Foreign Men Masters"  : {
        "comp": "cnralm", 
        "first": "ma_ft_frst_men_forgn_v",
        "total": "ma_ft_men_forgn_v",
        "awlevel": [7]
    },
    "White Women Masters": {
        "comp": "cwhitw", 
        "first": "ma_ft_frst_wmen_white_v",
        "total": "ma_ft_wmen_white_v",
        "awlevel": [7]
    },
    "Asian Women Masters": {
        "comp": "casiaw", 
        "first": "ma_ft_frst_wmen_asian_v",
        "total": "ma_ft_wmen_asian_v",
        "awlevel": [7]
    },
    "Black Women Masters": {
        "comp": "cbkaaw", 
        "first": "ma_ft_frst_wmen_black_v",
        "total": "ma_ft_wmen_black_v",
        "awlevel": [7]
    },
    "Hispanic Women Masters": {
        "comp": "chispw", 
        "first": "ma_ft_frst_wmen_hisp_v",
        "total": "ma_ft_wmen_hisp_v",
        "awlevel": [7]
    },
   "Native Hawaiian /Pacific islander Women Masters" : {
        "comp": "cnhpiw", 
        "first": "ma_ft_frst_wmen_pacific_v",
        "total": "ma_ft_wmen_pacific_v",
        "awlevel": [7]
    },
    "2 or more Women Masters"  : {
        "comp": "c2morw", 
        "first": "ma_ft_frst_wmen_multi_v",
        "total": "ma_ft_wmen_multi_v",
        "awlevel": [7]
    },
    "Unknown Women Masters"  : {
        "comp": "cunknw", 
        "first": "ma_ft_frst_wmen_unk_v",
        "total": "ma_ft_wmen_unk_v",
        "awlevel": [7]
    },
    "Foreign Women Masters"  : {
        "comp": "cnralw", 
        "first": "ma_ft_frst_wmen_forgn_v",
        "total": "ma_ft_wmen_forgn_v",
        "awlevel": [7]
    },
}
    
final_rows = []

# Make sure numeric fields are numeric
df = df.apply(pd.to_numeric, errors="ignore")

years = sorted(df["year"].unique())

# Precompute non-duplicated enrollment + first-year values
unique_first = df.drop_duplicates(subset=["unitid", "year"])[["unitid", "year"] + [col for col in df.columns if "_frst_" in col]]
unique_total = df.drop_duplicates(subset=["unitid", "year"])[["unitid", "year"] + [col for col in df.columns if "_tot_" in col]]


for cat_name, spec in categories.items():

    comp_var = spec["comp"]
    first_var = spec["first"]
    total_var = spec["total"]
    awlevels = spec.get("awlevel", None)

    # Loop through each year
    for year in years:

        # Filter current year for this category
        df_y = df[df["year"] == year]

        # Remove duplicates by UNITID before summing
        df_y_unique = df_y.drop_duplicates(subset=["unitid"])

        # TK INCLUDE FILTER TO REMOVE MASTERS ONLY INSTITUTIONS ( ONLY AWLEVEL 7 NO 9,17)

        # -------------------------------
        # FIRST YEAR AND ENROLLED
        # -------------------------------
        
        first_sum = (
            df_y_unique[first_var].sum(min_count=1)
            if first_var in df_y_unique.columns
            else np.nan
        )

        total_sum = (
            df_y_unique[total_var].sum(min_count=1)
            if total_var in df_y_unique.columns
            else np.nan
        )

        '''
        first_sum = df_y_unique[first_var].sum() if first_var in df_y_unique else 0
        total_sum = df_y_unique[total_var].sum() if total_var in df_y_unique else 0
        '''
        
        # -------------------------------
        # AWARDS
        # -------------------------------
       # -------------------------------
        phd_awarded = np.nan
        masters_awarded = np.nan

        if comp_var in df_y.columns:

            if awlevels and (9 in awlevels or 17 in awlevels):
                # This category tracks PhD completions
                phd_awarded = df_y[df_y["awlevel"].isin([9, 17])][comp_var].sum(min_count=1)

            if awlevels and 7 in awlevels:
                # This category tracks Masters completions
                masters_awarded = df_y[df_y["awlevel"] == 7][comp_var].sum(min_count=1)

        # -------------------------------
        # Determine degree type
        # -------------------------------
        if awlevels == [9, 17]:
            degree_type = "PhD"
        elif awlevels == [7]:
            degree_type = "Masters"
        else:
            degree_type = "All"

        # -------------------------------
        # SEX
        # -------------------------------
        if "_men_" in first_var:
            sex = "Men"
        elif "_wmen_" in first_var:
            sex = "Women"
        else:
            sex = "All"

        # -------------------------------
        # RACE
        # -------------------------------
        race_lookup = {
            "white": "White",
            "asian": "Asian",
            "black": "Black",
            "hisp": "Hispanic",
            "pacific": "Pacific Islander",
            "multi": "Two or More",
            "unk": "Unknown",
            "forgn": "Foreign"
        }
        race = "All"
        for key, value in race_lookup.items():
            if key in first_var:
                race = value


        # -------------------------------
        # Append row
        # -------------------------------
        final_rows.append({
            "year": year,
            "degree enrolled in": degree_type,
            "sex": sex,
            "race": race,
            "phd_awarded": phd_awarded,
            "masters_awarded": masters_awarded,
            "first_year": first_sum,
            "enrolled": total_sum,
        })

# -------------------------------
# Final DataFrame
# -------------------------------
final_df = pd.DataFrame(final_rows)

# -------------------------------
# Save to Excel
# -------------------------------
final_output = "/Users/co25936/Desktop/PER/IPEDS/PRC_National_dataset.xlsx"
final_df.to_excel(final_output, index=False)
print(f"Tidy dataset saved to: {final_output}")

