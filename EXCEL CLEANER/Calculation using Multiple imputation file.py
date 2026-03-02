# want to use the file /Users/co25936/Desktop/PER/IPEDS/PRC_National_dataset.xlsx to calculate PCR and RR from  the excel file
# PCR is calculated as         
#PCR(year) = [phd_awarded(year+5) + phd_awarded(year+6) + phd_awarded(year+7)] / [first_year(year-1) + first_year(year) + first_year(year+1)]
# RR
#Retention(year) = [enrolled(year) +  phd_awarded(year) - first_year(year)] / enrolled(year-1)]
# We need to only do this for sets of years where all the data is availbe ie no NAN's 
# need to do it for each set of degree, sex, and  race combos
    # Degree enrolled in is ALL, PhD or Masters
    # Sex enrolled is All, male, female
    # Race is All, White, Asian, Black, Hispanic,Unknown,Two or More,Pacific Islander, Foreign
#Create an excel file titled "PCR and RR calculated from Mult. Imp."


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# =========================
# CONFIG
# =========================
input_file = "/Users/co25936/Desktop/PER/IPEDS/PRC_National_dataset.xlsx"
output_file = "/Users/co25936/Desktop/PER/IPEDS/PCR and RR calculated from Mult. Imp.xlsx"
plot_dir = "/Users/co25936/Desktop/PER/IPEDS/PCR_RR_Scatter_Plots"

COL_YEAR = "year"
COL_DEGREE = "degree enrolled in"
COL_SEX = "sex"
COL_RACE = "race"
COL_FIRST_YEAR = "first_year"
COL_ENROLLED = "enrolled"
COL_PHD_AWARDED = "phd_awarded"

# LOAD DATA

df = pd.read_excel(input_file)

# Ensure sorted for time-based calculations
df = df.sort_values(
    by=[COL_DEGREE, COL_SEX, COL_RACE, COL_YEAR]
).reset_index(drop=True)

results = []


# GROUPED CALCULATIONS

group_cols = [COL_DEGREE, COL_SEX, COL_RACE]

for group_keys, g in df.groupby(group_cols):
    g = g.sort_values(COL_YEAR).reset_index(drop=True)

    years = g[COL_YEAR].values

    for i in range(len(g)):
        year = years[i]

        # ---------- PCR ----------
        try:
            fy_vals = g.loc[
                g[COL_YEAR].isin([year - 1, year, year + 1]),
                COL_FIRST_YEAR
            ]
            phd_vals = g.loc[
                g[COL_YEAR].isin([year + 5, year + 6, year + 7]),
                COL_PHD_AWARDED
            ]

            if (
                len(fy_vals) == 3 and
                len(phd_vals) == 3 and
                fy_vals.notna().all() and
                phd_vals.notna().all()and
                fy_vals.sum() > 0 
            ):
                pcr = phd_vals.sum() / fy_vals.sum()
            else:
                pcr = np.nan
        except Exception:
            pcr = np.nan

        # ---------- RR ----------
        try:
            row_curr = g[g[COL_YEAR] == year]
            row_prev = g[g[COL_YEAR] == year - 1]

            if (
                not row_curr.empty and
                not row_prev.empty and
                row_curr[[COL_ENROLLED, COL_PHD_AWARDED, COL_FIRST_YEAR]].notna().all(axis=None) and
                row_prev[[COL_ENROLLED]].notna().all(axis=None)
            ):
                denom = row_prev[COL_ENROLLED].values[0]

                        # NEW RULE: blank RR if denominator is 0
                if denom == 0:
                    rr = np.nan
                else:
                    rr = (row_curr[COL_ENROLLED].values[0] + row_curr[COL_PHD_AWARDED].values[0]- row_curr[COL_FIRST_YEAR].values[0]) / denom
            else:
                rr = np.nan
        except Exception:
            rr = np.nan

        results.append({
            COL_DEGREE: group_keys[0],
            COL_SEX: group_keys[1],
            COL_RACE: group_keys[2],
            COL_YEAR: year,
            "PCR": pcr,
            "RR": rr
        })


# SAVE EXCEL

result_df = pd.DataFrame(results)
result_df = result_df.dropna(subset=["PCR", "RR"], how="all")
result_df.to_excel(output_file, index=False)


#==================================================
# PCR plots
#===================================================

