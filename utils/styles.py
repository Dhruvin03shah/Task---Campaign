def load_css():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ── Global ─────────────────────────────────────────────────────────── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #16213e 100%);
    min-height: 100vh;
}

/* ── Fix white top bar ───────────────────────────────────────────────── */
[data-testid="stHeader"] {
    background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 100%) !important;
    border-bottom: 1px solid rgba(255,255,255,0.07);
}

[data-testid="stToolbar"] {
    background: transparent !important;
}

#root > div:first-child {
    background: #0f0f1a !important;
}

.stApp > header {
    background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 100%) !important;
}

/* ── Deploy button ───────────────────────────────────────────────────── */
[data-testid="stToolbar"] {
    right: 1rem !important;
    top: 0.5rem !important;
}

[data-testid="stToolbar"] button {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 0.8rem !important;
    padding: 0.4rem 1rem !important;
    box-shadow: 0 4px 15px rgba(102,126,234,0.4) !important;
    transition: all 0.3s ease !important;
    opacity: 1 !important;
    visibility: visible !important;
}

[data-testid="stToolbar"] button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(102,126,234,0.6) !important;
}

[data-testid="stToolbar"] button span,
[data-testid="stToolbar"] button p {
    color: white !important;
    font-weight: 600 !important;
}

[data-testid="stToolbar"] svg {
    fill: white !important;
    color: white !important;
}

/* ── Global input text visibility ───────────────────────────────────── */
input[type="text"],
input[type="number"],
input[type="email"],
input[type="password"],
input[type="search"],
input,
textarea,
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea,
.stTextInput input,
.stTextArea textarea,
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea {
    color: #111111 !important;
    background: rgba(255,255,255,0.92) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 8px !important;
    caret-color: #764ba2 !important;
    -webkit-text-fill-color: #111111 !important;
}

input::placeholder,
textarea::placeholder,
.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #64748b !important;
    -webkit-text-fill-color: #64748b !important;
    opacity: 1 !important;
}

input:focus,
textarea:focus,
.stTextInput input:focus,
.stTextArea textarea:focus {
    border-color: rgba(102,126,234,0.6) !important;
    box-shadow: 0 0 0 2px rgba(102,126,234,0.2) !important;
    color: #111111 !important;
    -webkit-text-fill-color: #111111 !important;
    background: rgba(255,255,255,0.96) !important;
}

input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus {
    -webkit-text-fill-color: #e2e8f0 !important;
    -webkit-box-shadow: 0 0 0px 1000px rgba(26,26,46,0.95) inset !important;
    transition: background-color 5000s ease-in-out 0s;
}

/* ── Sidebar inputs ──────────────────────────────────────────────────── */
[data-testid="stSidebar"] .stTextInput input {
    background: rgba(255,255,255,0.92) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 8px !important;
    color: #111111 !important;
    -webkit-text-fill-color: #111111 !important;
    caret-color: #764ba2 !important;
}

[data-testid="stSidebar"] .stTextInput input::placeholder {
    color: #64748b !important;
    -webkit-text-fill-color: #64748b !important;
}

[data-testid="stSidebar"] .stTextInput input:focus {
    border-color: rgba(102,126,234,0.6) !important;
    box-shadow: 0 0 0 2px rgba(102,126,234,0.2) !important;
    color: #111111 !important;
    -webkit-text-fill-color: #111111 !important;
}

/* ── Fix multiselect dropdown background ─────────────────────────────── */
[data-testid="stSidebar"] .stMultiSelect div[data-baseweb="select"] {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 8px !important;
}

[data-testid="stSidebar"] .stMultiSelect input {
    color: #e2e8f0 !important;
    -webkit-text-fill-color: #e2e8f0 !important;
    caret-color: #a78bfa !important;
    background: transparent !important;
}

[data-testid="stSidebar"] .stMultiSelect span {
    color: #e2e8f0 !important;
}

/* ── Fix multiselect tags (niche pills) ──────────────────────────────── */
[data-testid="stSidebar"] [data-baseweb="tag"] {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    border: none !important;
    border-radius: 20px !important;
}

