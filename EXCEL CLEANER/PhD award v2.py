import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Filepath for the original Excel file
file_path = '/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_Combined_file.xlsx'
df = pd.read_excel(file_path)

# Remove rows with missing values in 'ft_tot_all_races_v'
df_trimmed = df.dropna(subset=['ft_tot_all_races_v'])

# Filter by AWLEVEL = 17 and specified UNITIDs
unitid_list = [
    100663, 100751, 104151, 110404, 134130, 139658, 139755, 144005,
    145600, 147703, 151111, 152080, 243780, 153603, 153658, 172644,
    172699, 174066, 176080, 178411, 178396, 178420, 179867, 180461,
    181464, 182670, 183044, 186380, 186867, 186867, 196468, 190415,
    194824, 196130, 196097, 199102, 199120, 199847, 200280, 201885,
    203517, 204857, 206084, 207388, 209542, 209551, 209807, 211273,
    211440, 213543, 214777, 215293, 227757, 230728, 232982, 233921,
    234076, 231624, 236948, 240444
]

# Filter by AWLEVEL and UNITID
filtered_df = df_trimmed[df_trimmed['AWLEVEL'] == 17][['UNITID', 'Year', 'AWLEVEL', 'ft_tot_all_races_v', 'ft_frst_tot_all_races_v', 'CTOTALT']]
filtered_df = filtered_df[filtered_df['UNITID'].isin(unitid_list)]

# Create a complete DataFrame with all missing years filled
all_years = pd.MultiIndex.from_product([unitid_list, range(2000, 2024)], names=['UNITID', 'Year']).to_frame(index=False)
complete_df = all_years.merge(filtered_df, how='left', on=['UNITID', 'Year'])

# Fill missing AWLEVEL with 17
complete_df['AWLEVEL'] = complete_df['AWLEVEL'].fillna(17)

# Fill missing values with NaN
complete_df['ft_tot_all_races_v'] = complete_df['ft_tot_all_races_v'].fillna(np.nan)
complete_df['ft_frst_tot_all_races_v'] = complete_df['ft_frst_tot_all_races_v'].fillna(np.nan)
complete_df['CTOTALT'] = complete_df['CTOTALT'].fillna(np.nan)

# Add offset columns
offset_columns = [
    'total', 'total_plus_1', 'first_minus_1', 'first', 'first_plus_1', 
    'grad', 'grad_plus_5', 'grad_plus_6', 'grad_plus_7', 'PA_value', 'Retention'
]

for col in offset_columns:
    complete_df[col] = np.nan

# Function to safely extract first value or return NaN
def safe_extract(arr):
    """Safely extract the first value or return NaN if empty."""
    return arr[0] if len(arr) > 0 else np.nan

# Calculate offset values with safe handling
for index, row in complete_df.iterrows():
    year = row['Year']
    unitid = row['UNITID']

    # Lookup values with safe extraction
    total = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_tot_all_races_v'].values)
    total_plus_1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_tot_all_races_v'].values)

    first_minus_1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_all_races_v'].values)
    first = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_all_races_v'].values)
    first_plus_1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_all_races_v'].values)

    grad = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['CTOTALT'].values)
    grad_plus_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CTOTALT'].values)
    grad_plus_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CTOTALT'].values)
    grad_plus_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CTOTALT'].values)

    # Calculate PA and Retention values safely
    denominator = first_minus_1 + first + first_plus_1
    if denominator and denominator != 0:
        PA_value = (grad_plus_5 + grad_plus_6 + grad_plus_7) / denominator
    else:
        PA_value = np.nan

    retention_denominator = total if total and total != 0 else np.nan
    if retention_denominator:
        Retention = (total_plus_1 + grad - first_plus_1) / retention_denominator
    else:
        Retention = np.nan

    # Assign values
    complete_df.at[index, 'total'] = total
    complete_df.at[index, 'total_plus_1'] = total_plus_1
    complete_df.at[index, 'first_minus_1'] = first_minus_1
    complete_df.at[index, 'first'] = first
    complete_df.at[index, 'first_plus_1'] = first_plus_1
    complete_df.at[index, 'grad'] = grad
    complete_df.at[index, 'grad_plus_5'] = grad_plus_5
    complete_df.at[index, 'grad_plus_6'] = grad_plus_6
    complete_df.at[index, 'grad_plus_7'] = grad_plus_7
    complete_df.at[index, 'PA_value'] = PA_value
    complete_df.at[index, 'Retention'] = Retention

