import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Filepath for the original Excel file
# test line file_path = '/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_Combined_test_file.xlsx'
file_path = '/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_Combined_file.xlsx'
df = pd.read_excel(file_path)

# Remove rows with missing values in 'ft_tot_all_races_v'
df_trimmed = df.dropna(subset=['ft_tot_all_races_v'])

# Filter by AWLEVEL = 17 and specified UNITIDs
unitid_list = [
    100663, 100751, 104151, 110404, 134130, 139658, 139755, 144005,
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

    #Gender Breakdown- First time enrollment 
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
output_path = '/Users/co25936/Desktop/PER/IPEDS/complete_with_offsets_and_PA_noIPEDS.xlsx'
complete_df.to_excel(output_path, index=False)
print(f'File saved at: {output_path}')

# PLOTING 
import matplotlib.pyplot as plt

# PCR Value Plot
fig, ax = plt.subplots(figsize=(14, 6))  # Increase figure size for more space

# Plot individual UNITID data as dots
for unitid in complete_df['UNITID'].unique():
    subset = complete_df[complete_df['UNITID'] == unitid]
    ax.scatter(subset['Year'], subset['PCR_value'], label=f'UNITID {unitid}', alpha=0.5, s=10)

# Plot average line
average_PCR = complete_df.groupby('Year')['PCR_value'].mean()
ax.plot(average_PCR.index, average_PCR.values, color='red', label='Average PCR', linewidth=2)
print(average_PCR)

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
ax.set_title('PCR Value over Years')
ax.set_xlabel('Year')
ax.set_ylabel('PCR Value')
ax.grid(True)

# Adjust layout to prevent overlapping
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Add space on the right for the legend
plt.savefig('/Users/co25936/Desktop/PER/IPEDS/PCR_Value.png')
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





# --- 1. PCR VALUE MALE VS FEMALE ---

# Create PCR values for male and female based on CTOTALM and CTOTALW
complete_df['PCR_value_male'] = np.nan
complete_df['PCR_value_female'] = np.nan

for index, row in complete_df.iterrows():
    year = row['Year']
    unitid = row['UNITID']

    # Graduation by gender
    grad_m_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CTOTALM'].values)
    grad_m_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CTOTALM'].values)
    grad_m_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CTOTALM'].values)

    grad_f_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CTOTALW'].values)
    grad_f_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CTOTALW'].values)
    grad_f_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CTOTALW'].values)

    # First-year full-time enrollment by gender
    first_m1_m = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_men_all_races_v'].values)
    first_m_m = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_men_all_races_v'].values)
    first_p1_m = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_men_all_races_v'].values)

    first_m1_f = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_wmen_all_races_v'].values)
    first_m_f = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_wmen_all_races_v'].values)
    first_p1_f = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_wmen_all_races_v'].values)

    # Denominators
    denom_m = first_m1_m + first_m_m + first_p1_m
    denom_f = first_m1_f + first_m_f + first_p1_f

    # PCR Value calculation
    if denom_m and denom_m != 0:
        complete_df.at[index, 'PCR_value_male'] = (grad_m_5 + grad_m_6 + grad_m_7) / denom_m

    if denom_f and denom_f != 0:
        complete_df.at[index, 'PCR_value_female'] = (grad_f_5 + grad_f_6 + grad_f_7) / denom_f


# --- PLOT: PCR VALUE MALE VS FEMALE ---

fig, ax = plt.subplots(figsize=(14, 6))

#years to plot
years_to_plot = list(range(2001, 2017))

# Plot averages
avg_PCR_male = complete_df.groupby('Year')['PCR_value_male'].mean().loc[years_to_plot]
avg_PCR_female = complete_df.groupby('Year')['PCR_value_female'].mean().loc[years_to_plot] 
print("MALE PCR:", avg_PCR_male)
print("FEMALE PCR:", avg_PCR_female)


ax.plot(avg_PCR_male.index, avg_PCR_male.values, label='Male PCR Value', color='blue', linewidth=2)
ax.plot(avg_PCR_female.index, avg_PCR_female.values, label='Female PCR Value', color='purple', linewidth=2)

ax.set_xticks(range(2001, 2017))
ax.set_xticklabels(range(2001, 2017), rotation=45)

ax.set_title("PCR Value by Gender Over Time")
ax.set_xlabel("Year")
ax.set_ylabel("PCR Value")
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.savefig('/Users/co25936/Desktop/PER/IPEDS/PCR_Value_Male_vs_Female.png')
plt.show()



# 2 PCR plot using dr_ft_frst_tot_all_races_v and CTOTAL
# --- PCR VALUE using Doctoral First-Time Enrollment ---

complete_df['PCR_value_doctoral'] = np.nan

for index, row in complete_df.iterrows():
    year = row['Year']
    unitid = row['UNITID']

    # Doctoral first-time enrollment
    dr_m1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['dr_ft_frst_tot_all_races_v'].values)
    dr_0  = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['dr_ft_frst_tot_all_races_v'].values)
    dr_p1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['dr_ft_frst_tot_all_races_v'].values)

    # Graduation completions (total)
    grad_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CTOTALT'].values)
    grad_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CTOTALT'].values)
    grad_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CTOTALT'].values)

    dr_denom = np.nansum([dr_m1, dr_0, dr_p1])
    grad_sum = np.nansum([grad_5, grad_6, grad_7])

    if dr_denom > 0:
        complete_df.at[index, 'PCR_value_doctoral'] = grad_sum / dr_denom

