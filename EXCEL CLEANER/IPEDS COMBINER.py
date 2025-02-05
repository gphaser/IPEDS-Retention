import pandas as pd
import os

# Define the directory containing the Excel files
directory = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/Trimmed"  # Change this to your directory path

# Create an empty list to hold DataFrames
dataframes = []

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xlsx'):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Append the DataFrame to the list
        dataframes.append(df)

# Combine all DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Sort the combined DataFrame by the year column (assuming the year is in a column named 'Year')
combined_df = combined_df.sort_values(by='Year')

# Save the combined DataFrame to a new Excel file in the desired directory
combined_df.to_excel('/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/IPEDS_combined_file.xlsx', index=False)

print("All files have been combined and saved as 'IPEDS_combined_file.xlsx'.")
