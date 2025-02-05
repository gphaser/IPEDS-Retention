#IPEDS_Excel_Trimmer
import os
import pandas as pd

folder_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/"  # Ensure path is correctly formatted

for year in range(2023, 2024):
    filename = f"{folder_path}c{year}_a.xlsx"  # Construct full file path
    
    if os.path.exists(filename):  # Check if file exists
        df = pd.read_excel(filename)  # Read the Excel file
        
        # Select specific columns
        selected_columns = ["UNITID", "CIPCODE", "CTOTALT", "AWLEVEL"]
        df_filtered = df[selected_columns]  # Keep only selected columns

        # Filter for rows where 'CIP Code' is 40.0801 and Award Level is 7 (Masters) or 17 (PHD)

        df_filtered = df_filtered[(df_filtered["CIPCODE"] == 40.0801) & (df_filtered["AWLEVEL"].isin([7, 17]))]

        # Add a new column for the year
        df_filtered['Year'] = year


        # Save the trimmed file
        output_filename = f"{folder_path}c{year}_trimmed_file.xlsx"
        df_filtered.to_excel(output_filename, index=False)

        print(f"Saved: {output_filename}")
    else:
        print(f"File not found: {filename}, skipping.")
