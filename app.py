import streamlit as st
import pandas as pd
import os, sys

sys.path.insert(0, os.path.dirname(__file__))

from utils.styles        import load_css
from utils.data_cleaning  import load_and_clean, get_all_niches
from utils.recommendation import filter_by_niches, get_recommended_creators
from utils.ai_features    import recommend_creators_ai, detect_incomplete_profiles
from components.campaign  import render_campaign_panel, save_campaigns
from components.creator_table import render_creator_table, render_summary

st.set_page_config(
    page_title="Creator Dashboard",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Inject CSS ────────────────────────────────────────────────────────────────
st.markdown(load_css(), unsafe_allow_html=True)

# ── Load Data ─────────────────────────────────────────────────────────────────
@st.cache_data
def get_data():
    return load_and_clean("data/AI_Assignment.xlsx")

df         = get_data()
all_niches = get_all_niches(df)

# ── Sidebar ───────────────────────────────────────────────────────────────────
result = render_campaign_panel(all_niches)

# ── Main ──────────────────────────────────────────────────────────────────────
st.markdown('<div class="page-title">🎯 Creator Campaign Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Manage campaigns, discover creators, and get AI-powered recommendations</div>', unsafe_allow_html=True)

if result is None:
    st.markdown("""
    <div class="info-banner">
        👈 &nbsp; <b>Get started</b> — create a new campaign from the sidebar or select an existing one.
    </div>
    """, unsafe_allow_html=True)

    # Incomplete profile detector
    st.markdown('<div class="section-heading">🔍 AI: Incomplete Profile Detector</div>', unsafe_allow_html=True)
    issues = detect_incomplete_profiles(df)
    if issues:
        for issue in issues:
            st.markdown(f"""
            <div class="warning-card">
                ⚠️ &nbsp;<b>{issue['name']}</b> — Missing: {', '.join(issue['missing'])}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.success("✅ All creator profiles are complete!")

    # All creators overview
    st.markdown('<div class="section-heading" style="margin-top:1.5rem">📋 All Creators</div>', unsafe_allow_html=True)
    for _, row in df.iterrows():
        st.markdown(f"""
        <div class="creator-card">
            <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem">
                <div>
                    <div class="creator-name">{row['Name']}</div>
                    <div class="creator-meta">📍 {row['City']} &nbsp;·&nbsp; {row['Language']}</div>
                    <div>
                        <span class="badge badge-niche">{row['Primary_Niche']}</span>
                        <span class="badge badge-niche">{row['Secondary_Niche']}</span>
                    </div>
                </div>
                <div style="display:flex;gap:0.6rem;flex-wrap:wrap">
                    <span class="metric-chip">
                        <div class="chip-value">{row['Followers']:,}</div>
                        <div class="chip-label">Followers</div>
                    </span>
                    <span class="metric-chip">
                        <div class="chip-value">{row['Engagement_Rate_%']}%</div>
                        <div class="chip-label">Engagement</div>
                    </span>
                    <span class="metric-chip">
                        <div class="chip-value">{row['Platform']}</div>
                        <div class="chip-label">Platform</div>
                    </span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

else:
    campaign, campaigns = result

    tab1, tab2, tab3 = st.tabs(["👥 Creator Pool", "🤖 AI Recommendations", "📊 Summary"])

    with tab1:
        filtered = filter_by_niches(df, campaign["niches"])
        render_creator_table(filtered, campaign, campaigns, save_campaigns)

    with tab2:
        st.markdown("""
        <div style="background:linear-gradient(135deg,rgba(102,126,234,0.12),rgba(167,139,250,0.08));
                    border:1px solid rgba(102,126,234,0.25);border-radius:16px;padding:1.5rem;margin-bottom:1.5rem">
            <div style="font-size:1.1rem;font-weight:700;color:#e2e8f0;margin-bottom:0.3rem">
                ✦ AI-Powered Recommendations
            </div>
            <div style="font-size:0.85rem;color:#94a3b8">
                We analyze your campaign brief and creator profiles to surface the best matches — with reasoning.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("✨ Get AI Recommendations", use_container_width=True):
            with st.spinner("Claude is analyzing creators..."):
                filtered_ai = filter_by_niches(df, campaign["niches"])
                recs = recommend_creators_ai(filtered_ai, campaign["name"], campaign["niches"])

            if recs:
                for i, rec in enumerate(recs, 1):
                    rank_labels = {1: "🥇 Best Match", 2: "🥈 Strong Fit", 3: "🥉 Good Option"}
                    st.markdown(f"""
                    <div class="ai-card">
                        <div class="ai-card-rank">{rank_labels.get(i, f'#{i}')}</div>
                        <div class="ai-card-name">{rec['name']}</div>
                        <div class="ai-card-reason">{rec['reason']}</div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("Could not get AI recommendations. Check API connectivity.")

        st.markdown('<div class="section-heading" style="margin-top:1.5rem">📈 Top Creators by Relevance Score</div>', unsafe_allow_html=True)
        top = get_recommended_creators(df, campaign["niches"], top_n=5)
        if not top.empty:
            for _, row in top.iterrows():
                score = row.get("Relevance_Score", 0)
                tier  = row.get("Tier", "")
                st.markdown(f"""
                <div class="creator-card">
                    <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem">
                        <div>
                            <div class="creator-name">{row['Name']}</div>
                            <div class="creator-meta">{row['Platform']} &nbsp;·&nbsp; {row['Primary_Niche']}</div>
                            <span class="metric-chip">
                                <div class="chip-value">{row['Followers']:,}</div>
                                <div class="chip-label">Followers</div>
                            </span>
                            <span class="metric-chip">
                                <div class="chip-value">{row['Engagement_Rate_%']}%</div>
                                <div class="chip-label">Engagement</div>
                            </span>
                        </div>
                        <div style="text-align:right">
                            <div style="font-size:1.6rem;font-weight:700;color:#a78bfa">{score}</div>
                            <div style="font-size:0.72rem;color:#94a3b8">/ 100 score</div>
                            <div style="margin-top:0.3rem">{tier}</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    with tab3:
        st.markdown(f'<div class="section-heading">📊 {campaign["name"]} — Summary</div>', unsafe_allow_html=True)
        render_summary(campaign)

        classified = {k: v for k, v in campaign.get("creators", {}).items() if v != "—"}
        if classified:
            st.markdown('<div class="section-heading">Classification Breakdown</div>', unsafe_allow_html=True)
            for cid, status in classified.items():
                match = df[df["Creator_ID"] == cid]
                if not match.empty:
                    r = match.iloc[0]
                    st.markdown(f"""
                    <div class="creator-card" style="padding:0.9rem 1.2rem">
                        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem">
                            <div>
                                <div class="creator-name" style="font-size:0.95rem">{r['Name']}</div>
                                <div class="creator-meta">{r['Platform']} · {r['Primary_Niche']} · {r['Followers']:,} followers</div>
                            </div>
                            <div>
                                <span class="{'status-shortlisted' if status=='Shortlisted' else 'status-backup' if status=='Backup' else 'status-rejected'}">{status}</span>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="info-banner">
                No creators classified yet. Go to the <b>Creator Pool</b> tab to start tagging.
            </div>
            """, unsafe_allow_html=True)