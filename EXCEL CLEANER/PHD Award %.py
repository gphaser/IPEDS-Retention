#PHD Award %
# PHD Award %
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the Excel file
file_path = '/Users/co25936/Desktop/PER/IPEDS/GSS_IPEDS_Combined_file.xlsx'  # Replace with your actual file path
data = pd.read_excel(file_path)

# Define the range for x
x = 0  # You can adjust this value as needed (SHOULD BE 0 and 1)

# List of UNITIDs to process
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

# Initialize a list to store results
results = []

# Iterate over each UNITID in the specified list
for unitid in unitid_list:
    # Filter data for the current university and AWLEVEL = 17
    university_data = data[(data['UNITID'] == unitid) & (data['AWLEVEL'] == 17)]
    
    # Iterate over each year from 2000 to 2023
    for year in range(2000, 2024):
        # Get the relevant rows for the current year and the range defined by x
        relevant_years = university_data[(university_data['Year'] >= year - x) & 
                                          (university_data['Year'] <= year + x)]
        
        # Calculate the numerator (P_n) and denominator (F_n)
        numerator = relevant_years['CTOTALT'].sum()  # P_n using CTOTALT
        denominator = relevant_years['ft_frst_tot_all_races_v'].sum()  # F_n
        
        # Avoid division by zero
        if denominator != 0:
            pa_value = numerator / denominator
            
            # Calculate T_n and T_{n+1}
            T_n = relevant_years['ft_tot_all_races_v'].sum()  # Replace with the actual column name for T_n
            T_n_plus_1 = university_data[university_data['Year'] == year + 1]['ft_tot_all_races_v'].sum()  # Replace with the actual column name for T_{n+1}
            F_n_plus_1 = university_data[university_data['Year'] == year + 1]['ft_frst_tot_all_races_v'].sum()  # F_{n+1}
            
            # Calculate R_n
            if T_n != 0:  # Avoid division by zero
                retention_value = (T_n_plus_1 + numerator - F_n_plus_1) / T_n
            else:
                retention_value = None  # or some default value
            
            years_used = list(range(year, year + 7))  # Years used from selected year to year + 6
            results.append({
                'UNITID': unitid,
                'Year': year,
                'PA_Value': pa_value,
                'Retention_Value': retention_value,  # Add retention value to results
                'Years_Used': years_used
            })

# Convert results to a DataFrame
results_df = pd.DataFrame(results)

# Remove rows with empty PA values or retention values
results_df = results_df.dropna(subset=['PA_Value', 'Retention_Value'])

# Define the output directory
output_dir = '/Users/co25936/Desktop/PER/IPEDS'
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Save the results to a new Excel file
results_file_path = os.path.join(output_dir, 'pa_results.xlsx')
results_df.to_excel(results_file_path, index=False)

# Plotting the dot graph for each university
plt.figure(figsize=(10, 5))  # Adjusted figure size
for unitid in results_df['UNITID'].unique():
    university_results = results_df[results_df['UNITID'] == unitid]
    plt.scatter(university_results['Year'], university_results['PA_Value'], label=f'University {unitid}', alpha=0.7)

plt.title('Dot Plot of PA Values by University')
plt.xlabel('Year')
plt.ylabel('PA Value')
plt.xticks(range(2000, 2024))  # Set x-ticks for each year
plt.grid()

# Add the legend to the plot
plt.legend(title='University UNITID', bbox_to_anchor=(0, 1.2), loc='upper left')  # Adjust the position as needed

# Save the dot plot as a PNG file
dot_plot_file_path = os.path.join(output_dir, 'pa_dot_plot.png')
plt.savefig(dot_plot_file_path, bbox_inches='tight')  # Use bbox_inches='tight' to fit the plot
plt.show()

print(f"Calculation complete. Results saved to '{results_file_path}' and dot plot saved as '{dot_plot_file_path}'.")

