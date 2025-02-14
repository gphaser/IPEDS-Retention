import pandas as pd

# Step 1: Read the Excel file
file_path = '/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_Combined_file.xlsx'
data = pd.read_excel(file_path)

# Step 2: Filter the data for AWLEVEL = 17
filtered_data = data[data['AWLEVEL'] == 17]

# Step 3: Define the range of years
years = range(2000, 2024)  # 2023 is inclusive

# Step 4: Group by UNITID and check for the presence of all years
def has_all_years(group):
    return set(years).issubset(set(group['Year']))

# Filter the groups
valid_unitids = filtered_data.groupby('UNITID').filter(has_all_years)['UNITID'].unique()

# Step 5: Keep only the valid UNITIDs
final_data = filtered_data[filtered_data['UNITID'].isin(valid_unitids)]

# Step 6: Sort the final data
final_data = final_data.sort_values(by=['UNITID', 'AWLEVEL', 'Year'])

# Optional: Save the final data to a new Excel file
final_data.to_excel('/Users/co25936/Desktop/PER/IPEDS/Filtered_GSS_IPEDS_Combined_file.xlsx', index=False)

print("Data has been filtered and saved successfully.")
