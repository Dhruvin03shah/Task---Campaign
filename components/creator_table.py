import streamlit as st

STATUS_OPTIONS = ["—", "Shortlisted", "Backup", "Rejected"]

def _platform_badge(platform):
    p = platform.lower()
    cls = f"badge-platform-{p}" if p in ["instagram","youtube","twitter"] else "badge-niche"
    icons = {"instagram": "📸", "youtube": "▶️", "twitter": "🐦"}
    icon = icons.get(p, "🌐")
    return f'<span class="badge {cls}">{icon} {platform}</span>'

def _tier_badge(tier):
    if "Top" in tier:
        return f'<span class="badge badge-tier-top">{tier}</span>'
    elif "Good" in tier:
        return f'<span class="badge badge-tier-good">{tier}</span>'
    return f'<span class="badge badge-tier-possible">{tier}</span>'

def _status_badge(status):
    cls = {
        "Shortlisted": "status-shortlisted",
        "Backup":      "status-backup",
        "Rejected":    "status-rejected",
    }.get(status, "status-none")
    label = status if status != "—" else "Untagged"
    return f'<span class="{cls}">{label}</span>'

def _score_bar(score):
    pct = min(int(score), 100)
    return f'<div class="score-bar-bg"><div class="score-bar-fill" style="width:{pct}%"></div></div>'

def render_creator_table(creators_df, campaign, campaigns, save_fn):
    if creators_df.empty:
        st.markdown('<div class="info-banner">😕 No creators found matching the selected niches.</div>',
                    unsafe_allow_html=True)
        return

    niches_str   = ', '.join(campaign['niches'])
    count        = len(creators_df)

    st.markdown(f"""
    <div style="margin-bottom:1.5rem">
        <div class="section-heading">
            👥 Creator Pool &nbsp;
            <span style="font-size:0.8rem;font-weight:400;color:#94a3b8;">
                {count} creators matched · {niches_str}
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    for _, row in creators_df.iterrows():
        creator_id     = row["Creator_ID"]
        current_status = campaign.get("creators", {}).get(creator_id, "—")
        score          = row.get("Relevance_Score", 0)
        tier           = row.get("Tier", "🔍 Possible")
        profile        = str(row.get("Profile_Complete", ""))

        # Pre-compute all HTML fragments BEFORE the f-string
        platform_html  = _platform_badge(row["Platform"])
        tier_html      = _tier_badge(tier)
        status_html    = _status_badge(current_status)
        score_bar_html = _score_bar(score)
        niche1         = row["Primary_Niche"]
        niche2         = row["Secondary_Niche"]

        st.markdown(f"""
        <div class="creator-card">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem">
                <div>
                    <div class="creator-name">{row['Name']}</div>
                    <div class="creator-meta">📍 {row['City']} &nbsp;·&nbsp; {row['Language']}</div>
                    <div style="margin-bottom:0.7rem">
                        {platform_html}
                        <span class="badge badge-niche">{niche1}</span>
                        <span class="badge badge-niche">{niche2}</span>
                    </div>
                    <div>
                        <span class="metric-chip">
                            <div class="chip-value">{row['Followers']:,}</div>
                            <div class="chip-label">Followers</div>
                        </span>
                        <span class="metric-chip">
                            <div class="chip-value">{row['Engagement_Rate_%']}%</div>
                            <div class="chip-label">Engagement</div>
                        </span>
                        <span class="metric-chip">
                            <div class="chip-value">&#8377;{row['Cost_Per_Post']:,}</div>
                            <div class="chip-label">Per Post</div>
                        </span>
                    </div>
                </div>
                <div style="text-align:right;min-width:120px">
                    {tier_html}
                    <div style="font-size:0.78rem;color:#94a3b8;margin-top:0.4rem">
                        Score: <b style="color:#c4b5fd">{score}/100</b>
                    </div>
                    {score_bar_html}
                    <div style="margin-top:0.6rem">{status_html}</div>
                    <div style="font-size:0.72rem;color:#64748b;margin-top:0.3rem">{profile}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Action buttons below each card
        col1, col2, col3, col4 = st.columns([1, 1, 1, 3])
        with col1:
            if st.button("✅ Shortlist", key=f"s_{creator_id}"):
                campaign["creators"][creator_id] = "Shortlisted"
                campaigns[campaign["code"]] = campaign
                save_fn(campaigns)
                st.rerun()
        with col2:
            if st.button("🔁 Backup", key=f"b_{creator_id}"):
                campaign["creators"][creator_id] = "Backup"
                campaigns[campaign["code"]] = campaign
                save_fn(campaigns)
                st.rerun()
        with col3:
            if st.button("❌ Reject", key=f"r_{creator_id}"):
                campaign["creators"][creator_id] = "Rejected"
                campaigns[campaign["code"]] = campaign
                save_fn(campaigns)
                st.rerun()

        st.markdown("<div style='height:0.3rem'></div>", unsafe_allow_html=True)


def render_summary(campaign):
    creators    = campaign.get("creators", {})
    shortlisted = sum(1 for v in creators.values() if v == "Shortlisted")
    backup      = sum(1 for v in creators.values() if v == "Backup")
    rejected    = sum(1 for v in creators.values() if v == "Rejected")
    total       = len(creators)

    st.markdown(f"""
    <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:1.5rem">
        <div class="stat-card" style="flex:1;min-width:120px">
            <div class="stat-number" style="color:#4ade80">{shortlisted}</div>
            <div class="stat-label">Shortlisted</div>
        </div>
        <div class="stat-card" style="flex:1;min-width:120px">
            <div class="stat-number" style="color:#60a5fa">{backup}</div>
            <div class="stat-label">Backup</div>
        </div>
        <div class="stat-card" style="flex:1;min-width:120px">
            <div class="stat-number" style="color:#f87171">{rejected}</div>
            <div class="stat-label">Rejected</div>
        </div>
        <div class="stat-card" style="flex:1;min-width:120px">
            <div class="stat-number">{total}</div>
            <div class="stat-label">Total Tagged</div>
        </div>
    </div>
    """, unsafe_allow_html=True)