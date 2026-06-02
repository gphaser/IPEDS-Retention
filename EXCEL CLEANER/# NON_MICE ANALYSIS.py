# OK Code working but the numbers in the results need to be checked random check on 2mort 2017 true, hispanic women 2 true
# NON_MICE ANALYSIS
# Goal use the file "/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_COMBINED_WIDE_trimmed.xlsx"
# to preform the calculations for PCR and RR 
#PCR(year) = [sum of all comp(year+5) + comp(year+6) + comp(year+7)] / 
#                [sum of all first(year-1) + first(year) + first(year+1)]
    
#Retention(year) = [sum of all total(year) + comp(year) - first(year)] / 
#                     [sum of all total(year-1)]
# need to have breakdown for each of the different sex and race groups
''' groups are as follows
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
}
'''

import pandas as pd
import numpy as np
from pathlib import Path

# ==============================================================
# STEP 1: Load Data
# ==============================================================

input_path = "/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_COMBINED_WIDE_trimmed.xlsx"
output_dir = "/Users/co25936/Desktop/PER/IPEDS/Non_Mice_Analysis"

Path(output_dir).mkdir(parents=True, exist_ok=True)

# Load Excel file
# If your file has multiple sheets and you need a specific one,
# add sheet_name='SheetName'
df = pd.read_excel(input_path)