pcr_sexes = ["All", "Men", "Women"]

for sex_filter in pcr_sexes:

    # ---- determine groups for THIS figure ----
    plot_groups = [
        (degree, sex, race)
        for (degree, sex, race), g in result_df.groupby([COL_DEGREE, COL_SEX, COL_RACE])
        if sex == sex_filter and g["PCR"].notna().sum() >= 2
    ]

    if not plot_groups:
        continue

    cmap = plt.cm.tab10
    colors = cmap(np.linspace(0, 1, len(plot_groups)))
    group_color_map = dict(zip(plot_groups, colors))

    plt.figure(figsize=(12, 8))

    for (degree, sex, race) in plot_groups:
        g = result_df[
            (result_df[COL_DEGREE] == degree) &
            (result_df[COL_SEX] == sex) &
            (result_df[COL_RACE] == race)
        ].sort_values(COL_YEAR)

        g_pcr = g.dropna(subset=["PCR"])

        if len(g_pcr) >= 2:
            plt.plot(
                g_pcr[COL_YEAR],
                g_pcr["PCR"],
                color=group_color_map[(degree, sex, race)],
                marker="o",
                linewidth=1,
                alpha=0.85,
                label=f"{degree} | {race}"
            )

    plt.xlabel("Year")
    plt.ylabel("PCR")
    plt.title(f"PCR by Year — Sex: {sex_filter}")
    plt.xlim(2010, 2017)
    plt.xticks(range(2011, 2017))
    plt.legend(fontsize=6, ncol=3, frameon=False)
    plt.tight_layout()

    filename = f"PCR_Sex_{sex_filter}.png".replace(" ", "_")
    plt.savefig(os.path.join(plot_dir, filename), bbox_inches="tight")
    plt.close()

#==================================================
# RR plots
#===================================================

rr_degrees = ["All", "PhD"]
rr_sexes = ["All", "Men", "Women"]

for degree_filter in rr_degrees:
    for sex_filter in rr_sexes:

        plot_groups = [
            (degree, sex, race)
            for (degree, sex, race), g in result_df.groupby([COL_DEGREE, COL_SEX, COL_RACE])
            if degree == degree_filter and sex == sex_filter and g["RR"].notna().sum() >= 2
        ]

        if not plot_groups:
            continue

        cmap = plt.cm.tab20
        colors = cmap(np.linspace(0, 1, len(plot_groups)))
        group_color_map = dict(zip(plot_groups, colors))

        plt.figure(figsize=(12, 8))

        for (degree, sex, race) in plot_groups:
            g = result_df[
                (result_df[COL_DEGREE] == degree) &
                (result_df[COL_SEX] == sex) &
                (result_df[COL_RACE] == race)
            ].sort_values(COL_YEAR)

            g_rr = g.dropna(subset=["RR"])

            if len(g_rr) >= 2:
                plt.plot(
                    g_rr[COL_YEAR],
                    g_rr["RR"],
                    color=group_color_map[(degree, sex, race)],
                    marker="o",
                    linewidth=1,
                    alpha=0.85,
                    label=race
                )

        plt.xlabel("Year")
        plt.ylabel("RR")
        plt.title(f"RR by Year — Degree: {degree_filter} | Sex: {sex_filter}")
        plt.xlim(2010, 2024)
        plt.xticks(range(2011, 2024))
        plt.legend(fontsize=6, ncol=3, frameon=False)
        plt.tight_layout()

        filename = f"RR_{degree_filter}_Sex_{sex_filter}.png".replace(" ", "_")
        plt.savefig(os.path.join(plot_dir, filename), bbox_inches="tight")
        plt.close()



