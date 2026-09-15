import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Executive Job Intelligence Platform", 
    page_icon="⚡", 
    layout="wide"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    .stApp {
        background-color: #030712;
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #94a3b8;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(6px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .dashboard-container {
        animation: fadeIn 0.3s ease-out forwards;
    }

    .saas-card {
        background: linear-gradient(180deg, rgba(17, 24, 39, 0.7) 0%, rgba(11, 15, 25, 0.9) 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.5);
        transition: all 0.3s ease;
    }

    .saas-card:hover {
        border-color: rgba(59, 130, 246, 0.4);
        box-shadow: 0 10px 30px -5px rgba(59, 130, 246, 0.15);
        transform: translateY(-2px);
    }

    .card-label {
        font-size: 0.8rem;
        font-weight: 600;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .card-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #f8fafc;
        margin-top: 8px;
    }

    .card-badge {
        display: inline-block;
        padding: 2px 8px;
        font-size: 0.75rem;
        font-weight: 600;
        color: #38bdf8;
        background: rgba(56, 189, 248, 0.1);
        border-radius: 20px;
        margin-top: 12px;
    }

    .main-header {
        font-weight: 800;
        font-size: 2.25rem;
        color: #ffffff;
        letter-spacing: -0.03em;
    }

    .sub-header {
        font-size: 0.95rem;
        color: #64748b;
        margin-bottom: 20px;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background-color: #0b0f19;
        padding: 6px;
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.06);
    }

    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 10px;
        color: #64748b;
        font-weight: 600;
        padding: 8px 18px;
        font-size: 0.9rem;
    }

    .stTabs [aria-selected="true"] {
        background-color: #1e293b !important;
        color: #ffffff !important;
    }

    div[data-testid="stDataFrame"] {
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        background: #0b0f19;
        padding: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("processed_jobs_dataset.csv")

df = load_data()

# Session State for Panel Visibility
if "panel_active" not in st.session_state:
    st.session_state.panel_active = True

# Top Header Layout
header_col, action_col = st.columns([5, 1])
with header_col:
    st.markdown('<div class="main-header">Job Intelligence Platform</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Executive analytics engine tracking real-time market compensations and trends.</div>', unsafe_allow_html=True)

with action_col:
    st.markdown("<br>", unsafe_allow_html=True)
    if not st.session_state.panel_active:
        if st.button("⚙️ Open Filters", width="stretch"):
            st.session_state.panel_active = True
            st.rerun()

# Layout Structure based on Panel State
if st.session_state.panel_active:
    main_display, filter_panel = st.columns([4, 1])
    
    with filter_panel:
        st.markdown("""
            <div style='background: #0b0f19; padding: 20px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.08);'>
                <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;'>
                    <span style='font-size: 0.85rem; font-weight: 700; color: #f8fafc; text-transform: uppercase;'>Filters</span>
                </div>
        """, unsafe_allow_html=True)
        
        # BACK BUTTON TO HIDE PANEL
        if st.button("⬅ Back / Hide", width="stretch", type="secondary"):
            st.session_state.panel_active = False
            st.rerun()
            
        st.markdown("<hr style='border-color: rgba(255,255,255,0.08); margin: 15px 0;'>", unsafe_allow_html=True)
        
        selected_work_mode = st.selectbox("Work Mode", ["All"] + list(df["Work Mode"].unique()))
        selected_exp_level = st.selectbox("Experience Level", ["All"] + list(df["Experience Level"].unique()))
        
        st.markdown("</div>", unsafe_allow_html=True)
else:
    main_display = None
    selected_work_mode = "All"
    selected_exp_level = "All"

# Filter Calculations
filtered_df = df.copy()
if selected_work_mode != "All":
    filtered_df = filtered_df[filtered_df["Work Mode"] == selected_work_mode]
if selected_exp_level != "All":
    filtered_df = filtered_df[filtered_df["Experience Level"] == selected_exp_level]

# Dashboard Tabs
tab1, tab2, tab3 = st.tabs(["📊 Executive Overview", "📂 Live Database Stream", "📈 Market Trends"])

with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
            <div class="saas-card">
                <div class="card-label">Active Openings</div>
                <div class="card-value">{len(filtered_df):,}</div>
                <div class="card-badge">Live Verified</div>
            </div>
        """, unsafe_allow_html=True)

    with c2:
        avg_salary = int(filtered_df["Salary"].mean()) if not filtered_df.empty else 0
        st.markdown(f"""
            <div class="saas-card">
                <div class="card-label">Mean Compensation</div>
                <div class="card-value">${avg_salary:,}</div>
                <div class="card-badge">USD Benchmark</div>
            </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
            <div class="saas-card">
                <div class="card-label">Participating Firms</div>
                <div class="card-value">{filtered_df["Company Name"].nunique():,}</div>
                <div class="card-badge">Unique Entities</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("### **Compensation Breakdown by Work Mode**")
    if not filtered_df.empty:
        chart_summary = filtered_df.groupby("Work Mode")["Salary"].mean().reset_index()
        st.bar_chart(chart_summary.set_index("Work Mode"), color="#3b82f6")
    else:
        st.info("No records available for visual distribution.")

with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### **Filtered Record Stream**")
    st.dataframe(filtered_df, width="stretch", height=420)

with tab3:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### **Seniority vs Salary Analysis**")
    if not filtered_df.empty:
        chart_data = filtered_df.groupby("Experience Level")["Salary"].mean().reset_index()
        st.bar_chart(chart_data.set_index("Experience Level"), color="#10b981")
    else:
        st.warning("No data found for seniority analysis.")