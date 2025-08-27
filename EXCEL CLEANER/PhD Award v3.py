import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Filepath for the original Excel file
# test line file_path = '/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_Combined_test_file.xlsx'
file_path = '/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_Combined_file.xlsx'
df = pd.read_excel(file_path)

# Remove rows with missing values in 'ft_tot_all_races_v'
df_trimmed = df.dropna(subset=['ft_tot_all_races_v'])


#  FOR ALL UNIVERSITIES


# Filter by AWLEVEL and UNITID
filtered_df = df_trimmed[df_trimmed['AWLEVEL'] == 17][[
    'UNITID', 'Year', 'AWLEVEL',
    'ft_tot_all_races_v', 'ft_frst_tot_all_races_v',
    'CTOTALT', 'CTOTALM', 'CTOTALW',
    'ma_ft_men_all_races_v', 'ma_ft_wmen_all_races_v', 'ma_ft_tot_all_races_v',
    'dr_ft_men_all_races_v', 'dr_ft_wmen_all_races_v', 'dr_ft_tot_all_races_v',
    'ma_ft_frst_tot_all_races_v', 'dr_ft_frst_tot_all_races_v', 

    #Sex Breakdown- First time enrollment 
    'ft_frst_men_all_races_v', 'ft_frst_wmen_all_races_v',
     
     # Racial/Ethnic breakdowns - Total Enrollment
    "ft_tot_black_v", "ft_tot_indian_v", "ft_tot_asian_v", "ft_tot_pacific_v",
    "ft_tot_white_v", "ft_tot_hisp_v", "ft_tot_multi_v", "ft_tot_unk_v", "ft_tot_forgn_v",

    #Racial/Ethinc breakdwon - degrees earben
        # Racial breakdown, Non-residental alien, Black,Native American/Alaskin, Asian/Pacific islander, Hispanic, White, Unknown,
        'CRACE17_STD', 'CRACE18_STD','CRACE19_STD', 'CRACE20_STD','CRACE21_STD', 'CRACE22_STD', 'CUNKNT',
        # Other racial breakdowns Black, Aisan, Native Hawian/Pacific islander Hispanic/Latino., White (Unknown is the same),  2 or more races, non-american students
        'CBKAAT','CASIAT','CNHPIT', 'CHISPT', 'CWHITT', 'C2MORT', 'CNRALT', 
    
    # Racial/Ethnic breakdowns - First-Time Enrollment
    "ft_frst_tot_black_v", "ft_frst_tot_indian_v", "ft_frst_tot_asian_v", "ft_frst_tot_pacific_v",
    "ft_frst_tot_white_v", "ft_frst_tot_hisp_v", "ft_frst_tot_multi_v", "ft_frst_tot_unk_v", "ft_frst_tot_forgn_v"]

]

# TO ADD Bootstrap error bars
from scipy.stats import bootstrap

def bootstrap_ci(data, n_bootstrap=1000, ci=0.95):
    """Bootstrap the mean and return lower and upper bounds of the confidence interval."""
    data = data.dropna().values
    if len(data) < 2:
        return (np.nan, np.nan, np.nan)
    res = bootstrap((data,), np.mean, confidence_level=ci, n_resamples=n_bootstrap, method='basic')
    return (np.mean(data), res.confidence_interval.low, res.confidence_interval.high)

def get_bootstrap_stats(df, value_column):
    years = sorted(df['Year'].dropna().unique())
    stats = []

    for year in years:
        values = df[df['Year'] == year][value_column]
        mean, lower, upper = bootstrap_ci(values)
        stats.append({'Year': year, 'Mean': mean, 'Lower': lower, 'Upper': upper})

    return pd.DataFrame(stats)



# Instead of unitid_list, pull all unique UNITIDs from the dataset
all_unitids = filtered_df['UNITID'].unique()

# Create a complete DataFrame with all missing years filled (2000–2023 for ALL UNITIDs)
all_years = pd.MultiIndex.from_product([all_unitids, range(2000, 2024)], names=['UNITID', 'Year']).to_frame(index=False)
complete_df = all_years.merge(filtered_df, how='left', on=['UNITID', 'Year'])

# Create a complete DataFrame with all missing years filled
all_years = pd.MultiIndex.from_product([all_unitids, range(2000, 2024)], names=['UNITID', 'Year']).to_frame(index=False)
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
    'grad', 'grad_plus_5', 'grad_plus_6', 'grad_plus_7', 'PCR_value', 'Retention'
]

for col in offset_columns:
    complete_df[col] = np.nan

# Function to safely extract first value or return NaN

# Older version
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
    grad_plus_1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['CTOTALT'].values)
    grad_plus_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CTOTALT'].values)
    grad_plus_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CTOTALT'].values)
    grad_plus_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CTOTALT'].values)

    
    # Calculate PCR and Retention values safely
    denominator = first_minus_1 + first + first_plus_1
    if denominator and denominator != 0:
        PCR_value = (grad_plus_5 + grad_plus_6 + grad_plus_7) / denominator
    else:
        PCR_value = np.nan

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
    complete_df.at[index, 'PCR_value'] = PCR_value
    complete_df.at[index, 'Retention'] = Retention



