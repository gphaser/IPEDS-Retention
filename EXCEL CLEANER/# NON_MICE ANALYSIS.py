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
            "Retention_Denominator": denominator,
            "Comp_Total": temp[comp_current_col].sum() if comp_current_col in temp.columns else np.nan,
            "First_Total": temp[first_current_col].sum() if first_current_col in temp.columns else np.nan,
            "Total_Current": temp[total_current_col].sum() if total_current_col in temp.columns else np.nan
        })


# ==============================================================
# STEP 6: Create Results DataFrame
# ==============================================================

results_df = pd.DataFrame(results)

# TEMP DEBUG
print(results_df[results_df["Category"] == "Masters"].to_string())

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

master_groups = [
    "Masters",
    "White Masters",
    "Asian Masters",
    "Black Masters",
    "Hispanic Masters",
    "Native Hawaiian /Pacific islander Masters",
    "2 or more Masters",
    "Unknown Masters",
    "Foreign Masters"
]
men_master_groups = [
    "Men Masters",
    "White Men Masters",
    "Asian Men Masters",
    "Black Men Masters",
    "Hispanic Men Masters",
    "Native Hawaiian /Pacific islander Men Masters",
    "2 or more Men Masters",
    "Unknown Men Masters",
    "Foreign Men Masters"
]

women_master_groups = [
    "Women Masters",
    "White Women Masters",
    "Asian Women Masters",
    "Black Women Masters",
    "Hispanic Women Masters",
    "Native Hawaiian /Pacific islander Women Masters",
    "2 or more Women Masters",
    "Unknown Women Masters",
    "Foreign Women Masters"
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

master_plot_groups = (
    master_groups +
    men_master_groups +
    women_master_groups
)

master_df = results_df[
    results_df["Category"].isin(master_plot_groups)
]

master_rr_min = max(
    0,
    master_df["Retention"].dropna().min() - 0.1
)

master_rr_max = (
    master_df["Retention"].dropna().max() + 0.1
)


# this is a function that will make the graphs that we call below with LOG scale dots for pop size

def make_graph(groups, value_col, title, filename, ymin, ymax, size_col="Total_Current"):

    plt.figure(figsize=(12,8))

    # First pass: figure out global min/max of the size column across the groups being plotted,
    # so marker scaling is consistent across this graph's group.
    all_sizes = []
    for group in groups:
        temp = results_df[results_df["Category"] == group]
        if not temp.empty and size_col in temp.columns:
            all_sizes.extend(temp[size_col].dropna().tolist())

    if all_sizes:
        log_sizes_global = np.log(np.array(all_sizes) + 1)  # +1 avoids log(0)
        size_log_min = log_sizes_global.min()
        size_log_max = log_sizes_global.max()
    else:
        size_log_min, size_log_max = 0, 1

    # tweak these to control how small/large the dots get (start 30/400)
    MIN_MARKER_SIZE = 10
    MAX_MARKER_SIZE = 500

    for group in groups:

        temp = (
            results_df[
                results_df["Category"] == group
            ]
            .sort_values("Year")
        )

        if temp.empty:
            continue

        # draw the connecting line without markers
        line, = plt.plot(
            temp["Year"],
            temp[value_col],
            marker=None,
            label=group
        )

        # compute log-scaled marker sizes for this group's points
        if size_col in temp.columns:
            log_sizes = np.log(temp[size_col].fillna(0) + 1)
            if size_log_max > size_log_min:
                norm = (log_sizes - size_log_min) / (size_log_max - size_log_min)
            else:
                norm = np.zeros(len(log_sizes))
            marker_sizes = MIN_MARKER_SIZE + norm * (MAX_MARKER_SIZE - MIN_MARKER_SIZE)
        else:
            marker_sizes = MIN_MARKER_SIZE

        # overlay scatter points, sized logarithmically, same color as the line
        plt.scatter(
            temp["Year"],
            temp[value_col],
            s=marker_sizes,
            color=line.get_color(),
            zorder=3
        )

    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel(value_col)

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

''' Old version that worked but we want to add LOG-scale points
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
'''

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
    "Retention",
    "RR - All Students",
    "RR_Total_All.png",
    rr_min,
    rr_max
)