# --- PLOT: PCR Value from Doctoral First-Time Enrollment ---

fig, ax = plt.subplots(figsize=(14, 6))

# Plot per UNITID
for unitid in complete_df['UNITID'].unique():
    subset = complete_df[complete_df['UNITID'] == unitid]
    ax.scatter(subset['Year'], subset['PCR_value_doctoral'], label=f'UNITID {unitid}', alpha=0.5, s=10)

# Average line
avg_PCR_doctoral = complete_df.groupby('Year')['PCR_value_doctoral'].mean()
ax.plot(avg_PCR_doctoral.index, avg_PCR_doctoral.values, color='green', label='Average PCR (Doctoral)', linewidth=2)

# Axis and labels
ax.set_xticks(range(2000, 2024))
ax.set_xticklabels(range(2000, 2024), rotation=45)
ax.set_title('PCR using Doctoral First-Time Enrollment')
ax.set_xlabel('Year')
ax.set_ylabel('PCR Value (Doctoral)')
ax.grid(True)

# Legend outside
ax.legend(
    loc='center left', 
    bbox_to_anchor=(1.05, 0.5),
    fontsize='small',
    ncol=3,
    title='UNITIDs'
)

plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.savefig('/Users/co25936/Desktop/PER/IPEDS/PCR_Value_Doctoral.png')
plt.show()


# --- 3. MASTER'S VS DOCTORAL DEGREE BY GENDER (2017+) ---

# Filter for 2017 and beyond
grad_gender_df = df[(df['Year'] >= 2017)]

# Group by year and sum across institutions
grouped = grad_gender_df.groupby('Year').agg({
    'ma_ft_men_all_races_v': 'sum',
    'ma_ft_wmen_all_races_v': 'sum',
    'dr_ft_men_all_races_v': 'sum',
    'dr_ft_wmen_all_races_v': 'sum'
}).reset_index()

# --- PLOT: Master vs Doctor by Gender ---

fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(grouped['Year'], grouped['ma_ft_men_all_races_v'], label='Masters Men', color='blue', marker='o')
ax.plot(grouped['Year'], grouped['ma_ft_wmen_all_races_v'], label='Masters Women', color='purple', marker='o')
ax.plot(grouped['Year'], grouped['dr_ft_men_all_races_v'], label='Doctoral Men', color='green', marker='x')
ax.plot(grouped['Year'], grouped['dr_ft_wmen_all_races_v'], label='Doctoral Women', color='orange', marker='x')

ax.set_title("Graduate Enrollment by Gender and Degree Level (2017+)")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Students")
ax.legend()
ax.grid(True)

plt.tight_layout()
plt.savefig('/Users/co25936/Desktop/PER/IPEDS/Grad_Enrollment_By_Gender_And_Degree.png')
plt.show()


# --- 4. PCR VALUES FOR RACE ---
# White vs Non-white (separated by graduation rates)

# newer version that might work better (FIXES RACE PCR VALUES BUT CHANGES PREVIOUS PCR VALUES FOR GENDERg)
def safe_extract(arr):
    return arr[0] if len(arr) > 0 and not pd.isna(arr[0]) else 0

