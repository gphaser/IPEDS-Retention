# CSV TO XLSX converter
import pandas as pd
import os


# Specify the input CSV file and the output XLSX file
folder_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/"  # Ensure path is correctly formatted

for year in range(2023, 2024):
    filename = f"{folder_path}c{year}_a"  # Construct full file path
    input_csv_file = f'{filename}.csv'  # Use f-string for input file path
    output_xlsx_file = f'{filename}.xlsx'  # Use f-string for output file path
    # Read the CSV file
    data = pd.read_csv(input_csv_file)

    # Write the data to an XLSX file
    data.to_excel(output_xlsx_file, index=False)

    print(f"Converted '{input_csv_file}' to '{output_xlsx_file}' successfully.")    

