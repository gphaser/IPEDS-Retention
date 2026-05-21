# IMPORTAINT NEED TO ADJUST CARIABLES TO ACCOUNT FOR NOW ALL BEING LOWER CASE!

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


# Filter by awlevel and unitid
filtered_df = df_trimmed[df_trimmed['awlevel'] == 17][[
    'unitid', 'year', 'awlevel',
    'ft_tot_all_races_v', 'ft_frst_tot_all_races_v',
    'ctotalt', 'ctotalm', 'ctotalw',
    'ma_ft_tot_all_races_v','dr_ft_tot_all_races_v',
    'ma_ft_frst_tot_all_races_v', 'dr_ft_frst_tot_all_races_v', 

    #Sex Breakdown- First time enrollment 
    'ft_frst_men_all_races_v', 'ft_frst_wmen_all_races_v',
    "dr_ft_frst_men_all_races_v", "dr_ft_frst_wmen_all_races_v",
    "ma_ft_frst_men_all_races_v", "ma_ft_frst_wmen_all_races_v",
    #Sex breakdown - entrollment total
    'ft_men_all_races_v', 'ft_wmen_all_races_v',
    "dr_ft_men_all_races_v", "dr_ft_wmen_all_races_v",
    "ma_ft_men_all_races_v", "ma_ft_wmen_all_races_v",
     
     # Racial/Ethnic breakdowns - Total Enrollment
    "ft_tot_black_v", "ft_tot_indian_v", "ft_tot_asian_v", "ft_tot_pacific_v",
    "ft_tot_white_v", "ft_tot_hisp_v", "ft_tot_multi_v", "ft_tot_unk_v", "ft_tot_forgn_v",

    #Racial/Ethinc breakdwon - degrees earben
        # Racial breakdown, Non-residental alien, Black,Native American/Alaskin, Asian/Pacific islander, Hispanic, White, Unknown,
        'crace17_std', 'crace18_std','crace19_std', 'crace20_std','crace21_std', 'crace22_std', 'cunknt',
        # Other racial breakdowns Black, Aisan, Native Hawian/Pacific islander Hispanic/Latino., White (Unknown is the same),  2 or more races, non-american students
        'cbkaat','casiat','cnhpit', 'chispt', 'cwhitt', 'c2mort', 'cnralt', 
    
    # Racial/Ethnic breakdowns - First-Time Enrollment
    "ft_frst_tot_black_v", "ft_frst_tot_indian_v", "ft_frst_tot_asian_v", "ft_frst_tot_pacific_v",
    "ft_frst_tot_white_v", "ft_frst_tot_hisp_v", "ft_frst_tot_multi_v", "ft_frst_tot_unk_v", "ft_frst_tot_forgn_v"]

]
# If a school has >1 row in a year, sum numeric columns
filtered_df = filtered_df.groupby(["unitid", "year"], as_index=False).sum(numeric_only=True)

# Instead of unitid_list, pull all unique unitids from the dataset
all_unitids = filtered_df['unitid'].unique()

# Create a complete DataFrame with all missing years filled (2000–2023 for ALL unitids)
all_years = pd.MultiIndex.from_product([all_unitids, range(2000, 2024)], names=['unitid', 'year']).to_frame(index=False)
complete_df = all_years.merge(filtered_df, how='left', on=['unitid', 'year'])

# Create a complete DataFrame with all missing years filled
all_years = pd.MultiIndex.from_product([all_unitids, range(2000, 2024)], names=['unitid', 'year']).to_frame(index=False)
complete_df = all_years.merge(filtered_df, how='left', on=['unitid', 'year'])

# Fill missing awlevel with 17
complete_df['awlevel'] = complete_df['awlevel'].fillna(17)

# Fill missing values with NaN``
complete_df['ft_tot_all_races_v'] = complete_df['ft_tot_all_races_v'].fillna(np.nan)
complete_df['ft_frst_tot_all_races_v'] = complete_df['ft_frst_tot_all_races_v'].fillna(np.nan)
complete_df['ctotalt'] = complete_df['ctotalt'].fillna(np.nan)

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


# Example: write complete_df to Excel
output_path = "/Users/co25936/Desktop/PER/IPEDS/complete_output.xlsx"