# Save the final result
output_path = '/Users/co25936/Desktop/PER/IPEDS/complete_with_offsets_and_PA.xlsx'
complete_df.to_excel(output_path, index=False)
print(f'File saved at: {output_path}')

# PLOTING 
import matplotlib.pyplot as plt

# 🔥 PA Value Plot
fig, ax = plt.subplots(figsize=(14, 6))  # Increase figure size for more space

# Plot individual UNITID data as dots
for unitid in complete_df['UNITID'].unique():
    subset = complete_df[complete_df['UNITID'] == unitid]
    ax.scatter(subset['Year'], subset['PA_value'], label=f'UNITID {unitid}', alpha=0.5, s=10)

# Plot average line
average_PA = complete_df.groupby('Year')['PA_value'].mean()
ax.plot(average_PA.index, average_PA.values, color='red', label='Average PA', linewidth=2)

# X-axis ticks for every year
ax.set_xticks(range(2000, 2017))
ax.set_xticklabels(range(2000, 2017), rotation=45)

# Move the legend outside the plot and scale it down
ax.legend(
    loc='center left', 
    bbox_to_anchor=(1.05, 0.5),  # Moves the legend outside the plot
    fontsize='small', 
    ncol=3,  # Multiple columns for compactness
    title='UNITIDs'
)

# Titles and labels
ax.set_title('PA Value over Years')
ax.set_xlabel('Year')
ax.set_ylabel('PA Value')
ax.grid(True)

# Adjust layout to prevent overlapping
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Add space on the right for the legend
plt.savefig('/Users/co25936/Desktop/PER/IPEDS/PA_Value.png')
plt.show()


# Retention Plot
fig, ax = plt.subplots(figsize=(14, 6))  # Increase figure size for more space

# Plot individual UNITID data as dots
for unitid in complete_df['UNITID'].unique():
    subset = complete_df[complete_df['UNITID'] == unitid]
    ax.scatter(subset['Year'], subset['Retention'], label=f'UNITID {unitid}', alpha=0.5, s=10)

# Plot average line
average_retention = complete_df.groupby('Year')['Retention'].mean()
ax.plot(average_retention.index, average_retention.values, color='blue', label='Average Retention', linewidth=2)

# X-axis ticks for every year
ax.set_xticks(range(2000, 2024))
ax.set_xticklabels(range(2000, 2024), rotation=45)

# Move the legend outside the plot and scale it down
ax.legend(
    loc='center left', 
    bbox_to_anchor=(1.05, 0.5),  # Moves the legend outside the plot
    fontsize='small', 
    ncol=3,  # Multiple columns for compactness
    title='UNITIDs'
)

# Titles and labels
ax.set_title('Retention over Years')
ax.set_xlabel('Year')
ax.set_ylabel('Retention')
ax.grid(True)

# Adjust layout to prevent overlapping
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Add space on the right for the legend
plt.savefig('/Users/co25936/Desktop/PER/IPEDS/Retention_Value.png')
plt.show()