complete_df['PCR_value_white'] = np.nan
complete_df['PCR_value_nonwhite'] = np.nan

for index, row in complete_df.iterrows():
    year = row['Year']
    unitid = row['UNITID']

    # White first-time full-time enrollment (3-year window)
    white_m1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_white_v'].values)
    white_0  = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_white_v'].values)
    white_p1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_white_v'].values)

    # Non-White first-time full-time = total - white
    total_m1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_all_races_v'].values)
    total_0  = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_all_races_v'].values)
    total_p1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_all_races_v'].values)

    # Non-white first-time full-time students
    nonwhite_m1 = total_m1 - white_m1 if pd.notna(total_m1) and pd.notna(white_m1) else np.nan
    nonwhite_0  = total_0  - white_0  if pd.notna(total_0)  and pd.notna(white_0)  else np.nan
    nonwhite_p1 = total_p1 - white_p1 if pd.notna(total_p1) and pd.notna(white_p1) else np.nan

    # Graduation totals (separated by White and Non-White)
    grad_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CTOTALT'].values)
    grad_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CTOTALT'].values)
    grad_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CTOTALT'].values)
    grad_total = np.nansum([grad_5, grad_6, grad_7])

    # Denominators (for White and Non-White)
    denom_white = np.nansum([white_m1, white_0, white_p1])
    denom_nonwhite = np.nansum([nonwhite_m1, nonwhite_0, nonwhite_p1])

    # White graduation (using CWHITT + CRACE22_STD)
    grad_white_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CWHITT'].values) + \
                   safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CRACE22_STD'].values)
    grad_white_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CWHITT'].values) + \
                   safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CRACE22_STD'].values)
    grad_white_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CWHITT'].values) + \
                   safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CRACE22_STD'].values)

    # Non-White graduation (using CTOTAL - White graduation)
    grad_nonwhite_5 = grad_5 - grad_white_5
    grad_nonwhite_6 = grad_6 - grad_white_6
    grad_nonwhite_7 = grad_7 - grad_white_7

    # Calculate PCR Values for White and Non-White
    if denom_white > 0:
        complete_df.at[index, 'PCR_value_white'] = np.nansum([grad_white_5, grad_white_6, grad_white_7]) / denom_white

    if denom_nonwhite > 0:
        complete_df.at[index, 'PCR_value_nonwhite'] = np.nansum([grad_nonwhite_5, grad_nonwhite_6, grad_nonwhite_7]) / denom_nonwhite

# --- PLOT: PCR VALUE for White vs Non-White Students --- 
# (CURENT ISSUE SOMETHING ABOUT THE MULITPART LINES IS CAUSING ISSUES see line 486 for example, know bc 2 or more race line works and is 1 line)
fig, ax = plt.subplots(figsize=(14, 6))

# Averages (for 2001 to 2016)
years_to_plot = list(range(2001, 2017))

avg_PCR_white = complete_df.groupby('Year')['PCR_value_white'].mean().loc[years_to_plot]
avg_PCR_nonwhite = complete_df.groupby('Year')['PCR_value_nonwhite'].mean().loc[years_to_plot]

print("white PCR", avg_PCR_white)

ax.plot(avg_PCR_white.index, avg_PCR_white.values, label='White PCR Value', color='green', linewidth=2)
ax.plot(avg_PCR_nonwhite.index, avg_PCR_nonwhite.values, label='Non-White PCR Value', color='orange', linewidth=2)

# Axis and labels
ax.set_xticks(years_to_plot)
ax.set_xticklabels(years_to_plot, rotation=45)
ax.set_title("PCR Value by Racial Group (White vs Non-White) Over Time")
ax.set_xlabel("Year")
ax.set_ylabel("PCR Value")
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.savefig('/Users/co25936/Desktop/PER/IPEDS/PCR_Value_White_vs_NonWhite.png')
plt.show()

# --- PCR VALUE for White + Asian vs Other Races ---
complete_df['PCR_value_white_asian'] = np.nan
complete_df['PCR_value_white'] = np.nan
complete_df['PCR_value_asian'] = np.nan
complete_df['PCR_value_other_races'] = np.nan

