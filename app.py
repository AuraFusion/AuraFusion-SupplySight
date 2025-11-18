import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- Dashboard Title ---
st.set_page_config(page_title="SupplySight Dashboard", layout="wide")
st.markdown("""
    <h1 style='text-align: center; color: #002B5B;'>SupplySight: SME Supply Chain Resilience Dashboard</h1>
""", unsafe_allow_html=True)

# --- File Upload & Template ---
with st.sidebar:
    st.header("📤 Upload Your Supply Data")
    uploaded_file = st.file_uploader("Upload CSV or Excel File", type=['csv', 'xlsx'])
    st.markdown("[📥 Download Sample Template](https://yourdomain.com/sample_template.xlsx)")

# --- Dummy Data if No Upload ---
if uploaded_file:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
else:
    df = pd.DataFrame({
        'Supplier': ['Alpha Co', 'Beta Ltd', 'Gamma Inc'],
        'LeadTime': [25, 40, 15],
        'CostVolatility': [0.1, 0.35, 0.2],
        'SupplyRisk': [0.2, 0.8, 0.5],
        'Country': ['USA', 'China', 'Brazil']
    })

# --- Resilience Score ---
avg_volatility = df['CostVolatility'].mean()
avg_risk = df['SupplyRisk'].mean()
resilience_score = max(0, 100 - ((avg_volatility + avg_risk) * 50))

score_color = "#28a745" if resilience_score > 70 else ("#ffc107" if resilience_score > 50 else "#dc3545")

with st.container():
    st.markdown(f"""
    <div style='text-align: center; background-color:{score_color}; padding: 2rem; border-radius: 12px;'>
        <h2 style='color: white;'>Resilience Score</h2>
        <h1 style='color: white; font-size: 72px;'>{round(resilience_score)}</h1>
    </div>
    """, unsafe_allow_html=True)

# --- Recommendations Panel ---
st.subheader("🔍 Recommendations")
rec1 = "Diversify supplier base in high-risk regions (e.g., China)."
rec2 = "Introduce safety stock for long lead-time items (>30 days)."
rec3 = "Negotiate stable contracts with volatile suppliers."

cols = st.columns(3)
rec_colors = ["#FFD700", "#87CEFA", "#FFB6C1"]
recs = [rec1, rec2, rec3]
for i, col in enumerate(cols):
    with col:
        st.markdown(f"""
        <div style='background-color: {rec_colors[i]}; padding: 1rem; border-radius: 10px; min-height: 100px;'>
            <p style='font-size: 16px;'><strong>{recs[i]}</strong></p>
        </div>
        """, unsafe_allow_html=True)

# --- Mitigation Action Plan Card ---
st.subheader("🛠️ Mitigation Plan")
st.markdown("""
<div style='background-color: #FFF3CD; padding: 1.5rem; border-radius: 10px;'>
    <h4>Diversify Supplier Base</h4>
    <ul>
        <li>Research 3 alternate suppliers per key component</li>
        <li>Evaluate based on cost, risk, and geography</li>
        <li>Initiate pilot orders with at least one new supplier within 60 days</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- Key Metrics ---
st.subheader("📊 Key Metrics")
metrics = st.columns(2)

vol_color = "#28a745" if avg_volatility < 0.2 else ("#ffc107" if avg_volatility < 0.3 else "#dc3545")
risk_color = "#28a745" if avg_risk < 0.3 else ("#ffc107" if avg_risk < 0.6 else "#dc3545")

metrics[0].markdown(f"""
    <div style='background-color: {vol_color}; padding: 1rem; border-radius: 10px;'>
        <h5 style='color:white;'>Average Cost Volatility</h5>
        <h2 style='color:white;'>{avg_volatility:.2f}</h2>
    </div>
""", unsafe_allow_html=True)

metrics[1].markdown(f"""
    <div style='background-color: {risk_color}; padding: 1rem; border-radius: 10px;'>
        <h5 style='color:white;'>Average Supply Risk</h5>
        <h2 style='color:white;'>{avg_risk:.2f}</h2>
    </div>
""", unsafe_allow_html=True)
