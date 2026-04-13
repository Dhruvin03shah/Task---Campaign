import pandas as pd

def load_and_clean(path="data/AI_Assignment.xlsx"):
    df = pd.read_excel(path)

    # Standardize column names
    df.columns = [c.strip().replace(" ", "_") for c in df.columns]

    # Fill missing contact numbers
    df["Contact_Number"] = df["Contact_Number"].replace("", "N/A").fillna("N/A")

    # Normalize niche columns
    df["Primary_Niche"] = df["Primary_Niche"].str.strip().str.title()
    df["Secondary_Niche"] = df["Secondary_Niche"].str.strip().str.title()

    # Ensure numeric types
    df["Followers"] = pd.to_numeric(df["Followers"], errors="coerce").fillna(0).astype(int)
    df["Engagement_Rate_%"] = pd.to_numeric(df["Engagement_Rate_%"], errors="coerce").fillna(0.0)
    df["Avg_Views"] = pd.to_numeric(df["Avg_Views"], errors="coerce").fillna(0).astype(int)
    df["Cost_Per_Post"] = pd.to_numeric(df["Cost_Per_Post"], errors="coerce").fillna(0).astype(int)

    # Flag incomplete profiles
    df["Profile_Complete"] = df.apply(_check_completeness, axis=1)

    return df

def _check_completeness(row):
    missing = []
    if pd.isna(row["Contact_Email"]) or str(row["Contact_Email"]).strip() == "":
        missing.append("Email")
    if str(row.get("Contact_Number", "")).strip() in ["N/A", "", "nan"]:
        missing.append("Phone")
    if row["Followers"] == 0:
        missing.append("Followers")
    return "✅ Complete" if not missing else f"⚠️ Missing: {', '.join(missing)}"

def get_all_niches(df):
    niches = set(df["Primary_Niche"].dropna().tolist()) | set(df["Secondary_Niche"].dropna().tolist())
    return sorted(niches)