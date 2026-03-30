# IPEDS_Excel_Trimmer
import os
import pandas as pd

folder_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/Untrimmed IPEDS/"
output_path = '/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/Trimmed/'


def filter_existing_columns(df, selected_columns, filename):
    existing_columns = [col for col in selected_columns if col in df.columns]
    missing_columns = [col for col in selected_columns if col not in df.columns]

    if missing_columns:
        print(f"Warning: Missing columns in {filename}: {missing_columns}")
    
    return df[existing_columns] if existing_columns else pd.DataFrame()



# --------- Pre-2008 ---------
for year in range(2000, 2009):
    filename = f"{folder_path}c{year}_a.xlsx"
    
    if os.path.exists(filename):
        df = pd.read_excel(filename)
        df.columns = (
        df.columns
        .astype(str)
        .str.strip()          # remove leading/trailing whitespace
        .str.replace('\u00a0', '', regex=False)  # remove non-breaking spaces
        )
        df.columns = df.columns.str.lower() # makes all columns lowercase 

        selected_columns = ["unitid", "cipcode", "ctotalt", "awlevel", "ctotalm", "ctotalw", "crace15", "crace16",
                            # Racial breakdown, Black, Asian/Pacific islander, Hispanic, White, Unknown, Non-residental alien, Native American/Alaskin 
                            "crace18", "crace20","crace21", "crace22", 'crace17', 'crace19',
                            # Other racial breakdowns Black, Aisan, Native Hawian/Pacific islander Hispanic/Latino., White, Unknown is the same, 2 or more races, non-american students
                            "cbkaat","casiat","cnhpit", "chispt", "cwhitt", "c2mort", "cnralt",
                            # Sex breakdown
                            "cbkaam","casiam","cnhpim", "chispm", "cwhitm","cunknm", "c2morm", "cnralm",
                            "cbkaaw","casiaw","cnhpiw", "chispw", "cwhitw","cunknw", "c2morw", "cnralw",
                            # Major number (either 1st or 2nd major)
                            'majornum',
                            ]

        df_filtered = filter_existing_columns(df, selected_columns, filename)

        # Only proceed if df_filtered is not empty and has required columns
        if not df_filtered.empty and "cipcode" in df_filtered.columns and "awlevel" in df_filtered.columns:
            count = df['cipcode'].astype(str).str.startswith('40.08').sum()
            print(f"{year} - starts with 40.08: {count}")

            count_general = df['cipcode'].astype(str).str.startswith('40.0801').sum()
            print(f"{year} - starts with 40.0801: {count_general}")

            df_filtered = df_filtered[
                (df_filtered["cipcode"] == 40.0801) &
                (df_filtered["awlevel"].isin([7, 9, 11, 17]))
            ]

            df_filtered["year"] = year

            output_filename = f"{output_path}c{year}_trimmed_file.xlsx"
            df_filtered.to_excel(output_filename, index=False)
            print(f"Saved: {output_filename}")
        else:
            print(f"Skipped {filename} due to missing key columns.")
    else:
        print(f"File not found: {filename}, skipping.")


# --------- 2009 and after ---------
for year in range(2009, 2024):
    filename = f"{folder_path}c{year}_a.xlsx"
    
    if os.path.exists(filename):
        df = pd.read_excel(filename)
        df.columns = (
        df.columns
        .astype(str)
        .str.strip()          # remove leading/trailing whitespace
        .str.replace('\u00a0', '', regex=False)  # remove non-breaking spaces
        )
        df.columns = df.columns.str.lower() # makes all columns lowercase 


        print("RAW COLUMN NAMES:")
        for col in df.columns:
             print(repr(col))

        selected_columns = ["unitid", "cipcode", "ctotalt", "awlevel", "ctotalm", "ctotalw", 
                            # Racial breakdown, Black, Asian/Pacific islander, Hispanic, White, Unknown, Non-residental alien, Native American/Alaskin 
                            "crace18", "crace20","crace21", "crace22", "cunknt", "crace17", "crace19",
                            # Other racial breakdowns Black, Aisan, Native Hawian/Pacific islander Hispanic/Latino., White (Unknown is the same),  2 or more races, non-american students
                            "cbkaat","casiat","cnhpit", "chispt", "cwhitt", "c2mort", "cnralt",
                            # Sex breakdown
                            "cbkaam","casiam","cnhpim", "chispm", "cwhitm","cunknm", "c2morm", "cnralm",
                            "cbkaaw","casiaw","cnhpiw", "chispw", "cwhitw","cunknw", "c2morw", "cnralw",
                            # Major number (either 1st or 2nd major)
                            'majornum',
                            ]
        df_filtered = filter_existing_columns(df, selected_columns, filename)

        if not df_filtered.empty and "cipcode" in df_filtered.columns and "awlevel" in df_filtered.columns:
            count = df['cipcode'].astype(str).str.startswith('40.08').sum()
            print(f"{year} - starts with 40.08: {count}")

            count_general = df['cipcode'].astype(str).str.startswith('40.0801').sum()
            print(f"{year} - starts with 40.0801: {count_general}")

            df_filtered = df_filtered[
                (df_filtered["cipcode"] == 40.0801) &
                (df_filtered["awlevel"].isin([7,9,17]))
            ]

            df_filtered["year"] = year

            output_filename = f"{output_path}c{year}_trimmed_file.xlsx"
            df_filtered.to_excel(output_filename, index=False)
            print(f"Saved: {output_filename}")
        else:
            print(f"Skipped {filename} due to missing key columns.")
    else:
        print(f"File not found: {filename}, skipping.")




