# COMBINE THE GSS AND IPEDS COMBINED DATASETS INTO ONE
import pandas as pd
import os

# NEEED TO ADJUST SO KEEP DATA if GSS or IPEDS IS MISSING DATA AND CREATE ROWS FOR WHEN THERE IS NO DATA



# Define the directory containing the Excel files
directory1 = '/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS'  # Change this to your directory path
directory2 = '/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS'
directory3 = '/Users/co25936/Desktop/PER/IPEDS/'

# Specify the names of the Excel files you want to combine
file1 = 'GSS_combined_file.xlsx'  # Change this to your actual first file name
# file2 = 'IPEDS_WIDE_SAFE.xlsx' # Change this to your actual second file name
file2 = 'IPEDS_combined_file.xlsx'  # Change this to your actual second file name

# Construct the full file paths
file_path_1 = os.path.join(directory1, file1)
#file_path_2 = os.path.join(directory3, file2)
file_path_2 = os.path.join(directory2, file2)

# Read the first worksheet into a DataFrame
df1 = pd.read_excel(file_path_1, sheet_name='Sheet1')  # Change 'Sheet1' to your actual sheet name in your Excel file for file1
print("Columns in df1:", df1.columns.tolist())  # Debugging line

# Read the second worksheet into a DataFrame
df2 = pd.read_excel(file_path_2, sheet_name='Sheet1')  # Change 'Sheet1' to your actual sheet name in the Excel file for file2
print("Columns in df2:", df2.columns.tolist())  # Debugging line


# SORT THROUGH THE GSS add ft_tot_all_races_v+ft_tot_forgn_v+ ft_frst_tot_all_races_v if sum = 0 then replace values with NaN 
# Calculate the sum of the specified columns
sum_columns = df1[['ft_tot_all_races_v', 'ft_tot_forgn_v', 'ft_frst_tot_all_races_v']].sum(axis=1)

# Replace values with NaN if the sum equals 0 (this leaves the cell emptpy)
df1.loc[sum_columns == 0, ['ft_tot_all_races_v', 'ft_tot_forgn_v', 'ft_frst_tot_all_races_v']] = pd.NA

# Standardize column names before merging. Done by making them all lowercase 
df1.columns = df1.columns.str.lower()
df2.columns = df2.columns.str.lower()


# Merge the DataFrames on 'unitid' and 'year'

combined_df = pd.merge(df1, df2, on=['unitid', 'year'], how='outer')  # Use 'inner' if you only want matching unitids and year, and 'outer' for rows only in GSS or rows only in IPEDS

# Create full UNITID-Year grid to have blank rows for no data 
all_unitids = combined_df['unitid'].unique()
all_years = combined_df['year'].unique()

full_index = pd.MultiIndex.from_product(
    [all_unitids, all_years],
    names=['unitid', 'year']
)

full_df = pd.DataFrame(index=full_index).reset_index()

combined_df = pd.merge(full_df, combined_df, on=['unitid', 'year'], how='left')

# Check for duplicates and aggregate if necessary
# For example, if you want to keep the first occurrence of each combination:
# combined_df = combined_df.groupby(['unitid', 'year'], as_index=False).first()

# Check the columns of the combined DataFrame
print("Columns in combined_df:", combined_df.columns.tolist())  # Debugging line

# Save the combined DataFrame to a new Excel file
combined_df.to_excel(os.path.join(directory3, 'GSS_IPEDS_Combined_file.xlsx'), index=False)

print("The worksheets have been combined and saved as 'GSS_IPEDS_Combined_file.xlsx'.")