for index, row in complete_df.iterrows():
    year = row['Year']
    unitid = row['UNITID']

    # White and Asian first-time full-time enrollment (3-year window)
    white_asian_m1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_white_v'].values) + \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_asian_v'].values)
    white_asian_0  = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_white_v'].values) + \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_asian_v'].values)
    white_asian_p1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_white_v'].values) + \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_asian_v'].values)
    
    # White first-time full-time enrollment (3-year window)
    white_m1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_white_v'].values)
    white_0  = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_white_v'].values)
    white_p1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_white_v'].values)

    # Asian full time enrollment 
    asian_m1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_asian_v'].values)
    asian_0  = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_asian_v'].values)
    asian_p1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_asian_v'].values)

    # Other races first-time full-time = total - white - asian
    total_m1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_all_races_v'].values)
    total_0  = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_all_races_v'].values)
    total_p1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_all_races_v'].values)

    other_races_m1 = total_m1 - white_asian_m1 if pd.notna(total_m1) and pd.notna(white_asian_m1) else np.nan
    other_races_0  = total_0  - white_asian_0  if pd.notna(total_0)  and pd.notna(white_asian_0)  else np.nan
    other_races_p1 = total_p1 - white_asian_p1 if pd.notna(total_p1) and pd.notna(white_asian_p1) else np.nan

    # Graduation totals (White + Asian and Other Races)
    grad_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CTOTALT'].values)
    grad_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CTOTALT'].values)
    grad_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CTOTALT'].values)
    grad_total = np.nansum([grad_5, grad_6, grad_7])

    # White + Asian graduation (CWHITT + CRACE21_STD + CASIAT)
    white_asian_grad_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CWHITT'].values) + \
                         safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CRACE21_STD'].values)+ \
                         safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CRACE22_STD'].values) + \
                         safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CASIAT'].values)

    white_asian_grad_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CWHITT'].values) + \
                         safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CRACE21_STD'].values)+ \
                         safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CRACE22_STD'].values) + \
                         safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CASIAT'].values)

    white_asian_grad_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CWHITT'].values) + \
                         safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CRACE21_STD'].values)+ \
                         safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CRACE22_STD'].values) + \
                         safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CASIAT'].values)
    
    # White graduation (using CWHITT + CRACE22_STD)
    white_grad_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CWHITT'].values) + \
                   safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CRACE22_STD'].values)
    white_grad_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CWHITT'].values) + \
                   safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CRACE22_STD'].values)
    white_grad_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CWHITT'].values) + \
                   safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CRACE22_STD'].values)
    
    #Asian graduation
    asian_grad_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CASIAT'].values) + \
                   safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CRACE21_STD'].values)
    asian_grad_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CASIAT'].values) + \
                   safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CRACE21_STD'].values)
    asian_grad_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CASIAT'].values) + \
                   safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CRACE21_STD'].values)

    # Other Races graduation = total - white_asian graduation
    other_races_grad_5 = grad_5 - white_asian_grad_5
    other_races_grad_6 = grad_6 - white_asian_grad_6
    other_races_grad_7 = grad_7 - white_asian_grad_7

    # Denominators (sum of first-time full-time enrollments)
    denom_white_asian = np.nansum([white_asian_m1, white_asian_0, white_asian_p1])
    denom_white = np.nansum ([white_m1, white_0, white_p1])
    denom_asian = np.nansum([asian_m1, asian_0, asian_p1])
    denom_other_races = np.nansum([other_races_m1, other_races_0, other_races_p1])

    # PCR Values calculation
    if denom_white_asian > 0:
        complete_df.at[index, 'PCR_value_white_asian'] = (white_asian_grad_5 + white_asian_grad_6 + white_asian_grad_7) / denom_white_asian

    if denom_white > 0:
        complete_df.at[index, 'PCR_value_white'] = (white_grad_5 + white_grad_6 + white_grad_7) / denom_white
        
    if denom_asian > 0:
        complete_df.at[index, 'PCR_value_asian'] = (asian_grad_5 + asian_grad_6 + asian_grad_7) / denom_asian

    if denom_other_races > 0:
        complete_df.at[index, 'PCR_value_other_races'] = (other_races_grad_5 + other_races_grad_6 + other_races_grad_7) / denom_other_races

# --- PLOT: PCR VALUE for White + Asian vs Other Races ---
fig, ax = plt.subplots(figsize=(14, 6))

# Averages for White + Asian and Other Races PCR Values (filtered to 2001–2016)
years_to_plot = list(range(2001, 2017))

