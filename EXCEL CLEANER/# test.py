import pandas as pd
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

names = list(categories.keys())
print("Total keys:", len(names))
print("Unique keys:", len(set(names)))
dupes = [n for n in names if names.count(n) > 1]
print("Duplicates:", set(dupes))