'''
groups = list(result_df.groupby([COL_DEGREE, COL_SEX, COL_RACE]).groups.keys())
cmap = plt.cm.tab20
colors = cmap(np.linspace(0, 1, len(groups)))
group_color_map = dict(zip(groups, colors))



os.makedirs(plot_dir, exist_ok=True)

# ---------- PCR graphs ----------
pcr_sexes = ["All", "Men", "Women"]

for sex_filter in pcr_sexes:

    plt.figure(figsize=(12, 8))

    for (degree, sex, race), g in result_df.groupby([COL_DEGREE, COL_SEX, COL_RACE]):

        if sex != sex_filter:
            continue

        g_pcr = g.dropna(subset=["PCR"]).sort_values(COL_YEAR)

        if len(g_pcr) >= 2:
            plt.plot(
                g_pcr[COL_YEAR],
                g_pcr["PCR"],
                color=group_color_map[(degree, sex, race)],
                marker="o",
                linewidth=1,
                alpha=0.85,
                label=f"{degree} | {race}"
            )

    plt.xlabel("Year")
    plt.ylabel("PCR")
    plt.title(f"PCR by Year — Sex: {sex_filter}")
    plt.xlim(2010, 2017)
    plt.xticks(range(2011, 2017))
    plt.legend(fontsize=6, ncol=3, frameon=False)
    plt.tight_layout()

    filename = f"PCR_Sex_{sex_filter}.png".replace(" ", "_")
    plt.savefig(os.path.join(plot_dir, filename), bbox_inches="tight")
    plt.close()



# ---------- RR: single plot ----------
rr_degrees = ["All", "PhD"]
rr_sexes = ["All", "Men", "Women"]

for degree_filter in rr_degrees:
    for sex_filter in rr_sexes:

        plt.figure(figsize=(12, 8))

        for (degree, sex, race), g in result_df.groupby([COL_DEGREE, COL_SEX, COL_RACE]):

            if degree != degree_filter or sex != sex_filter:
                continue

            g_rr = g.dropna(subset=["RR"]).sort_values(COL_YEAR)

            if len(g_rr) >= 2:
                plt.plot(
                    g_rr[COL_YEAR],
                    g_rr["RR"],
                    color=group_color_map[(degree, sex, race)],
                    marker="o",
                    linewidth=1,
                    alpha=0.85,
                    label=race
                )

        plt.xlabel("Year")
        plt.ylabel("RR")
        plt.title(f"RR by Year — Degree: {degree_filter} | Sex: {sex_filter}")
        plt.xlim(2010, 2024)
        plt.xticks(range(2011, 2024))
        plt.legend(fontsize=6, ncol=3, frameon=False)
        plt.tight_layout()

        filename = f"RR_{degree_filter}_Sex_{sex_filter}.png".replace(" ", "_")
        plt.savefig(os.path.join(plot_dir, filename), bbox_inches="tight")
        plt.close()

'''

print("✅ Excel file created:")
print(output_file)
print("📈 Combined PCR and RR plots created in:")
print(plot_dir)













''' OLD VERSION
# TIME-SERIES PLOTS 

# THIS WORKS BUT GRAPHS NEED WORK! cleaned up a bit but still needs analysis

os.makedirs(plot_dir, exist_ok=True)

for (degree, sex, race), g in result_df.groupby([COL_DEGREE, COL_SEX, COL_RACE]):

    # ---------- PCR vs Year ----------
    g_pcr = g.dropna(subset=["PCR"])
    if len(g_pcr) >= 2:
        plt.figure()
        plt.scatter(g_pcr[COL_YEAR], g_pcr["PCR"])
        plt.xlabel("Year")
        plt.ylabel("PCR")
        plt.title(f"PCR by Year\nDegree: {degree} | Sex: {sex} | Race: {race}")

        plt.xlim(2010, 2017)
        plt.xticks(range(2011, 2017))

        filename = f"PCR_{degree}_{sex}_{race}.png".replace(" ", "_")
        plt.savefig(os.path.join(plot_dir, filename), bbox_inches="tight")
        plt.close()

    # ---------- RR vs Year ----------
    g_rr = g.dropna(subset=["RR"])
    if len(g_rr) >= 2:
        plt.figure()
        plt.scatter(g_rr[COL_YEAR], g_rr["RR"])
        plt.xlabel("Year")
        plt.ylabel("RR")
        plt.tick_params(axis="x", labelsize=8, length=6, width=1.2)
        plt.title(f"RR by Year\nDegree: {degree} | Sex: {sex} | Race: {race}")

        plt.xlim(2010, 2024)
        plt.xticks(range(2011, 2024))

        filename = f"RR_{degree}_{sex}_{race}.png".replace(" ", "_")
        plt.savefig(os.path.join(plot_dir, filename), bbox_inches="tight")
        plt.close()


print("✅ Excel file created:")
print(output_file)
print("\n📊 Scatter plots saved to:")
print(plot_dir)
'''

