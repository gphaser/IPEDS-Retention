# Excel_Trimmer GSS
import os
import pandas as pd

folder_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/Untrimmed GSS/"  # Ensure path is correctly formatted

# Columns you want to keep
selected_columns = [
    "UNITID", "gss_code", 
    "ft_tot_all_races_v", "ft_tot_forgn_v", "ft_frst_tot_all_races_v", 
    "ft_men_all_races_v", "ft_wmen_all_races_v", "ft_frst_men_all_races_v", "ft_frst_wmen_all_races_v",
    "ma_ft_tot_all_races_v", "dr_ft_tot_all_races_v",
    "ma_ft_frst_tot_all_races_v", "dr_ft_frst_tot_all_races_v", 

    #Sex enrollment inital
    "dr_ft_frst_men_all_races_v", "dr_ft_frst_wmen_all_races_v",
    "ma_ft_frst_men_all_races_v", "ma_ft_frst_wmen_all_races_v",
    #Sex entrollment total
    "dr_ft_men_all_races_v", "dr_ft_wmen_all_races_v",
    "ma_ft_men_all_races_v", "ma_ft_wmen_all_races_v",
   

    # Racial/Ethnic breakdowns - Total Enrollment
    "ft_tot_black_v", "ft_tot_indian_v", "ft_tot_asian_v", "ft_tot_pacific_v",
    "ft_tot_white_v", "ft_tot_hisp_v", "ft_tot_multi_v", "ft_tot_unk_v", "ft_tot_forgn_v",
    
    # Racial/Ethnic breakdowns - First-Year Enrollment
    "ft_frst_tot_black_v", "ft_frst_tot_indian_v", "ft_frst_tot_asian_v", "ft_frst_tot_pacific_v",
    "ft_frst_tot_white_v", "ft_frst_tot_hisp_v", "ft_frst_tot_multi_v", "ft_frst_tot_unk_v", "ft_frst_tot_forgn_v"
]


for year in range(2000, 2024):
    filename = f"{folder_path}gss{year}_Code.xlsx"  # Construct full file path
    
    if os.path.exists(filename):  # Check if file exists
        df = pd.read_excel(filename)  # Read the Excel file

        # Determine which selected columns exist in the file
        existing_columns = [col for col in selected_columns if col in df.columns]
        missing_columns = [col for col in selected_columns if col not in df.columns]

        if missing_columns:
            print(f"Warning: Missing columns in {filename}: {missing_columns}")

        # Keep only existing columns
        df_filtered = df[existing_columns]

        # Filter for rows where 'gss_code' is 203 (only if 'gss_code' exists)
        if "gss_code" in df_filtered.columns:
            df_filtered = df_filtered[df_filtered["gss_code"] == 203]
        else:
            print(f"Skipping file {filename} because 'gss_code' column is missing.")
            continue

        # Add a new column for the year
        df_filtered['Year'] = year

        # Save the trimmed file
        output_filename = f"{folder_path}gss{year}_trimmed_file.xlsx"
        df_filtered.to_excel(output_filename, index=False)

        print(f"Saved: {output_filename}")
    else:
        print(f"File not found: {filename}, skipping.")



'''
#Excel_Trimmer GSS
import os
import pandas as pd

folder_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/"  # Ensure path is correctly formatted

for year in range(2000, 2024):
    filename = f"{folder_path}gss{year}_Code.xlsx"  # Construct full file path
    
    if os.path.exists(filename):  # Check if file exists
        df = pd.read_excel(filename)  # Read the Excel file
        
        # Select specific columns
        selected_columns = ["UNITID", "gss_code", "ft_tot_all_races_v", "ft_tot_forgn_v", "ft_frst_tot_all_races_v", 
                            "ft_men_all_races_v", "ft_wmen_all_races_v", "ft_frst_men_all_races_v", "ft_frst_wmen_all_races_v",
                             "ma_ft_men_all_races_v", "ma_ft_wmen_all_races_v", "ma_ft_tot_all_races_v", 
                             "dr_ft_men_all_races_v", "dr_ft_wmen_all_races_v","dr_ft_tot_all_races_v"], 
        df_filtered = df[selected_columns]  # Keep only selected columns

        # Filter for rows where 'gss_code' is 203
        df_filtered = df_filtered[df_filtered["gss_code"] == 203]

        # Add a new column for the year

        
        df_filtered['Year'] = year


        # Save the trimmed file
        output_filename = f"{folder_path}gss{year}_trimmed_file.xlsx"
        df_filtered.to_excel(output_filename, index=False)

        print(f"Saved: {output_filename}")
    else:
        print(f"File not found: {filename}, skipping.")



'''

