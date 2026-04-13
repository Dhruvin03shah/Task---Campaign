import math
import pandas as pd

def compute_relevance_score(df, selected_niches):
    """Score each creator 0–100 based on niche match + engagement + followers."""
    scores = []
    for _, row in df.iterrows():
        score = 0

        # Niche match — up to 50 pts
        if row["Primary_Niche"] in selected_niches:
            score += 50
        elif row["Secondary_Niche"] in selected_niches:
            score += 25

        # Engagement rate — up to 30 pts (normalized against 7% ceiling)
        score += min(row["Engagement_Rate_%"] / 7.0, 1.0) * 30

        # Followers — up to 20 pts (log-normalized against 250k)
        followers = max(row["Followers"], 1)
        score += min(math.log10(followers) / math.log10(250000), 1.0) * 20

        scores.append(round(score, 1))

    df = df.copy()
    df["Relevance_Score"] = scores
    return df

def tier_label(score):
    if score >= 70:
        return "🔥 Top Pick"
    elif score >= 40:
        return "👍 Good Fit"
    else:
        return "🔍 Possible"