'''
import pandas as pd
import numpy as np

# Filepath for the original Excel file
file_path = '/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_Combined_file.xlsx'
df = pd.read_excel(file_path)

# Remove rows with missing values in 'ft_tot_all_races_v'
df_trimmed = df.dropna(subset=['ft_tot_all_races_v'])

# Filter by AWLEVEL = 17 and specified UNITIDs
unitid_list = [
    100663, 100751, 104151, 110404, 134130, 139658, 139755, 144005,
    145600, 147703, 151111, 152080, 243780, 153603, 153658, 172644,
    172699, 174066, 176080, 178411, 178396, 178420, 179867, 180461,
    181464, 182670, 183044, 186380, 186867, 186867, 196468, 190415,
    194824, 196130, 196097, 199102, 199120, 199847, 200280, 201885,
    203517, 204857, 206084, 207388, 209542, 209551, 209807, 211273,
    211440, 213543, 214777, 215293, 227757, 230728, 232982, 233921,
    234076, 231624, 236948, 240444
]

# Filter by AWLEVEL and UNITID
filtered_df = df_trimmed[df_trimmed['AWLEVEL'] == 17][['UNITID', 'Year', 'AWLEVEL', 'ft_tot_all_races_v','ft_frst_tot_all_races_v', 'CTOTALT']]
filtered_df = filtered_df[filtered_df['UNITID'].isin(unitid_list)]

# Create a complete DataFrame with all missing years filled
# Generate all years between 2000 and 2023 for each UNITID
all_years = pd.MultiIndex.from_product([unitid_list, range(2000, 2024)], names=['UNITID', 'Year']).to_frame(index=False)

# Merge with the filtered data to add missing years
complete_df = all_years.merge(filtered_df, how='left', on=['UNITID', 'Year'])

# Fill missing AWLEVEL with 17 (since that's the only level we're working with)
complete_df['AWLEVEL'] = complete_df['AWLEVEL'].fillna(17)

# Fill missing values in 'ft_tot_all_races_v' and 'CTOTALT' with NaN
complete_df['ft_tot_all_races_v'] = complete_df['ft_tot_all_races_v'].fillna(np.nan)
complete_df['CTOTALT'] = complete_df['CTOTALT'].fillna(np.nan)

# Add offset columns
complete_df['total'] = None
complete_df['total_plus_1'] = None
complete_df['first_minus_1'] = None
complete_df['first']= None
complete_df['first_plus_1'] = None
complete_df['grad'] = None
complete_df['grad_plus_5'] = None
complete_df['grad_plus_6'] = None
complete_df['grad_plus_7'] = None
complete_df['PA_value'] = None
complete_df['Retention'] = None



# Calculate offset values
for index, row in complete_df.iterrows():
    year = row['Year']
    unitid = row['UNITID']

    # Lookup values with year offsets
    total = complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year )]['ft_tot_all_races_v'].values
    total_plus_1 = complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_tot_all_races_v'].values

    first_minus_1 = complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_all_races_v'].values
    first = complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_all_races_v'].values
    first_plus_1 = complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_all_races_v'].values

    grad = complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['CTOTALT'].values
    grad_plus_5 = complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CTOTALT'].values
    grad_plus_6 = complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CTOTALT'].values
    grad_plus_7 = complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CTOTALT'].values

    # Calculate the PA and RA values
    PA_value = (grad_plus_5+grad_plus_6+grad_plus_7)/ (first_minus_1 + first + first_plus_1)
    Retention  = (total_plus_1 + grad - first_plus_1) / total

    # Assign the offset values if they exist
    complete_df.at[index, 'total'] = total[0] if len(total) > 0 else None
    complete_df.at[index, 'total_plus_1'] = total_plus_1[0] if len(total_plus_1) > 0 else None
    complete_df.at[index, 'first_minus_1'] = first_minus_1[0] if len(first_minus_1) > 0 else None
    complete_df.at[index, 'first'] = first[0] if len(first) > 0 else None
    complete_df.at[index, 'first_plus_1'] = first_plus_1[0] if len(first_plus_1) > 0 else None
    complete_df.at[index, 'grad'] = grad[0] if len(grad) > 0 else None
    complete_df.at[index, 'grad_plus_5'] = grad_plus_5[0] if len(grad_plus_5) > 0 else None
    complete_df.at[index, 'grad_plus_6'] = grad_plus_6[0] if len(grad_plus_6) > 0 else None
    complete_df.at[index, 'grad_plus_7'] = grad_plus_7[0] if len(grad_plus_7) > 0 else None
    complete_df.at[index, 'PA_value'] = PA_value[0] if len(PA_value) > 0 else None
    complete_df.at[index, 'Retention'] = Retention[0] if len(Retention) > 0 else None




# Save the final result with the new columns
output_path = '/Users/co25936/Desktop/PER/IPEDS/complete_with_missing_years.xlsx'
complete_df.to_excel(output_path, index=False)
print(f'File with missing years and offsets saved at: {output_path}')
'''