import pandas as pd
import os

# Define the directory containing the Excel files
directory = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/Trimmed"

# Create an empty list to hold DataFrames
dataframes = []

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(directory, filename)
        df = pd.read_excel(file_path)

        # --- Standardize columns: Fill CTOTALM and CTOTALW if missing ---
        if 'CTOTALM' not in df.columns:
            if 'CRACE15' in df.columns:
                df['CTOTALM'] = df['CRACE15']
            elif 'crace15' in df.columns:
                df['CTOTALM'] = df['crace15']
        
        if 'CTOTALW' not in df.columns:
            if 'CRACE16' in df.columns:
                df['CTOTALW'] = df['CRACE16']
            elif 'crace16' in df.columns:
                df['CTOTALW'] = df['crace16']

        # Optional: drop the redundant columns
        df = df.drop(columns=[col for col in ['CRACE15', 'crace15', 'CRACE16', 'crace16'] if col in df.columns])

        # Standardize doctoral award level from 9 to 17 (pre-2008)
        df['AWLEVEL'] = df['AWLEVEL'].replace(9, 17)

        # Append to list
        dataframes.append(df)

# Combine all DataFrames
combined_df = pd.concat(dataframes, ignore_index=True)

# Sort by Year
combined_df = combined_df.sort_values(by='Year')

# Save combined file
combined_df.to_excel('/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/IPEDS_combined_file.xlsx', index=False)

print("All files have been combined and saved as 'IPEDS_combined_file.xlsx'.")



'''
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
        
        # Change AWLEVEL from 9 to 17 this is to make pre 2008 doctoral degrees unified
        df['AWLEVEL'] = df['AWLEVEL'].replace(9, 17)


        
        # Append the DataFrame to the list
        dataframes.append(df)

# Combine all DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Sort the combined DataFrame by the year column (assuming the year is in a column named 'Year')
combined_df = combined_df.sort_values(by='Year')

# Save the combined DataFrame to a new Excel file in the desired directory
combined_df.to_excel('/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/IPEDS_combined_file.xlsx', index=False)

print("All files have been combined and saved as 'IPEDS_combined_file.xlsx'.")
'''