# ==============================================================
# STEP 2: Define Categories
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
    "Doctor": {
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
    "Native Hawaiian /Pacific islander": {
        "comp": "cnhpit",
        "first": "ft_frst_tot_pacific_v",
        "total": "ft_tot_pacific_v",
        "awlevel": [7, 9, 17]
    },
    "2 or more": {
        "comp": "c2mort",
        "first": "ft_frst_tot_multi_v",
        "total": "ft_tot_multi_v",
        "awlevel": [7, 9, 17]
    },
    "Unknown": {
        "comp": "cunknt",
        "first": "ft_frst_tot_unk_v",
        "total": "ft_tot_unk_v",
        "awlevel": [7, 9, 17]
    },
    "Foreign": {
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
    "Native Hawaiian /Pacific islander Men": {
        "comp": "cnhpim",
        "first": "ft_frst_men_pacific_v",
        "total": "ft_men_pacific_v",
        "awlevel": [7, 9, 17]
    },
    "2 or more Men": {
        "comp": "c2morm",
        "first": "ft_frst_men_multi_v",
        "total": "ft_men_multi_v",
        "awlevel": [7, 9, 17]
    },
    "Unknown Men": {
        "comp": "cunknm",
        "first": "ft_frst_men_unk_v",
        "total": "ft_men_unk_v",
        "awlevel": [7, 9, 17]
    },
    "Foreign Men": {
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
    "Native Hawaiian /Pacific islander Women": {
        "comp": "cnhpiw",
        "first": "ft_frst_wmen_pacific_v",
        "total": "ft_wmen_pacific_v",
        "awlevel": [7, 9, 17]
    },
    "2 or more Women": {
        "comp": "c2morw",
        "first": "ft_frst_wmen_multi_v",
        "total": "ft_wmen_multi_v",
        "awlevel": [7, 9, 17]
    },
    "Unknown Women": {
        "comp": "cunknw",
        "first": "ft_frst_wmen_unk_v",
        "total": "ft_wmen_unk_v",
        "awlevel": [7, 9, 17]
    },
    "Foreign Women": {
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
}

# ==============================================================
# STEP 3: Clean Data
# ==============================================================

# Standardize column names
# Removes accidental spaces from Excel headers
df.columns = df.columns.str.strip()

# Convert numeric columns safely
for col in df.columns:
    if col not in ["unitid"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Replace missing values with 0 for calculations
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(0)

# ==============================================================
# STEP 4: Validate Required Columns
# ==============================================================

required_base_cols = ["awlevel"]

missing_base = [c for c in required_base_cols if c not in df.columns]

if missing_base:
    raise ValueError(f"Missing required columns: {missing_base}")

# ==============================================================
# STEP 5: PCR + Retention Calculations
# ==============================================================

results = []

# Detect all available years from column suffixes
# Example column: ft_tot_all_races_v_2013
available_years = sorted({
    int(col.split("_")[-1])
    for col in df.columns
    if col.split("_")[-1].isdigit()
})

print(f"Detected years: {available_years}")

for category_name, config in categories.items():

    comp_base = config["comp"]
    first_base = config["first"]
    total_base = config["total"]
    allowed_awlevels = config["awlevel"]

    # Filter by award levels
    temp = df[df["awlevel"].isin(allowed_awlevels)].copy()

    for yr in available_years:

        # ======================================================
        # Build Dynamic Column Names
        # ======================================================

        comp_cols = [
            f"{comp_base}_{yr + 5}",
            f"{comp_base}_{yr + 6}",
            f"{comp_base}_{yr + 7}"
        ]

        first_cols = [
            f"{first_base}_{yr - 1}",
            f"{first_base}_{yr}",
            f"{first_base}_{yr + 1}"
        ]

        total_current_col = f"{total_base}_{yr}"
        total_prev_col = f"{total_base}_{yr - 1}"

        comp_current_col = f"{comp_base}_{yr}"
        first_current_col = f"{first_base}_{yr}"
        
# ==============================================================
# STEP 5: PCR + Retention Calculations
# ==============================================================

results = []

# Detect all available years from column suffixes
# Example column: ft_tot_all_races_v_2013
available_years = sorted({
    int(col.split("_")[-1])
    for col in df.columns
    if col.split("_")[-1].isdigit()
})

print(f"Detected years: {available_years}")

for category_name, config in categories.items():

    comp_base = config["comp"]
    first_base = config["first"]
    total_base = config["total"]
    allowed_awlevels = config["awlevel"]

    # Filter by award levels
    temp = df[df["awlevel"].isin(allowed_awlevels)].copy()

    for yr in available_years:

        # ======================================================
        # Build Dynamic Column Names
        # ======================================================

        comp_cols = [
            f"{comp_base}_{yr + 5}",
            f"{comp_base}_{yr + 6}",
            f"{comp_base}_{yr + 7}"
        ]

        first_cols = [
            f"{first_base}_{yr - 1}",
            f"{first_base}_{yr}",
            f"{first_base}_{yr + 1}"
        ]

        total_current_col = f"{total_base}_{yr}"
        total_prev_col = f"{total_base}_{yr - 1}"

        comp_current_col = f"{comp_base}_{yr}"
        first_current_col = f"{first_base}_{yr}"

        # ======================================================
        # PCR Calculation
        # ======================================================

        pcr = np.nan
        comp_sum = np.nan
        first_sum = np.nan

        pcr_needed = comp_cols + first_cols

        missing_pcr = [c for c in pcr_needed if c not in temp.columns]

        if not missing_pcr:

            comp_sum = sum(
                temp[col].fillna(0).sum()
                for col in comp_cols
            )

            first_sum = sum(
                temp[col].fillna(0).sum()
                for col in first_cols
            )

            if first_sum != 0:
                pcr = comp_sum / first_sum

        print("\nDEBUG YEAR:", yr)
        print("Looking for:", total_prev_col)

        if total_prev_col in temp.columns:
            print("Column exists")
            print(temp[total_prev_col].head(10))
            print("NaN count:", temp[total_prev_col].isna().sum())
            print("Raw sum (no fill):", temp[total_prev_col].sum())
        else:
            print("MISSING COLUMN:", total_prev_col)

        # ======================================================
        # Retention Calculation
        # ======================================================

        retention = np.nan
        numerator = np.nan
        denominator = np.nan

        retention_needed = [
            total_current_col,
            total_prev_col,
            comp_current_col,
            first_current_col
        ]

        missing_retention = [
            c for c in retention_needed
            if c not in temp.columns
        ]

        if not missing_retention:

            numerator = (
                temp[total_current_col].fillna(0).sum()
                + temp[comp_current_col].fillna(0).sum()
                - temp[first_current_col].fillna(0).sum()
            )

            denominator = temp[total_prev_col].fillna(0).sum()

            if denominator != 0:
                retention = numerator / denominator

        # ======================================================
        # Save Results
        # ======================================================

        results.append({
            "Category": category_name,
            "Year": yr,
            "PCR": pcr,
            "Retention": retention,
            "PCR_Numerator_Comp": comp_sum,
            "PCR_Denominator_First": first_sum,
            "Retention_Numerator": numerator,
            "Retention_Denominator": denominator
        })


# ==============================================================
# STEP 6: Create Results DataFrame
# ==============================================================

results_df = pd.DataFrame(results)

# Optional formatting
results_df = results_df.sort_values(["Category", "Year"])

# ==============================================================
# STEP 7: Save Outputs
# ==============================================================

excel_output = Path(output_dir) / "PCR_Retention_Results.xlsx"
results_df.to_excel(excel_output, index=False)


print("PCR + Retention calculations complete")
print(f"Excel saved to: {excel_output}")

# ==============================================================
# STEP 7.5: Make Graphs
# ==============================================================

import matplotlib.pyplot as plt
from pathlib import Path
import re

output_dir = Path("/Users/co25936/Desktop/PER/IPEDS/Non_Mice_Analysis")
output_dir.mkdir(parents=True, exist_ok=True)

def clean_filename(name):
    return re.sub(r'[^\w\-_. ]', '_', name)

for cat in results_df["Category"].unique():

    print("PLOTTING:", cat)

    cat_df = results_df[results_df["Category"] == cat].sort_values("Year")

    if cat_df.empty:
        continue

    safe_cat = clean_filename(cat)

    # ======================
    # PCR SCATTER
    # ======================
    plt.figure()
    plt.scatter(cat_df["Year"], cat_df["PCR"])
    plt.title(f"PCR Over Time - {cat}")
    plt.xlabel("Year")
    plt.ylabel("PCR")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(output_dir / f"PCR_{safe_cat}.png", dpi=300)
    plt.close()

    # ======================
    # RETENTION SCATTER
    # ======================
    plt.figure()
    plt.scatter(cat_df["Year"], cat_df["Retention"])
    plt.title(f"Retention Over Time - {cat}")
    plt.xlabel("Year")
    plt.ylabel("Retention")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(output_dir / f"Retention_{safe_cat}.png", dpi=300)
    plt.close()

# Also want unified y-axis and sex-groups so 
total_groups = [
    "Total",
    "White",
    "Asian",
    "Black",
    "Hispanic",
    "Native Hawaiian /Pacific islander",
    "2 or more",
    "Unknown",
    "Foreign"
]

men_groups = [
    "Men",
    "White Men",
    "Asian Men",
    "Black Men",
    "Hispanic Men",
    "Native Hawaiian /Pacific islander Men",
    "2 or more Men",
    "Unknown Men",
    "Foreign Men"
]

women_groups = [
    "Women",
    "White Women",
    "Asian Women",
    "Black Women",
    "Hispanic Women",
    "Native Hawaiian /Pacific islander Women",
    "2 or more Women",
    "Unknown Women",
    "Foreign Women"
]

doctor_groups = [
    "Doctor",
    "White Doctor",
    "Asian Doctor",
    "Black Doctor",
    "Hispanic Doctor",
    "Native Hawaiian /Pacific islander Doctor",
    "2 or more Doctor",
    "Unknown Doctor",
    "Foreign Doctor"
]
men_doctor_groups = [
    "Men Doctor",
    "White Men Doctor",
    "Asian Men Doctor",
    "Black Men Doctor",
    "Hispanic Men Doctor",
    "Native Hawaiian /Pacific islander Men Doctor",
    "2 or more Men Doctor",
    "Unknown Men Doctor",
    "Foreign Men Doctor"
]

women_doctor_groups = [
    "Women Doctor",
    "White Women Doctor",
    "Asian Women Doctor",
    "Black Women Doctor",
    "Hispanic Women Doctor",
    "Native Hawaiian /Pacific islander Women Doctor",
    "2 or more Women Doctor",
    "Unknown Women Doctor",
    "Foreign Women Doctor"
]

pcr_min = results_df["PCR"].dropna().min() - 0.1
rr_min = results_df["Retention"].dropna().min() - 0.1

plot_groups = (
    total_groups +
    men_groups +
    women_groups
)

plot_df = results_df[
    results_df["Category"].isin(plot_groups)
]

pcr_max = plot_df["PCR"].dropna().max()
rr_max = plot_df["Retention"].dropna().max()


doctor_plot_groups = (
    doctor_groups +
    men_doctor_groups +
    women_doctor_groups
)

doctor_df = results_df[
    results_df["Category"].isin(doctor_plot_groups)
]

doctor_rr_min = max(
    0,
    doctor_df["Retention"].dropna().min() - 0.1
)

doctor_rr_max = (
    doctor_df["Retention"].dropna().max() + 0.1
)



# this is a function that will make the graphs that we call below
def make_graph(groups, value_col, title, filename, ymin, ymax):

    plt.figure(figsize=(12,8))

    for group in groups:

        temp = (
            results_df[
                results_df["Category"] == group
            ]
            .sort_values("Year")
        )

        if temp.empty:
            continue

        plt.plot(
            temp["Year"],
            temp[value_col],
            marker="o",
            label=group
        )

    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel(value_col)

    # SAME y-axis for every graph
    plt.ylim(ymin, ymax)

    plt.grid(True)

    plt.legend(
        bbox_to_anchor=(1.05, 1),
        loc="upper left"
    )

    plt.tight_layout()

    plt.savefig(
        output_dir / filename,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

# PCR graphs all use same PCR scale
make_graph(
    total_groups,
    "PCR",
    "PCR - All Students",
    "PCR_Total_All.png",
    pcr_min,
    pcr_max
)

make_graph(
    men_groups,
    "PCR",
    "PCR - Men",
    "PCR_Men_All.png",
    pcr_min,
    pcr_max
)

make_graph(
    women_groups,
    "PCR",
    "PCR - Women",
    "PCR_Women_All.png",
    pcr_min,
    pcr_max
)

# RR graphs all use same RR scale
make_graph(
    total_groups,
    "Retention Rate",
    "RR - All Students",
    "RR_Total_All.png",
    rr_min,
    rr_max
)

make_graph(
    men_groups,
    "Retention Rate",
    "RR - Men",
    "RR_Men_All.png",
    rr_min,
    rr_max
)

make_graph(
    women_groups,
    "Retention Rate",
    "RR - Women",
    "RR_Women_All.png",
    rr_min,
    rr_max
)

make_graph(
    doctor_groups,
    "Retention Rate",
    "RR - Doctoral Students",
    "RR_Doctor_All.png",
    doctor_rr_min,
    doctor_rr_max
)

make_graph(
    men_doctor_groups,
    "Retention Rate",
    "RR - Men Doctoral Students",
    "RR_Doctor_Men.png",
    doctor_rr_min,
    doctor_rr_max
)

make_graph(
    women_doctor_groups,
    "Retention Rate",
    "RR - Women Doctoral Students",
    "RR_Doctor_Women.png",
    doctor_rr_min,
    doctor_rr_max
)

# ==============================================================
# STEP 8: Optional Summary Tables
# ==============================================================

# Wide-format PCR table
pcr_table = results_df.pivot(
    index="Year",
    columns="Category",
    values="PCR"
)

# Wide-format Retention table
retention_table = results_df.pivot(
    index="Year",
    columns="Category",
    values="Retention"
)

# Save summary tables
summary_output = Path(output_dir) / "PCR_Retention_Summary.xlsx"

with pd.ExcelWriter(summary_output, engine="openpyxl") as writer:
    results_df.to_excel(writer, sheet_name="Long_Format", index=False)
    pcr_table.to_excel(writer, sheet_name="PCR_Wide")
    retention_table.to_excel(writer, sheet_name="Retention_Wide")

print(f"Summary workbook saved to: {summary_output}")


## Notes

# The script automatically skips categories whose columns do not exist in the dataset.
# Missing numeric values are converted to 0.
# Award level filtering is handled separately for each category.