[data-testid="stSidebar"] [data-baseweb="tag"] span {
    color: white !important;
    -webkit-text-fill-color: white !important;
}

[data-testid="stSidebar"] [data-baseweb="tag"] [role="presentation"] {
    color: white !important;
    fill: white !important;
}

[data-baseweb="tag"] {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    border: none !important;
    border-radius: 20px !important;
}

[data-baseweb="tag"] span {
    color: white !important;
    -webkit-text-fill-color: white !important;
}

[data-baseweb="tag"] svg {
    fill: white !important;
    color: white !important;
}

/* ── Sidebar ─────────────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    border-right: 1px solid rgba(255,255,255,0.07);
}

[data-testid="stSidebar"] .stRadio label,
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stMultiSelect label,
[data-testid="stSidebar"] .stTextInput label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span {
    color: #c8d0e0 !important;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #e2e8f0 !important;
    font-weight: 600;
}

[data-testid="stSidebar"] .stButton button {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 0.5rem 1rem !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(102,126,234,0.4) !important;
}

[data-testid="stSidebar"] .stButton button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(102,126,234,0.6) !important;
}

/* ── Main text ───────────────────────────────────────────────────────── */
h1, h2, h3, h4, p, span, label, div {
    color: #e2e8f0;
}

/* ── Page title ──────────────────────────────────────────────────────── */
.page-title {
    font-size: 2rem;
    font-weight: 700;
    background: linear-gradient(135deg, #667eea, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.2rem;
}

.page-subtitle {
    color: #94a3b8;
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
}

/* ── Stat cards ──────────────────────────────────────────────────────── */
.stat-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 1.2rem 1.5rem;
    text-align: center;
    backdrop-filter: blur(10px);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.stat-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
}

.stat-card .stat-number {
    font-size: 2rem;
    font-weight: 700;
    color: #a78bfa;
}

.stat-card .stat-label {
    font-size: 0.8rem;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 0.2rem;
}

/* ── Creator cards ───────────────────────────────────────────────────── */
.creator-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1rem;
    backdrop-filter: blur(10px);
    transition: all 0.25s ease;
    position: relative;
    overflow: hidden;
}

.creator-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 4px; height: 100%;
    background: linear-gradient(180deg, #667eea, #a78bfa);
    border-radius: 4px 0 0 4px;
}

