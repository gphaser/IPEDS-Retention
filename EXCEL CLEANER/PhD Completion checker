# Get the number of IPEDS and GSS mismatches per year for each year in the data. Note which schools have duplicates or mismatches.
    # Which schools have IPEDS values but not GSS values
    # Which schools have GSS values but not IPEDs
    # Which schools have doubles
        # Keep track of doubles in gss
        # Keep track of doubles in ipeds
    # Calculate the number of schools with all of the given information in a year
        # Total number of unique UNITID’s
    # Make sure to have which schools are the problem in each year as well as what the problem is
        # E.g. 100000 is duplicated in 2008. 1420592 is in IPEDS in 2005 but not GSS
    # Export to an excel file 



import pandas as pd
from pathlib import Path


def analyze_ipeds_gss_mismatches(
    ipeds_file: str = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/IPEDS_combined_file_trimmed_AWLEVEL17.xlsx",
    gss_file: str = "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/GSS_combined_file.xlsx",
    out_path="/Users/co25936/Desktop/PER/IPEDS/ipeds_gss_mismatch_report.xlsx"
) -> str:
    """
    Reads IPEDS and GSS Excel files, checks mismatches/duplicates, 
    and writes a detailed Excel report.
    """

    # --- Load data ---
    df_i = pd.read_excel(ipeds_file)
    df_g = pd.read_excel(gss_file)

    # Make sure keys exist
    for name, df in [("ipeds_file", df_i), ("gss_file", df_g)]:
        if not {"Year", "UNITID"}.issubset(df.columns):
            missing = {"Year", "UNITID"} - set(df.columns)
            raise ValueError(f"{name} missing required columns: {sorted(missing)}")

    # Normalize types (cast UNITID to string, Year to int if possible)
    df_i["UNITID"] = df_i["UNITID"].astype(str).str.strip()
    df_g["UNITID"] = df_g["UNITID"].astype(str).str.strip()
    # If Year has NaNs or non-numeric, keep as-is; otherwise cast to int
    for df in (df_i, df_g):
        try:
            df["Year"] = pd.to_numeric(df["Year"], errors="raise").astype(int)
        except Exception:
            pass  # leave as original if mixed types; grouping still works

    # --- Unique pairs (Year, UNITID) ---
    i_pairs = df_i[["Year", "UNITID"]].drop_duplicates()
    g_pairs = df_g[["Year", "UNITID"]].drop_duplicates()

    # --- Duplicates within each dataset (same Year+UNITID appears multiple times) ---
    def dup_table(df, source):
        dup_mask = df.duplicated(subset=["Year", "UNITID"], keep=False)
        dups = df.loc[dup_mask, ["Year", "UNITID"]].copy()
        if dups.empty:
            return dups.assign(count=0, issue=f"Duplicate in {source}", description="")
        counts = df.groupby(["Year", "UNITID"]).size().rename("count").reset_index()
        counts = counts[counts["count"] > 1]
        counts["issue"] = f"Duplicate in {source}"
        counts["description"] = counts.apply(
            lambda r: f"{r.UNITID} is duplicated in {source} in {r.Year} ({r['count']} rows)", axis=1
        )
        return counts.sort_values(["Year", "UNITID"])

    ipeds_dupes = dup_table(df_i, "IPEDS")
    gss_dupes   = dup_table(df_g, "GSS")

    # Count duplicate pairs per year (not rows)
    ipeds_dupe_pairs_per_year = (
        ipeds_dupes.groupby("Year").size().rename("ipeds_dupe_pairs").reset_index()
        if not ipeds_dupes.empty else pd.DataFrame(columns=["Year", "ipeds_dupe_pairs"])
    )
    gss_dupe_pairs_per_year = (
        gss_dupes.groupby("Year").size().rename("gss_dupe_pairs").reset_index()
        if not gss_dupes.empty else pd.DataFrame(columns=["Year", "gss_dupe_pairs"])
    )

    # --- Outer merge to locate membership mismatches ---
    merged_pairs = i_pairs.merge(g_pairs, on=["Year", "UNITID"], how="outer", indicator=True)

    only_in_ipeds = merged_pairs[merged_pairs["_merge"] == "left_only"].copy()
    only_in_gss   = merged_pairs[merged_pairs["_merge"] == "right_only"].copy()
    in_both       = merged_pairs[merged_pairs["_merge"] == "both"].copy()

    only_in_ipeds["issue"] = "In IPEDS only"
    only_in_ipeds["description"] = only_in_ipeds.apply(
        lambda r: f"{r.UNITID} is in IPEDS in {r.Year} but not GSS", axis=1
    )
    only_in_gss["issue"] = "In GSS only"
    only_in_gss["description"] = only_in_gss.apply(
        lambda r: f"{r.UNITID} is in GSS in {r.Year} but not IPEDS", axis=1
    )

    # --- Per-year summary counts ---
    def per_year_counts(pairs, label):
        return pairs.groupby("Year")["UNITID"].nunique().rename(f"{label}_unique_schools").reset_index()

    i_counts = per_year_counts(i_pairs, "ipeds")
    g_counts = per_year_counts(g_pairs, "gss")
    in_both_counts = in_both.groupby("Year")["UNITID"].nunique().rename("complete_overlap").reset_index()

    only_i_counts = only_in_ipeds.groupby("Year")["UNITID"].nunique().rename("only_in_ipeds").reset_index()
    only_g_counts = only_in_gss.groupby("Year")["UNITID"].nunique().rename("only_in_gss").reset_index()

    # Combine per-year metrics
    years = pd.concat([i_counts["Year"], g_counts["Year"]]).drop_duplicates().sort_values()
    summary = pd.DataFrame({"Year": years})
    for piece in [i_counts, g_counts, in_both_counts, only_i_counts, only_g_counts,
                  ipeds_dupe_pairs_per_year, gss_dupe_pairs_per_year]:
        summary = summary.merge(piece, on="Year", how="left")

    # Fill NaNs with zeros where appropriate
    count_cols = [c for c in summary.columns if c != "Year"]
    summary[count_cols] = summary[count_cols].fillna(0).astype(int)

    # Add a convenience column for “mismatch pairs” (membership + duplicate pairs)
    summary["membership_mismatches"] = summary["only_in_ipeds"] + summary["only_in_gss"]
    summary["duplicate_pairs_total"] = summary.get("ipeds_dupe_pairs", 0) + summary.get("gss_dupe_pairs", 0)

    # --- Detailed issues table (all problems with readable messages) ---
    issues_detail = pd.concat([
        only_in_ipeds[["Year", "UNITID", "issue", "description"]],
        only_in_gss[["Year", "UNITID", "issue", "description"]],
        ipeds_dupes[["Year", "UNITID", "issue", "description"]],
        gss_dupes[["Year", "UNITID", "issue", "description"]],
    ], ignore_index=True).sort_values(["Year", "UNITID", "issue"])

    # --- Schools with all info in a given year (intersection) ---
    complete_schools_by_year = in_both.sort_values(["Year", "UNITID"])[["Year", "UNITID"]]

    # --- Export to Excel ---
    out_path = str(Path(out_path))
    with pd.ExcelWriter(out_path, engine="xlsxwriter") as xw:
        summary.to_excel(xw, index=False, sheet_name="per_year_summary")
        issues_detail.to_excel(xw, index=False, sheet_name="issues_detail")
        complete_schools_by_year.to_excel(xw, index=False, sheet_name="complete_schools_by_year")
        only_in_ipeds[["Year", "UNITID", "issue"]].to_excel(xw, index=False, sheet_name="only_in_ipeds")
        only_in_gss[["Year", "UNITID", "issue"]].to_excel(xw, index=False, sheet_name="only_in_gss")
        ipeds_dupes.to_excel(xw, index=False, sheet_name="ipeds_dupes")
        gss_dupes.to_excel(xw, index=False, sheet_name="gss_dupes")

    return out_path


report_path = analyze_ipeds_gss_mismatches(
    ipeds_file="/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/IPEDS_combined_file_trimmed_AWLEVEL17.xlsx",
    gss_file="/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/GSS_combined_file.xlsx",
    out_path="/Users/co25936/Desktop/PER/IPEDS/ipeds_gss_mismatch_report.xlsx"
)

print(f"Excel report written to: {report_path}")