avg_PCR_white_asian = complete_df.groupby('Year')['PCR_value_white_asian'].mean().loc[years_to_plot]
avg_PCR_other_races = complete_df.groupby('Year')['PCR_value_other_races'].mean().loc[years_to_plot]
avg_PCR_white = complete_df.groupby('Year')['PCR_value_white'].mean().loc[years_to_plot]
avg_PCR_asian = complete_df.groupby('Year')['PCR_value_asian'].mean().loc[years_to_plot]

print("white_asain PCR", avg_PCR_white_asian)

# Plotting PCR Values
#  Line commented out combines Asian and White into a singular line
# ax.plot(avg_PCR_white_asian.index, avg_PCR_white_asian.values, label='White + Asian PCR Value', color='green', linewidth=2)
ax.plot(avg_PCR_white.index, avg_PCR_white.values, label='White PCR Value', color='green', linewidth=2)
ax.plot(avg_PCR_asian.index, avg_PCR_asian.values, label='Asian PCR Value', color='blue', linewidth=2)
ax.plot(avg_PCR_other_races.index, avg_PCR_other_races.values, label='Other Races PCR Value', color='orange', linewidth=2)

# Axis and labels
ax.set_xticks(years_to_plot)
ax.set_xticklabels(years_to_plot, rotation=45)
ax.set_title("PCR Value for White + Asian vs Other Races Over Time")
ax.set_xlabel("Year")
ax.set_ylabel("PCR Value")
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.savefig('/Users/co25936/Desktop/PER/IPEDS/PCR_Value_White_Asian_vs_Other.png')
plt.show()

# --- PCR VALUE for White, Asian, Non-Resident vs Other Races ---
complete_df['PCR_value_white_asian_non'] = np.nan
complete_df['PCR_value_other_groups'] = np.nan

for index, row in complete_df.iterrows():
    year = row['Year']
    unitid = row['UNITID']

    # Define White, Asian, Non-Resident full time enrollment 

    wan_m1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_white_v'].values) + \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_asian_v'].values)+ \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_forgn_v'].values)
    
    wan_0  = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_white_v'].values) + \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_asian_v'].values)+ \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_forgn_v'].values)
    
    wan_p1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_white_v'].values) + \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_asian_v'].values)+ \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_forgn_v'].values)

    
    # Total first-time full-time enrollment (all races)
    total_m1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_all_races_v'].values)
    total_0  = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_all_races_v'].values)
    total_p1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_all_races_v'].values)

    # Other Races = Total - (White + Asian + Non-Resident)
    other_races_m1 = total_m1 - (wan_m1) if pd.notna(total_m1) and pd.notna(wan_m1) else np.nan
    other_races_0  = total_0  - (wan_0) if pd.notna(total_0) and pd.notna(wan_0) else np.nan
    other_races_p1 = total_p1 - (wan_p1) if pd.notna(total_p1) and pd.notna(wan_p1) else np.nan

    # Graduation totals (White, Asian, Non-Resident, Other Races)
    grad_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CTOTALT'].values)
    grad_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CTOTALT'].values)
    grad_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CTOTALT'].values)
    grad_total = np.nansum([grad_5, grad_6, grad_7])

    # Graduation for White, Asian, Non-Resident groups
    white_grad_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CWHITT'].values) + \
                   safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CRACE22_STD'].values)
    white_grad_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CWHITT'].values) + \
                   safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CRACE22_STD'].values)
    white_grad_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CWHITT'].values) + \
                   safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CRACE22_STD'].values)

    asian_grad_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CRACE21_STD'].values) + \
                    safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CASIAT'].values)
    asian_grad_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CRACE21_STD'].values) + \
                    safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CASIAT'].values)
    asian_grad_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CRACE21_STD'].values) + \
                    safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CASIAT'].values)

    non_resident_grad_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CRACE17_STD'].values) + \
                           safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CNRALT'].values)
    non_resident_grad_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CRACE17_STD'].values) + \
                           safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CNRALT'].values)
    non_resident_grad_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CRACE17_STD'].values) + \
                           safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CNRALT'].values)
    
    #combine into one grad
    wan_grad_5 = white_grad_5 + asian_grad_5 + non_resident_grad_5
    wan_grad_6 = white_grad_6 + asian_grad_6 + non_resident_grad_6
    wan_grad_7 = white_grad_7 + asian_grad_7 + non_resident_grad_7

    # Other Races graduation = total - white - asian - non-resident graduation
    other_races_grad_5 = grad_5 - (white_grad_5 + asian_grad_5 + non_resident_grad_5)
    other_races_grad_6 = grad_6 - (white_grad_6 + asian_grad_6 + non_resident_grad_6)
    other_races_grad_7 = grad_7 - (white_grad_7 + asian_grad_7 + non_resident_grad_7)

    # Denominators for each group (sum of first-time full-time enrollments)
    denom_wan = np.nansum([wan_m1, wan_0, wan_p1])
    denom_other = np.nansum([other_races_m1, other_races_0, other_races_p1])

    # PCR Values calculation
    if denom_wan> 0:
        complete_df.at[index, 'PCR_value_white_asian_non'] = (wan_grad_5 + wan_grad_6 + wan_grad_7) / denom_wan 

    if denom_other > 0:
        complete_df.at[index, 'PCR_value_other_groups'] = (other_races_grad_5 + other_races_grad_6 + other_races_grad_7) / denom_other