make_graph(
    men_groups,
    "Retention",
    "RR - Men",
    "RR_Men_All.png",
    rr_min,
    rr_max
)

make_graph(
    women_groups,
    "Retention",
    "RR - Women",
    "RR_Women_All.png",
    rr_min,
    rr_max
)

make_graph(
    doctor_groups,
    "Retention",
    "RR - Doctoral Students",
    "RR_Doctor_All.png",
    doctor_rr_min,
    doctor_rr_max
)

make_graph(
    men_doctor_groups,
    "Retention",
    "RR - Men Doctoral Students",
    "RR_Doctor_Men.png",
    doctor_rr_min,
    doctor_rr_max
)

make_graph(
    women_doctor_groups,
    "Retention",
    "RR - Women Doctoral Students",
    "RR_Doctor_Women.png",
    doctor_rr_min,
    doctor_rr_max
)

make_graph(
    master_groups,
    "Retention",
    "RR - Masters Students",
    "RR_Master_All.png",
    master_rr_min,
    master_rr_max
)

make_graph(
    men_master_groups,
    "Retention",
    "RR - Men Masters Students",
    "RR_Master_Men.png",
    master_rr_min,
    master_rr_max
)

make_graph(
    women_master_groups,
    "Retention",
    "RR - Women Masters Students",
    "RR_Master_Women.png",
    master_rr_min,
    master_rr_max
)

# ==============================================================
# STEP 8: Summary Tables
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

# Wide-format totals tables
comp_total_table = results_df.pivot(
    index="Year",
    columns="Category",
    values="Comp_Total"
)

first_total_table = results_df.pivot(
    index="Year",
    columns="Category",
    values="First_Total"
)

# ==============================================================
# PhD vs Masters First-Time Student Fraction
# ==============================================================

def strip_level_suffix(cat_name, suffix):
    if cat_name == suffix.strip():
        return "Total"
    if cat_name.endswith(" " + suffix):
        return cat_name[: -(len(suffix) + 1)]
    return None

doctor_rows = results_df[
    results_df["Category"].str.endswith("Doctor") | (results_df["Category"] == "Doctor")
].copy()
doctor_rows["Group"] = doctor_rows["Category"].apply(lambda c: strip_level_suffix(c, "Doctor"))

masters_rows = results_df[
    results_df["Category"].str.endswith("Masters") | (results_df["Category"] == "Masters")
].copy()
masters_rows["Group"] = masters_rows["Category"].apply(lambda c: strip_level_suffix(c, "Masters"))

phd_vs_masters = pd.merge(
    doctor_rows[["Group", "Year", "First_Total"]].rename(columns={"First_Total": "PhD_First"}),
    masters_rows[["Group", "Year", "First_Total"]].rename(columns={"First_Total": "Masters_First"}),
    on=["Group", "Year"],
    how="outer"
)

phd_vs_masters["PhD_Fraction"] = phd_vs_masters["PhD_First"] / (
    phd_vs_masters["PhD_First"] + phd_vs_masters["Masters_First"]
)

phd_vs_masters = phd_vs_masters.sort_values(["Group", "Year"])

# ==============================================================
# Save Everything
# ==============================================================

summary_output = Path(output_dir) / "PCR_Retention_Summary.xlsx"

with pd.ExcelWriter(summary_output, engine="openpyxl") as writer:
    results_df.to_excel(writer, sheet_name="Long_Format", index=False)
    pcr_table.to_excel(writer, sheet_name="PCR_Wide")
    retention_table.to_excel(writer, sheet_name="Retention_Wide")
    comp_total_table.to_excel(writer, sheet_name="Comp_Total_Wide")
    first_total_table.to_excel(writer, sheet_name="First_Total_Wide")
    phd_vs_masters.to_excel(writer, sheet_name="PhD_vs_Masters_Frac", index=False)

print(f"Summary workbook saved to: {summary_output}")

## Notes

# The script automatically skips categories whose columns do not exist in the dataset.
# Missing numeric values are converted to 0.
# Award level filtering is handled separately for each category.
# NEED TO INCLUDE Native american values ma_ft_tot_indian_v_* (TRY TO FIGURE OUT WHY EXCLUDEDS)