'''
#IPEDS_Excel_Trimmer
import os
import pandas as pd

folder_path = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/"  # Ensure path is correctly formatted

for year in range(2000, 2008):
    filename = f"{folder_path}c{year}_a.xlsx"  # Construct full file path
    
    if os.path.exists(filename):  # Check if file exists
        df = pd.read_excel(filename)  # Read the Excel file
        
        # Select specific columns
        selected_columns = ["UNITID", "CIPCODE", "CTOTALT", "AWLEVEL", 
                            "crace15", "crace16", "CRACE15", "CRACE16", "CTOTALM", "CTOTALW"]
        df_filtered = df[selected_columns]  # Keep only selected columns

        # Filter for rows where 'CIP Code' is 40.0801 and Award Level is 7 (Masters) or 17 (PHD)
        # Pre 2008 cold be called 1st Profesional degree ad had a AWLEVEL OF 11 
        # PRE 2008 Doctor degree had a AWLEVL of 9
        # Code added to include dgreesed eared for both men and women including both variations

        count = df['CIPCODE'].astype(str).str.startswith('40.08').sum()
        print(count)

        count_general = df['CIPCODE'].astype(str).str.startswith('40.0801').sum()
        print(count_general)

        df_filtered = df_filtered[(df_filtered["CIPCODE"] == 40.0801) & (df_filtered["AWLEVEL"].isin([7, 9]))]

        # Add a new column for the year
        df_filtered['Year'] = year


        # Save the trimmed file
        output_filename = f"{folder_path}c{year}_trimmed_file.xlsx"
        df_filtered.to_excel(output_filename, index=False)

        print(f"Saved: {output_filename}")
    else:
        print(f"File not found: {filename}, skipping.")




for year in range(2009, 2024):
    filename = f"{folder_path}c{year}_a.xlsx"  # Construct full file path
    
    if os.path.exists(filename):  # Check if file exists
        df = pd.read_excel(filename)  # Read the Excel file
        
        # Select specific columns
        selected_columns = ["UNITID", "CIPCODE", "CTOTALT", "AWLEVEL", 
                            "CTOTALM", "CTOTALW"]
        df_filtered = df[selected_columns]  # Keep only selected columns

        # Filter for rows where 'CIP Code' is 40.0801 and Award Level is 7 (Masters) or 17 (PHD)
        # Pre 2008 cold be called 1st Profesional degree ad had a AWLEVEL OF 11 

        count = df['CIPCODE'].astype(str).str.startswith('40.08').sum()
        print(count)

        count_general = df['CIPCODE'].astype(str).str.startswith('40.0801').sum()
        print(count_general)

        df_filtered = df_filtered[(df_filtered["CIPCODE"] == 40.0801) & (df_filtered["AWLEVEL"].isin([7, 17]))]

        # Add a new column for the year
        df_filtered['Year'] = year


        # Save the trimmed file
        output_filename = f"{folder_path}c{year}_trimmed_file.xlsx"
        df_filtered.to_excel(output_filename, index=False)

        print(f"Saved: {output_filename}")
    else:
        print(f"File not found: {filename}, skipping.")
'''