# Save the final result
output_path = '/Users/co25936/Desktop/PER/IPEDS/complete_with_offsets_and_PA_noIPEDS_All_UNITIDS.xlsx'
complete_df.to_excel(output_path, index=False)
print(f'File saved at: {output_path}')

# --- Aggregate PCR across UNITIDs instead of averaging ---

# Collapse the data by year (sum across UNITIDs)
yearly_totals = complete_df.groupby("Year").agg({
    "first_minus_1": "sum",
    "first": "sum",
    "first_plus_1": "sum",
    "grad_plus_5": "sum",
    "grad_plus_6": "sum",
    "grad_plus_7": "sum"
}).reset_index()

# Calculate PCR using sums (not averages of ratios)
yearly_totals["PCR_value_total"] = (
    (yearly_totals["grad_plus_5"] + yearly_totals["grad_plus_6"] + yearly_totals["grad_plus_7"]) /
    (yearly_totals["first_minus_1"] + yearly_totals["first"] + yearly_totals["first_plus_1"])
)

# --- Plotting only 2001–2016 ---
fig, ax = plt.subplots(figsize=(14, 6))

# Restrict scatter to 2001–2016
for unitid in complete_df["UNITID"].unique():
    subset = complete_df[(complete_df["UNITID"] == unitid) & 
                         (complete_df["Year"].between(2001, 2016))]
    ax.scatter(subset["Year"], subset["PCR_value"], alpha=0.3, s=20)

# Restrict yearly_totals to 2001–2016
yearly_subset = yearly_totals[yearly_totals["Year"].between(2001, 2016)]

# Plot the total PCR (red line)
ax.plot(yearly_subset["Year"], yearly_subset["PCR_value_total"],
        color="red", linewidth=2, label="Total PCR (summed across UNITIDs)")

print(yearly_totals["PCR_value_total"])

# Set ticks only for 2001–2016
ax.set_xticks(range(2001, 2017))
ax.set_xticklabels(range(2001, 2017), rotation=45)

# Optionally enforce x-axis range
ax.set_xlim(2001, 2016)

ax.set_title("PCR Value (Summed Across all UNITIDs, 2001–2016)", fontsize=18)
ax.set_xlabel("Year", fontsize=16)
ax.set_ylabel("PCR Value", fontsize=16)
ax.legend()
ax.grid(True)

# Adjust y-axis to have ticks at each integer
y_min, y_max = ax.get_ylim()
ax.set_yticks(np.arange(np.floor(y_min), np.ceil(y_max) + 1, 1))


plt.tight_layout()
plt.savefig('/Users/co25936/Desktop/PER/IPEDS/PCR_Value_Total_noAvg_All_UNITIDS.png')
plt.show()


# FOR Limited UNITID's

# Filter by AWLEVEL = 17 and specified UNITIDs
unitid_list = [
    100663, 100751, 104151, 110404, 
    134130,139658, 139755, 144005,
    145600, 147703, 151111, 152080, 243780, 153603, 153658, 172644,
    172699, 174066, 176080, 178411, 178396, 178420, 179867, 180461,
    181464, 182670, 183044, 186380, 186867, 190044, 196468, 190415,
    194824, 196130, 196097, 199102, 199120, 199847, 200280, 201885,
    203517, 204857, 206084, 207388, 209542, 209551, 209807, 211273,
    211440, 213543, 214777, 215293, 227757, 230728, 232982, 233921,
    234076, 231624, 236948, 240444
]

# Filter by AWLEVEL and UNITID
filtered_df = df_trimmed[df_trimmed['AWLEVEL'] == 17][[
    'UNITID', 'Year', 'AWLEVEL',
    'ft_tot_all_races_v', 'ft_frst_tot_all_races_v',
    'CTOTALT', 'CTOTALM', 'CTOTALW',
    'ma_ft_men_all_races_v', 'ma_ft_wmen_all_races_v', 'ma_ft_tot_all_races_v',
    'dr_ft_men_all_races_v', 'dr_ft_wmen_all_races_v', 'dr_ft_tot_all_races_v',
    'ma_ft_frst_tot_all_races_v', 'dr_ft_frst_tot_all_races_v', 

    #Sex Breakdown- First time enrollment 
    'ft_frst_men_all_races_v', 'ft_frst_wmen_all_races_v',
     
     # Racial/Ethnic breakdowns - Total Enrollment
    "ft_tot_black_v", "ft_tot_indian_v", "ft_tot_asian_v", "ft_tot_pacific_v",
    "ft_tot_white_v", "ft_tot_hisp_v", "ft_tot_multi_v", "ft_tot_unk_v", "ft_tot_forgn_v",

    #Racial/Ethinc breakdwon - degrees earben
        # Racial breakdown, Non-residental alien, Black,Native American/Alaskin, Asian/Pacific islander, Hispanic, White, Unknown,
        'CRACE17_STD', 'CRACE18_STD','CRACE19_STD', 'CRACE20_STD','CRACE21_STD', 'CRACE22_STD', 'CUNKNT',
        # Other racial breakdowns Black, Aisan, Native Hawian/Pacific islander Hispanic/Latino., White (Unknown is the same),  2 or more races, non-american students
        'CBKAAT','CASIAT','CNHPIT', 'CHISPT', 'CWHITT', 'C2MORT', 'CNRALT', 
    
    # Racial/Ethnic breakdowns - First-Time Enrollment
    "ft_frst_tot_black_v", "ft_frst_tot_indian_v", "ft_frst_tot_asian_v", "ft_frst_tot_pacific_v",
    "ft_frst_tot_white_v", "ft_frst_tot_hisp_v", "ft_frst_tot_multi_v", "ft_frst_tot_unk_v", "ft_frst_tot_forgn_v"]

]

