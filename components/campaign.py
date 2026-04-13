import streamlit as st
import json
import os
import time

CAMPAIGNS_FILE = "data/campaigns.json"

def load_campaigns():
    if os.path.exists(CAMPAIGNS_FILE):
        with open(CAMPAIGNS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_campaigns(campaigns):
    with open(CAMPAIGNS_FILE, "w") as f:
        json.dump(campaigns, f, indent=2)

def render_campaign_panel(all_niches):
    st.sidebar.header("📁 Campaign Manager")

    campaigns = load_campaigns()
    mode = st.sidebar.radio(
        "",
        ["➕ New Campaign", "📂 Select Existing"],
        label_visibility="collapsed"
    )

    if mode == "➕ New Campaign":
        st.sidebar.subheader("Create Campaign")
        code = st.sidebar.text_input("Campaign Code *", placeholder="e.g. CAMP001")
        name = st.sidebar.text_input("Campaign Name *", placeholder="e.g. Summer Fitness Drive")

        # Session state init
        if "custom_niches" not in st.session_state:
            st.session_state.custom_niches = []

        all_options = sorted(set(all_niches + st.session_state.custom_niches)) + ["➕ Other (add custom)"]

        selected_raw = st.sidebar.multiselect("Target Niches *", options=all_options)

        if "➕ Other (add custom)" in selected_raw:
            st.sidebar.markdown("**✏️ Create your own niche:**")
            col1, col2 = st.sidebar.columns([3, 1])
            with col1:
                new_niche = st.text_input(
                    "niche name",
                    placeholder="e.g. Crypto",
                    label_visibility="collapsed",
                    key="custom_niche_input"
                )
            with col2:
                if st.button("Add", use_container_width=True):
                    niche_clean = new_niche.strip().title()
                    if niche_clean and niche_clean not in all_options:
                        st.session_state.custom_niches.append(niche_clean)
                        st.rerun()
                    elif not niche_clean:
                        st.sidebar.warning("Type a niche name first!")
                    else:
                        st.sidebar.warning("Already exists!")

        selected_niches = [n for n in selected_raw if n != "➕ Other (add custom)"]

        if st.session_state.custom_niches:
            st.sidebar.markdown("**Your custom niches:**")
            for cn in st.session_state.custom_niches:
                c1, c2 = st.sidebar.columns([4, 1])
                c1.markdown(f"🏷️ `{cn}`")
                if c2.button("✕", key=f"remove_{cn}"):
                    st.session_state.custom_niches.remove(cn)
                    st.rerun()

        if st.sidebar.button("🚀 Create Campaign", use_container_width=True):
            if not code or not name or not selected_niches:
                st.sidebar.error("All fields are mandatory!")
            elif code in campaigns:
                st.sidebar.error("Campaign code already exists!")
            else:
                campaigns[code] = {
                    "code": code,
                    "name": name,
                    "niches": selected_niches,
                    "creators": {}
                }
                save_campaigns(campaigns)
                st.session_state.custom_niches = []

                # ── Success message for 4 seconds ──
                msg = st.sidebar.empty()
                msg.success(f"✅ Campaign '{name}' created!")
                time.sleep(4)
                msg.empty()

                st.rerun()

        return None

    else:
        if not campaigns:
            st.sidebar.info("No campaigns yet. Create one first.")
            return None

        options = {f"{v['code']} — {v['name']}": k for k, v in campaigns.items()}
        selected_label = st.sidebar.selectbox("Select Campaign", list(options.keys()))
        selected_code  = options[selected_label]
        campaign = campaigns[selected_code]

        st.sidebar.markdown(f"**Niches:** {', '.join(campaign['niches'])}")
        total       = len(campaign.get("creators", {}))
        shortlisted = sum(1 for s in campaign["creators"].values() if s == "Shortlisted")
        st.sidebar.markdown(f"**Tagged:** {total} | ✅ Shortlisted: {shortlisted}")

        st.sidebar.divider()

        # ── Delete Campaign ──────────────────────────────────────────────────
        st.sidebar.markdown("**⚠️ Danger Zone**")
        if "confirm_delete" not in st.session_state:
            st.session_state.confirm_delete = False

        if not st.session_state.confirm_delete:
            if st.sidebar.button("🗑️ Delete This Campaign", use_container_width=True):
                st.session_state.confirm_delete = True
                st.rerun()
        else:
            st.sidebar.warning(f"Delete **{campaign['name']}**? This cannot be undone.")
            c1, c2 = st.sidebar.columns(2)
            with c1:
                if st.button("Yes, Delete", use_container_width=True):
                    del campaigns[selected_code]
                    save_campaigns(campaigns)
                    st.session_state.confirm_delete = False

                    msg = st.sidebar.empty()
                    msg.error(f"🗑️ Campaign deleted!")
                    time.sleep(3)
                    msg.empty()

                    st.rerun()
            with c2:
                if st.button("Cancel", use_container_width=True):
                    st.session_state.confirm_delete = False
                    st.rerun()

        return campaign, campaigns