# index=False prevents pandas from writing the row numbers as an extra column
complete_df.to_excel(output_path, index=False)

print(f"File saved at: {output_path}")

# Calculate offset values with safe handling
for index, row in complete_df.iterrows():
    year = row['year']
    unitid = row['unitid']

    # Lookup values with safe extraction
    total = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year)]['ft_tot_all_races_v'].values)
    total_plus_1 = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year + 1)]['ft_tot_all_races_v'].values)

    first_minus_1 = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year - 1)]['ft_frst_tot_all_races_v'].values)
    first = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year)]['ft_frst_tot_all_races_v'].values)
    first_plus_1 = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year + 1)]['ft_frst_tot_all_races_v'].values)

    grad = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year)]['ctotalt'].values)

    grad_plus_1 = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year + 1)]['ctotalt'].values)
    grad_plus_5 = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year + 5)]['ctotalt'].values)
    grad_plus_6 = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year + 6)]['ctotalt'].values)
    grad_plus_7 = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year + 7)]['ctotalt'].values)



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
output_path = '/Users/co25936/Desktop/PER/IPEDS/complete_with_offsets_and_PA_noIPEDS_All_unitidS.xlsx'
complete_df.to_excel(output_path, index=False)
print(f'File saved at: {output_path}')

# --- Aggregate PCR across unitids instead of averaging ---

