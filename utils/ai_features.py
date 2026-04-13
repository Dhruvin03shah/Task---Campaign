import requests
import json

ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"

def _call_claude(prompt, max_tokens=500):
    response = requests.post(
        ANTHROPIC_API_URL,
        headers={"Content-Type": "application/json"},
        json={
            "model": "claude-sonnet-4-20250514",
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}],
        },
    )
    data = response.json()
    return data["content"][0]["text"].strip()


def auto_tag_niches(creator_row):
    """Use Claude to suggest niche tags based on creator profile."""
    prompt = f"""
You are a marketing analyst. Based on this influencer profile, suggest the top 2 niche tags.
Name: {creator_row['Name']}
Platform: {creator_row['Platform']}
Primary Niche: {creator_row['Primary_Niche']}
Secondary Niche: {creator_row['Secondary_Niche']}
City: {creator_row['City']}

Reply ONLY as JSON: {{"tags": ["Tag1", "Tag2"]}}
No explanation, no markdown.
"""
    try:
        result = _call_claude(prompt, max_tokens=100)
        return json.loads(result).get("tags", [])
    except Exception:
        return [creator_row["Primary_Niche"], creator_row["Secondary_Niche"]]


def recommend_creators_ai(creators_df, campaign_name, niches):
    """Use Claude to pick and explain the top 3 creators for a campaign."""
    summary = "\n".join([
        f"- {row['Name']} | {row['Platform']} | {row['Primary_Niche']}/{row['Secondary_Niche']} | "
        f"{row['Followers']:,} followers | {row['Engagement_Rate_%']}% engagement | ₹{row['Cost_Per_Post']:,}/post"
        for _, row in creators_df.iterrows()
    ])

    prompt = f"""
You are an influencer marketing expert.

Campaign: "{campaign_name}"
Target Niches: {', '.join(niches)}

Available creators:
{summary}

Pick the TOP 3 best creators for this campaign and explain why in 1 sentence each.
Reply ONLY as JSON:
{{"recommendations": [
  {{"name": "...", "reason": "..."}},
  {{"name": "...", "reason": "..."}},
  {{"name": "...", "reason": "..."}}
]}}
No markdown, no extra text.
"""
    try:
        result = _call_claude(prompt, max_tokens=400)
        return json.loads(result).get("recommendations", [])
    except Exception:
        return []


def detect_incomplete_profiles(creators_df):
    """Return list of creators with missing profile fields."""
    issues = []
    for _, row in creators_df.iterrows():
        missing = []
        if str(row.get("Contact_Email", "")).strip() in ["", "nan"]:
            missing.append("Email")
        if str(row.get("Contact_Number", "")).strip() in ["", "nan", "N/A"]:
            missing.append("Phone")
        if row.get("Followers", 0) == 0:
            missing.append("Followers")
        if missing:
            issues.append({"name": row["Name"], "missing": missing})
    return issues