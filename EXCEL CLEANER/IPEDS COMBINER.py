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

        # --- Standardize and combine other race columns ---
        # Create new columns and populate from either uppercase or lowercase versions
        if 'CRACE17' in df.columns or 'crace17' in df.columns:
            df['CRACE17_STD'] = df.get('CRACE17', df.get('crace17', pd.NA))
        if 'CRACE18' in df.columns or 'crace18' in df.columns:
            df['CRACE18_STD'] = df.get('CRACE18', df.get('crace18', pd.NA))
        if 'CRACE19' in df.columns or 'crace19' in df.columns:
            df['CRACE19_STD'] = df.get('CRACE19', df.get('crace19', pd.NA))
        if 'CRACE20' in df.columns or 'crace20' in df.columns:
            df['CRACE20_STD'] = df.get('CRACE20', df.get('crace20', pd.NA))
        if 'CRACE21' in df.columns or 'crace21' in df.columns:
            df['CRACE21_STD'] = df.get('CRACE21', df.get('crace21', pd.NA))
        if 'CRACE22' in df.columns or 'crace22' in df.columns:
            df['CRACE22_STD'] = df.get('CRACE22', df.get('crace22', pd.NA))

        # Drop redundant original columns
        columns_to_drop = ['CRACE15', 'crace15', 'CRACE16', 'crace16',
                           'CRACE17', 'crace17', 'CRACE18', 'crace18',
                           'CRACE19', 'crace19', 'CRACE20', 'crace20',
                           'CRACE21', 'crace21', 'CRACE22', 'crace22']
        df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

        # Standardize doctoral award level from 9 to 17 (pre-2010)
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

# --- Create trimmed version with only AWLEVEL = 17 ---
trimmed_df = combined_df[combined_df["AWLEVEL"] == 17].copy()

trimmed_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/IPEDS_combined_file_trimmed_AWLEVEL17.xlsx"
trimmed_df.to_excel(trimmed_path, index=False)
print(f"Trimmed file (AWLEVEL=17 only) saved as: {trimmed_path}")