# Collapse the data by year (sum across unitids)
yearly_totals = complete_df.groupby("year").agg({
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



# Count unique unitids per year
unitid_counts = complete_df.groupby("year")["unitid"].nunique().reset_index()
unitid_counts.columns = ["year", "Unique_unitids"]

print("\nNumber of unique unitids per year:")
print(unitid_counts)

# Correct way: use the raw column, not the offset one
true_enrollment_and_grads = filtered_df.groupby("year").agg({
    "ft_frst_tot_all_races_v": "sum",   # first-year enrollments
    "ctotalt": "sum"                    # PhD grads
}).reset_index()

print("\nTRUE Number of first years per year (direct from IPEDS):")
print(true_enrollment_and_grads[["year", "ft_frst_tot_all_races_v"]])

print("\nTRUE Number of male first years per year (direct from IPEDS):")
print(filtered_df[["year", "ft_frst_men_all_races_v"]])

print("\nTRUE Number of female first years per year (direct from IPEDS):")
print(filtered_df[["year", "ft_frst_wmen_all_races_v"]])

print("\nTRUE Number of PhD grads per year (direct from IPEDS):")
print(true_enrollment_and_grads[["year", "ctotalt"]])

print("\nTRUE Number of male grads per year (direct from IPEDS):")
print(filtered_df[["year", "ctotalm"]])

print("\nTRUE Number of female grads per year (direct from IPEDS):")
print(filtered_df[["year", "ctotalw"]])


# TO CHECK IF MALE + FEMALE = TOTAL


# --- Find institutions with PCR > 2 ---
high_pcr_df = complete_df[complete_df["PCR_value"] > 2]

if not high_pcr_df.empty:
    print("\nunitids with PCR_value > 2:")
    for _, row in high_pcr_df[["unitid", "year", "PCR_value"]].sort_values(["unitid", "year"]).iterrows():
        print(f"unitid: {row['unitid']}, year: {int(row['year'])}, PCR_value: {row['PCR_value']:.3f}")
else:
    print("\nNo institutions with PCR_value > 2.")



''' OLD WAY
# Aggregate first-years and PhD grads across unitids per year
enrollment_and_grads = complete_df.groupby("year").agg({
    "first": "sum",   # first-year enrollments
    "grad": "sum"     # PhD grads (ctotalt)
}).reset_index()

print("\nNumber of first years per year:")
print(enrollment_and_grads[["year", "first"]])

print("\nNumber of PhD grads per year:")
print(enrollment_and_grads[["year", "grad"]])
'''

# --- Plotting only 2001–2016 ---
fig, ax = plt.subplots(figsize=(14, 6))

# Restrict scatter to 2001–2016
for unitid in complete_df["unitid"].unique():
    subset = complete_df[(complete_df["unitid"] == unitid) & 
                         (complete_df["year"].between(2001, 2016))]
    ax.scatter(subset["year"], subset["PCR_value"], alpha=0.3, s=20)

# Restrict yearly_totals to 2001–2016
yearly_subset = yearly_totals[yearly_totals["year"].between(2001, 2016)]

# Plot the total PCR (red line)
ax.plot(yearly_subset["year"], yearly_subset["PCR_value_total"],
        color="red", linewidth=2, label="Total PCR (summed across unitids)")

print(yearly_totals["PCR_value_total"])


# Set ticks only for 2001–2016
ax.set_xticks(range(2001, 2017))
ax.set_xticklabels(range(2001, 2017), rotation=45)

# Optionally enforce x-axis range
ax.set_xlim(2001, 2016)

ax.set_title("PCR Value (Summed Across all unitids, 2001–2016)", fontsize=18)
ax.set_xlabel("year", fontsize=16)
ax.set_ylabel("PCR Value", fontsize=16)
ax.legend()
ax.grid(True)

# Adjust y-axis to have ticks at each integer
y_min, y_max = ax.get_ylim()
ax.set_yticks(np.arange(np.floor(y_min), np.ceil(y_max) + 1, 1))


plt.tight_layout()
plt.savefig('/Users/co25936/Desktop/PER/IPEDS/PCR_Value_Total_noAvg_All_unitidS.png')
plt.show()


# FOR Limited unitid's

# Filter by awlevel = 17 and specified unitids
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

# Filter by awlevel and unitid
filtered_df = df_trimmed[df_trimmed['awlevel'] == 17][[
    'unitid', 'year', 'awlevel',
    'ft_tot_all_races_v', 'ft_frst_tot_all_races_v',
    'ctotalt', 'ctotalm', 'ctotalw',
    'ma_ft_men_all_races_v', 'ma_ft_wmen_all_races_v', 'ma_ft_tot_all_races_v',
    'dr_ft_men_all_races_v', 'dr_ft_wmen_all_races_v', 'dr_ft_tot_all_races_v',
    'ma_ft_frst_tot_all_races_v', 'dr_ft_frst_tot_all_races_v', 

    #Sex Breakdown- First time enrollment 
    'ft_frst_men_all_races_v', 'ft_frst_wmen_all_races_v',
    'ma_ft_frst_men_all_races_v','dr_ft_frst_men_all_races_v',
    #Sex Breakdown - Full time enrollment
    'ft_men_all_races_v', 'ft_wmen_all_races_v',
    'ma_ft_men_all_races_v','dr_ft_men_all_races_v',


     # Racial/Ethnic breakdowns - Total Enrollment
    "ft_tot_black_v", "ft_tot_indian_v", "ft_tot_asian_v", "ft_tot_pacific_v",
    "ft_tot_white_v", "ft_tot_hisp_v", "ft_tot_multi_v", "ft_tot_unk_v", "ft_tot_forgn_v",

    #Racial/Ethinc breakdwon - degrees earben
        # Racial breakdown, Non-residental alien, Black,Native American/Alaskin, Asian/Pacific islander, Hispanic, White, Unknown,
        'crace17_std', 'crace18_std','crace19_std', 'crace20_std','crace21_std', 'crace22_std', 'cunknt',
        # Other racial breakdowns Black, Aisan, Native Hawian/Pacific islander Hispanic/Latino., White (Unknown is the same),  2 or more races, non-american students
        'cbkaat','casiat','cnhpit', 'chispt', 'cwhitt', 'c2mort', 'cnralt', 
    
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
    years = sorted(df['year'].dropna().unique())
    stats = []

    for year in years:
        values = df[df['year'] == year][value_column]
        mean, lower, upper = bootstrap_ci(values)
        stats.append({'year': year, 'Mean': mean, 'Lower': lower, 'Upper': upper})

    return pd.DataFrame(stats)



filtered_df = filtered_df[filtered_df['unitid'].isin(unitid_list)]

# Create a complete DataFrame with all missing years filled
all_years = pd.MultiIndex.from_product([unitid_list, range(2000, 2024)], names=['unitid', 'year']).to_frame(index=False)
complete_df = all_years.merge(filtered_df, how='left', on=['unitid', 'year'])

# Fill missing awlevel with 17
complete_df['awlevel'] = complete_df['awlevel'].fillna(17)

# Fill missing values with NaN
complete_df['ft_tot_all_races_v'] = complete_df['ft_tot_all_races_v'].fillna(np.nan)
complete_df['ft_frst_tot_all_races_v'] = complete_df['ft_frst_tot_all_races_v'].fillna(np.nan)
complete_df['ctotalt'] = complete_df['ctotalt'].fillna(np.nan)

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
    year = row['year']
    unitid = row['unitid']

    # Lookup values with safe extraction
    total = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year)]['ft_tot_all_races_v'].values)
    total_plus_1 = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year + 1)]['ft_tot_all_races_v'].values)

    first_minus_1 = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year - 1)]['ft_frst_tot_all_races_v'].values)
    first = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year)]['ft_frst_tot_all_races_v'].values)
    first_plus_1 = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year + 1)]['ft_frst_tot_all_races_v'].values)

    grad = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year)]['ctotalt'].values)
    grad_plus_1 = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year + 1)]['ctotalt'].values)
    grad_plus_5 = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year + 5)]['ctotalt'].values)
    grad_plus_6 = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year + 6)]['ctotalt'].values)
    grad_plus_7 = safe_extract(complete_df[(complete_df['unitid'] == unitid) & (complete_df['year'] == year + 7)]['ctotalt'].values)

    
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

