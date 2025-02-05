#Excel_Trimmer GSS
import os
import pandas as pd

folder_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/"  # Ensure path is correctly formatted

for year in range(2000, 2024):
    filename = f"{folder_path}gss{year}_Code.xlsx"  # Construct full file path
    
    if os.path.exists(filename):  # Check if file exists
        df = pd.read_excel(filename)  # Read the Excel file
        
        # Select specific columns
        selected_columns = ["UNITID", "gss_code", "ft_tot_all_races_v", "ft_tot_forgn_v", "ft_frst_tot_all_races_v"]
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





