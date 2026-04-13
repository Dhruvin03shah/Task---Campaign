from utils.scoring import compute_relevance_score, tier_label

def filter_by_niches(df, selected_niches):
    """Return all creators matching any selected niche, scored and sorted."""
    if not selected_niches:
        return df.copy()
    mask = (
        df["Primary_Niche"].isin(selected_niches) |
        df["Secondary_Niche"].isin(selected_niches)
    )
    result = df[mask].copy()
    result = compute_relevance_score(result, selected_niches)
    result["Tier"] = result["Relevance_Score"].apply(tier_label)
    return result.sort_values("Relevance_Score", ascending=False)

def get_recommended_creators(df, selected_niches, top_n=5):
    """Return top N creators for given niches."""
    filtered = filter_by_niches(df, selected_niches)
    return filtered.head(top_n) if top_n else filtered