.creator-card:hover {
    transform: translateX(4px);
    border-color: rgba(102,126,234,0.3);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

.creator-name {
    font-size: 1.05rem;
    font-weight: 600;
    color: #e2e8f0;
    margin-bottom: 0.2rem;
}

.creator-meta {
    font-size: 0.8rem;
    color: #94a3b8;
    margin-bottom: 0.8rem;
}

/* ── Badges ──────────────────────────────────────────────────────────── */
.badge {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 600;
    margin-right: 5px;
    margin-bottom: 4px;
    letter-spacing: 0.03em;
}

.badge-platform-instagram { background: rgba(228,64,95,0.15);  color: #f472b6; border: 1px solid rgba(244,114,182,0.3); }
.badge-platform-youtube   { background: rgba(239,68,68,0.15);  color: #f87171; border: 1px solid rgba(248,113,113,0.3); }
.badge-platform-twitter   { background: rgba(59,130,246,0.15); color: #60a5fa; border: 1px solid rgba(96,165,250,0.3);  }

.badge-niche {
    background: rgba(167,139,250,0.1);
    color: #a78bfa;
    border: 1px solid rgba(167,139,250,0.25);
}

.badge-tier-top      { background: rgba(251,146,60,0.15);  color: #fb923c; border: 1px solid rgba(251,146,60,0.3);  }
.badge-tier-good     { background: rgba(34,197,94,0.15);   color: #4ade80; border: 1px solid rgba(74,222,128,0.3);  }
.badge-tier-possible { background: rgba(148,163,184,0.1);  color: #94a3b8; border: 1px solid rgba(148,163,184,0.2); }

/* ── Metric chips ────────────────────────────────────────────────────── */
.metric-chip {
    display: inline-block;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 5px 12px;
    margin-right: 8px;
    text-align: center;
}

.metric-chip .chip-value {
    font-size: 0.95rem;
    font-weight: 700;
    color: #c4b5fd;
}

.metric-chip .chip-label {
    font-size: 0.68rem;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}

/* ── Status badges ───────────────────────────────────────────────────── */
.status-shortlisted { background: rgba(34,197,94,0.15);  color: #4ade80; border: 1px solid rgba(74,222,128,0.3);  padding: 3px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 600; }
.status-backup      { background: rgba(59,130,246,0.15); color: #60a5fa; border: 1px solid rgba(96,165,250,0.3);  padding: 3px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 600; }
.status-rejected    { background: rgba(239,68,68,0.15);  color: #f87171; border: 1px solid rgba(248,113,113,0.3); padding: 3px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 600; }
.status-none        { background: rgba(148,163,184,0.1); color: #94a3b8; border: 1px solid rgba(148,163,184,0.2); padding: 3px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 600; }

/* ── Section headings ────────────────────────────────────────────────── */
.section-heading {
    font-size: 1.1rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid rgba(255,255,255,0.07);
}

/* ── AI recommendation cards ─────────────────────────────────────────── */
.ai-card {
    background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(167,139,250,0.08));
    border: 1px solid rgba(102,126,234,0.25);
    border-radius: 16px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1rem;
    position: relative;
    overflow: hidden;
}

.ai-card::after {
    content: '✦';
    position: absolute;
    top: 1rem; right: 1.2rem;
    font-size: 1.2rem;
    color: rgba(167,139,250,0.4);
}

.ai-card-rank {
    font-size: 0.72rem;
    font-weight: 700;
    color: #a78bfa;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.3rem;
}

.ai-card-name {
    font-size: 1rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 0.5rem;
}

.ai-card-reason {
    font-size: 0.85rem;
    color: #94a3b8;
    line-height: 1.5;
}

/* ── Buttons ─────────────────────────────────────────────────────────── */
.stButton button {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    padding: 0.6rem 1.5rem !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(102,126,234,0.35) !important;
    letter-spacing: 0.02em !important;
}

.stButton button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(102,126,234,0.55) !important;
}

/* ── Tabs ────────────────────────────────────────────────────────────── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.03);
    border-radius: 12px;
    padding: 4px;
    gap: 4px;
    border: 1px solid rgba(255,255,255,0.07);
}

.stTabs [data-baseweb="tab"] {
    border-radius: 9px !important;
    color: #94a3b8 !important;
    font-weight: 500 !important;
    padding: 0.5rem 1.2rem !important;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    color: white !important;
}

/* ── Alerts ──────────────────────────────────────────────────────────── */
.stAlert {
    border-radius: 12px !important;
    border: none !important;
}

/* ── Divider ─────────────────────────────────────────────────────────── */
hr {
    border-color: rgba(255,255,255,0.07) !important;
    margin: 1rem 0 !important;
}

/* ── Scrollbar ───────────────────────────────────────────────────────── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(167,139,250,0.3); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(167,139,250,0.5); }

/* ── Info banner ─────────────────────────────────────────────────────── */
.info-banner {
    background: linear-gradient(135deg, rgba(102,126,234,0.08), rgba(167,139,250,0.05));
    border: 1px solid rgba(102,126,234,0.2);
    border-radius: 14px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1.5rem;
    color: #94a3b8;
    font-size: 0.9rem;
}

/* ── Warning card ────────────────────────────────────────────────────── */
.warning-card {
    background: rgba(251,146,60,0.07);
    border: 1px solid rgba(251,146,60,0.2);
    border-radius: 12px;
    padding: 0.8rem 1.2rem;
    margin-bottom: 0.6rem;
    color: #fdba74;
    font-size: 0.88rem;
}

/* ── Score bar ───────────────────────────────────────────────────────── */
.score-bar-bg {
    background: rgba(255,255,255,0.07);
    border-radius: 4px;
    height: 4px;
    margin-top: 4px;
    overflow: hidden;
}

.score-bar-fill {
    height: 4px;
    border-radius: 4px;
    background: linear-gradient(90deg, #667eea, #a78bfa);
}
</style>
"""