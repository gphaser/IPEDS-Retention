# GSS COMBINER
import pandas as pd
import os

# Define the directory containing the Excel files
directory = "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/GSS Trimmed"  # Change this to your directory path

# Column pairs to combine
column_pairs = [
    ("ft_tot_unk_v", "ft_tot_unknown_v"),
    ("ft_frst_tot_unk_v", "ft_frst_tot_unknown_v"),
    ("ft_frst_men_unk_v", "ft_frst_men_unknown_v"),
    ("ft_frst_wmen_unk_v","ft_frst_wmen_unknown_v"),
    ("ft_men_unk_v","ft_men_unknown_v"),
    ("ft_wmen_unkn_v", "ft_wmen_unknown_v"),
    ("ft_tot__multi_v", "ft_tot__multi_non_hisp_v", ),
    ("ft_frst_tot_multi_v","ft_frst_tot_multi_non_hisp_v"),
    ("ft_frst_men_multi_v", "ft_frst_men_multi_non_hisp_v"),
    ("ft_frst_wmen_multi_v", "ft_frst_wmen_multi_non_hisp_v"),
    ("ft_men_multi_v", "ft_men_multi_non_hisp_v"),
    ("ft_wmen_multi_v", "ft_wmen_multi_non_hisp_v"),
]   

# Create an empty list to hold DataFrames
dataframes = []

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(directory, filename)
        df = pd.read_excel(file_path)

        # --- Combine specified column pairs ---
        for col1, col2 in column_pairs:
            if col1 in df.columns and col2 in df.columns:
                df[col1] = df[col1].fillna(0) + df[col2].fillna(0)
                df = df.drop(columns=[col2])  # drop the second column
            elif col2 in df.columns and col1 not in df.columns:
                # rename col2 to col1 for consistency
                df = df.rename(columns={col2: col1})

        dataframes.append(df)

# Combine all DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Sort the combined DataFrame by 'Year'
combined_df = combined_df.sort_values(by='Year')

# Save the combined DataFrame
output_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/GSS_combined_file.xlsx"
combined_df.to_excel(output_path, index=False)

print("All files have been combined and saved as 'GSS_combined_file.xlsx'.")





 # NEED TO COMBINE THE UNKNOW AND KNOWN COLUMNS
''' 
#GSS COMBINER
import pandas as pd
import os

# Define the directory containing the Excel files
directory = "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/GSS Trimmed"  # Change this to your directory path

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
combined_df.to_excel('/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/GSS_combined_file.xlsx', index=False)

print("All files have been combined and saved as 'GSS_combined_file.xlsx'.")
'''