# TO ADD Bootstrap error bars
from scipy.stats import bootstrap

def bootstrap_ci(data, n_bootstrap=1000, ci=0.95):
    """Bootstrap the mean and return lower and upper bounds of the confidence interval."""
    data = data.dropna().values
    if len(data) < 2:
        return (np.nan, np.nan, np.nan)
    res = bootstrap((data,), np.mean, confidence_level=ci, n_resamples=n_bootstrap, method='basic')
    return (np.mean(data), res.confidence_interval.low, res.confidence_interval.high)

def get_bootstrap_stats(df, value_column):
    years = sorted(df['Year'].dropna().unique())
    stats = []

    for year in years:
        values = df[df['Year'] == year][value_column]
        mean, lower, upper = bootstrap_ci(values)
        stats.append({'Year': year, 'Mean': mean, 'Lower': lower, 'Upper': upper})

    return pd.DataFrame(stats)



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
    'grad', 'grad_plus_5', 'grad_plus_6', 'grad_plus_7', 'PCR_value', 'Retention'
]

for col in offset_columns:
    complete_df[col] = np.nan

# Function to safely extract first value or return NaN

# Older version
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
    grad_plus_1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['CTOTALT'].values)
    grad_plus_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CTOTALT'].values)
    grad_plus_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CTOTALT'].values)
    grad_plus_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CTOTALT'].values)

    
    # Calculate PCR and Retention values safely
    denominator = first_minus_1 + first + first_plus_1
    if denominator and denominator != 0:
        PCR_value = (grad_plus_5 + grad_plus_6 + grad_plus_7) / denominator
    else:
        PCR_value = np.nan

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
    complete_df.at[index, 'PCR_value'] = PCR_value
    complete_df.at[index, 'Retention'] = Retention



# Save the final result
output_path = '/Users/co25936/Desktop/PER/IPEDS/complete_with_offsets_and_PA_noIPEDS_noAvg.xlsx'
complete_df.to_excel(output_path, index=False)
print(f'File saved at: {output_path}')

# --- Aggregate PCR across UNITIDs instead of averaging ---

# Collapse the data by year (sum across UNITIDs)
yearly_totals = complete_df.groupby("Year").agg({
    "first_minus_1": "sum",
    "first": "sum",
    "first_plus_1": "sum",
    "grad_plus_5": "sum",
    "grad_plus_6": "sum",
    "grad_plus_7": "sum"
}).reset_index()

# Calculate PCR using sums (not averages of ratios)
yearly_totals["PCR_value_total"] = (
    (yearly_totals["grad_plus_5"] + yearly_totals["grad_plus_6"] + yearly_totals["grad_plus_7"]) /
    (yearly_totals["first_minus_1"] + yearly_totals["first"] + yearly_totals["first_plus_1"])
)

# --- Plotting only 2001–2016 ---
fig, ax = plt.subplots(figsize=(14, 6))

# Restrict scatter to 2001–2016
for unitid in complete_df["UNITID"].unique():
    subset = complete_df[(complete_df["UNITID"] == unitid) & 
                         (complete_df["Year"].between(2001, 2016))]
    ax.scatter(subset["Year"], subset["PCR_value"], alpha=0.3, s=20)

# Restrict yearly_totals to 2001–2016
yearly_subset = yearly_totals[yearly_totals["Year"].between(2001, 2016)]

# Plot the total PCR (red line)
ax.plot(yearly_subset["Year"], yearly_subset["PCR_value_total"],
        color="red", linewidth=2, label="Total PCR (summed across UNITIDs)")

print(yearly_totals["PCR_value_total"])

# Set ticks only for 2001–2016
ax.set_xticks(range(2001, 2017))
ax.set_xticklabels(range(2001, 2017), rotation=45)

# Optionally enforce x-axis range
ax.set_xlim(2001, 2016)

ax.set_title("PCR Value (Unweighteted avg)", fontsize=18)
ax.set_xlabel("Year", fontsize=16)
ax.set_ylabel("PCR Value", fontsize=16)
ax.legend()
ax.grid(True)

plt.tight_layout()
plt.savefig('/Users/co25936/Desktop/PER/IPEDS/PCR_Value_Total_noAvg_2001_2016.png')
plt.show()



