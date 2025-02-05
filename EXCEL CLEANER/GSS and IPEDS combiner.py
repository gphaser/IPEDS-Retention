# COMBINE THE GSS AND IPEDS COMBINED DATASETS INTO ONE
import pandas as pd
import os

# Define the directory containing the Excel files
directory1 = '/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS'  # Change this to your directory path
directory2 = '/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS'
directory3 = '/Users/co25936/Desktop/PER/IPEDS/'

# Specify the names of the Excel files you want to combine
file1 = 'GSS_combined_file.xlsx'  # Change this to your actual first file name
file2 = 'IPEDS_combined_file.xlsx'  # Change this to your actual second file name

# Construct the full file paths
file_path_1 = os.path.join(directory1, file1)
file_path_2 = os.path.join(directory2, file2)

# Read the first worksheet into a DataFrame
df1 = pd.read_excel(file_path_1, sheet_name='Sheet1')  # Change 'Sheet1' to your actual sheet name
print("Columns in df1:", df1.columns.tolist())  # Debugging line

# Read the second worksheet into a DataFrame
df2 = pd.read_excel(file_path_2, sheet_name='Sheet1')  # Change 'Sheet1' to your actual sheet name
print("Columns in df2:", df2.columns.tolist())  # Debugging line

# Merge the DataFrames on 'UNITID' (you can specify how='outer' or how='inner' based on your needs)
combined_df = pd.merge(df1, df2, on='UNITID', how='outer')  # Use 'inner' if you only want matching UNITIDs

# Check the columns of the combined DataFrame
print("Columns in combined_df:", combined_df.columns.tolist())  # Debugging line

# Handle duplicate Year columns
if 'Year_x' in combined_df.columns and 'Year_y' in combined_df.columns:
    # If you want to keep Year_x or Year_y, you can drop the other
    combined_df['Year'] = combined_df['Year_x'].combine_first(combined_df['Year_y'])
    combined_df.drop(columns=['Year_x', 'Year_y'], inplace=True)

# Sort the combined DataFrame by 'Year' and 'UNITID'
combined_df = combined_df.sort_values(by=['Year', 'UNITID'])

# Save the combined DataFrame to a new Excel file
combined_df.to_excel(os.path.join(directory3, 'GSS_IPEDS_Combined_file.xlsx'), index=False)

print("The worksheets have been combined and saved as 'GSS_IPEDS_Combined_file.xlsx'.")