# --- Aggregate PCR across unitids instead of averaging ---

# Collapse the data by year (sum across unitids)
yearly_totals = complete_df.groupby("year").agg({
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

# Count unique unitids per year
unitid_counts = complete_df.groupby("year")["unitid"].nunique().reset_index()
unitid_counts.columns = ["year", "Unique_unitids"]

print("\nNumber of unique unitids per year:")
print(unitid_counts)

# Aggregate first-years and PhD grads across unitids per year
enrollment_and_grads = complete_df.groupby("year").agg({
    "first": "sum",   # first-year enrollments
    "grad": "sum"     # PhD grads (ctotalt)
}).reset_index()

print("\nNumber of first years per year:")
print(enrollment_and_grads[["year", "first"]])

print("\nNumber of PhD grads per year:")
print(enrollment_and_grads[["year", "grad"]])


# --- Find institutions with PCR > 2 ---
high_pcr_df = complete_df[complete_df["PCR_value"] > 2]

if not high_pcr_df.empty:
    print("\nunitids with PCR_value > 2:")
    for _, row in high_pcr_df[["unitid", "year", "PCR_value"]].sort_values(["unitid", "year"]).iterrows():
        print(f"unitid: {row['unitid']}, year: {int(row['year'])}, PCR_value: {row['PCR_value']:.3f}")
else:
    print("\nNo institutions with PCR_value > 2.")



# --- Plotting only 2001–2016 ---
fig, ax = plt.subplots(figsize=(14, 6))

# Restrict scatter to 2001–2016
for unitid in complete_df["unitid"].unique():
    subset = complete_df[(complete_df["unitid"] == unitid) & 
                         (complete_df["year"].between(2001, 2016))]
    ax.scatter(subset["year"], subset["PCR_value"], alpha=0.3, s=20)

# Restrict yearly_totals to 2001–2016
yearly_subset = yearly_totals[yearly_totals["year"].between(2001, 2016)]

# Plot the total PCR (red line)
ax.plot(yearly_subset["year"], yearly_subset["PCR_value_total"],
        color="red", linewidth=2, label="Total PCR (summed across unitids)")

print(yearly_totals["PCR_value_total"])

# Set ticks only for 2001–2016
ax.set_xticks(range(2001, 2017))
ax.set_xticklabels(range(2001, 2017), rotation=45)

# Optionally enforce x-axis range
ax.set_xlim(2001, 2016)

ax.set_title("PCR Value (Unweighteted avg)", fontsize=18)
ax.set_xlabel("year", fontsize=16)
ax.set_ylabel("PCR Value", fontsize=16)
ax.legend()
ax.grid(True)

plt.tight_layout()
plt.savefig('/Users/co25936/Desktop/PER/IPEDS/PCR_Value_Total_noAvg_2001_2016.png')
plt.show()