# --- PLOT: PCR VALUE for White, Asian, Non-Resident vs Other Races ---
fig, ax = plt.subplots(figsize=(14, 6))

# Averages for each group (filtered to 2001–2016)
years_to_plot = list(range(2001, 2017))

avg_PCR_wan = complete_df.groupby('Year')['PCR_value_white_asian_non'].mean().loc[years_to_plot]
avg_PCR_other_groups = complete_df.groupby('Year')['PCR_value_other_groups'].mean().loc[years_to_plot]

print("Whte asain non-resident PCR", avg_PCR_wan)

# Plotting PCR Values
ax.plot(avg_PCR_wan.index, avg_PCR_wan.values, label='White,Asian,Non-resident PCR Value', color='blue', linewidth=2)
ax.plot(avg_PCR_other_groups.index, avg_PCR_other_groups.values, label='Other Races PCR Value', color='orange', linewidth=2)

# Axis and labels
ax.set_xticks(years_to_plot)
ax.set_xticklabels(years_to_plot, rotation=45)
ax.set_title("PCR Value for White, Asian, Non-Resident vs Other Races Over Time")
ax.set_xlabel("Year")
ax.set_ylabel("PCR Value")
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.savefig('/Users/co25936/Desktop/PER/IPEDS/PCR_Value_White_Asian_Non_Resident_vs_Other.png')
plt.show()

# --- PCR VALUE for White, Asian, 2 or More Races, Non-Resident vs Other Races ---
complete_df['PCR_value_white_asian_non-resident_2orMore'] = np.nan
complete_df['PCR_value_other_groups'] = np.nan

for index, row in complete_df.iterrows():
    year = row['Year']
    unitid = row['UNITID']

    # Define White, Asian, 2 or More Races, Non-Resident full time enrollment 
    wan2_m1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_white_v'].values) + \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_asian_v'].values)+ \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_forgn_v'].values)+ \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_multi_v'].values)
    
    wan2_0  = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_white_v'].values) + \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_asian_v'].values)+ \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_forgn_v'].values)+ \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_multi_v'].values)
    
    wan2_p1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_white_v'].values) + \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_asian_v'].values)+ \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_forgn_v'].values)+ \
                     safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_multi_v'].values)
    

    # Total first-time full-time enrollment (all races)
    total_m1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year - 1)]['ft_frst_tot_all_races_v'].values)
    total_0  = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year)]['ft_frst_tot_all_races_v'].values)
    total_p1 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 1)]['ft_frst_tot_all_races_v'].values)

    # Other Races = Total - (White + Asian + 2 or More Races + Non-Resident)
    other_races_m1 = total_m1 - (wan2_m1) if pd.notna(total_m1) else np.nan
    other_races_0  = total_0  - (wan2_0) if pd.notna(total_0) else np.nan
    other_races_p1 = total_p1 - (wan2_p1) if pd.notna(total_p1) else np.nan


    # Graduation for White, Asian, 2 or More Races, Non-Resident groups
    white_grad_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CWHITT'].values) + \
                   safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CRACE22_STD'].values)
    white_grad_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CWHITT'].values) + \
                   safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CRACE22_STD'].values)
    white_grad_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CWHITT'].values) + \
                   safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CRACE22_STD'].values)

    asian_grad_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CRACE21_STD'].values) + \
                    safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CASIAT'].values)
    asian_grad_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CRACE21_STD'].values) + \
                    safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CASIAT'].values)
    asian_grad_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CRACE21_STD'].values) + \
                    safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CASIAT'].values)
    
    non_resident_grad_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CRACE17_STD'].values) + \
                           safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CNRALT'].values)
    non_resident_grad_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CRACE17_STD'].values) + \
                           safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CNRALT'].values)
    non_resident_grad_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CRACE17_STD'].values) + \
                           safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CNRALT'].values)
    
    two_or_more_races_grad_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['C2MORT'].values)
    two_or_more_races_grad_6  = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['C2MORT'].values)
    two_or_more_races_grad_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['C2MORT'].values)

    #combine into one grad
    wan2_grad_5 = white_grad_5 + asian_grad_5 + non_resident_grad_5 + two_or_more_races_grad_5
    wan2_grad_6 = white_grad_6 + asian_grad_6 + non_resident_grad_6 + two_or_more_races_grad_6
    wan2_grad_7 = white_grad_7 + asian_grad_7 + non_resident_grad_7 + two_or_more_races_grad_7

    # Graduation total
    grad_5 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 5)]['CTOTALT'].values)
    grad_6 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 6)]['CTOTALT'].values)
    grad_7 = safe_extract(complete_df[(complete_df['UNITID'] == unitid) & (complete_df['Year'] == year + 7)]['CTOTALT'].values)
    grad_total = np.nansum([grad_5, grad_6, grad_7])
    
    # Other Races graduation = total - white - asian - non-resident graduation - 2 or more
    other_races_grad_5 = grad_5 - (white_grad_5 + asian_grad_5 + non_resident_grad_5 + two_or_more_races_grad_5)
    other_races_grad_6 = grad_6 - (white_grad_6 + asian_grad_6 + non_resident_grad_6 + two_or_more_races_grad_6)
    other_races_grad_7 = grad_7 - (white_grad_7 + asian_grad_7 + non_resident_grad_7 + two_or_more_races_grad_7)

    # Denominators for each group (sum of first-time full-time enrollments)
    denom_wan2 = np.nansum([wan2_m1, wan2_0, wan2_p1])
    denom_other = np.nansum([other_races_m1, other_races_0, other_races_p1,])
    # Calculate PCR Values for each group (e.g., White, Asian, etc.)
    if denom_wan2 > 0:
        complete_df.at[index, 'PCR_value_white_asian_non-resident_2orMore'] = (wan2_grad_5 + wan2_grad_6 + wan2_grad_7) / denom_wan2
    
    if denom_other > 0:
        complete_df.at[index, 'PCR_value_other_groups'] = (other_races_grad_5 + other_races_grad_6 + other_races_grad_7) / denom_other

# --- PLOT: PCR VALUE for White, Asian, 2 or More Races, Non-Resident vs Other Races ---
fig, ax = plt.subplots(figsize=(14, 6))

# Averages for each group (filtered to 2001–2016)
years_to_plot = list(range(2001, 2017))

avg_PCR_wan2 = complete_df.groupby('Year')['PCR_value_white_asian_non-resident_2orMore'].mean().loc[years_to_plot]
avg_PCR_other_groups = complete_df.groupby('Year')['PCR_value_other_groups'].mean().loc[years_to_plot]

print("white asian non-res 2 or more PCR", avg_PCR_wan2)

# Plotting PCR Values
ax.plot(avg_PCR_wan2.index, avg_PCR_wan2.values, label='White,Asian,2 or More races,Non-Resident PCR Value', color='blue', linewidth=2)
ax.plot(avg_PCR_other_groups.index, avg_PCR_other_groups.values, label='Other Races PCR Value', color='orange', linewidth=2)

# Axis and labels
ax.set_xticks(years_to_plot)
ax.set_xticklabels(years_to_plot, rotation=45)
ax.set_title("PCR Value for White, Asian, 2 or More Races, Non-Resident vs Other Races Over Time")
ax.set_xlabel("Year")
ax.set_ylabel("PCR Value")
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.savefig('/Users/co25936/Desktop/PER/IPEDS/PCR_Value_White_Asian_2orMore_Non_Resident_vs_Other.png')
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