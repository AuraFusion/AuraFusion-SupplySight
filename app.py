# SupplySight: Streamlit Dashboard UI with Enhanced Visuals + Spider Chart

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO

st.set_page_config(page_title="SupplySight", layout="wide")

# ---------- Template Download ----------
def generate_template():
    df_template = pd.DataFrame({
        'Supplier_Count': [3],
        'Geo_Spread': [4],
        'Cost_Volatility': [2],
        'Lead_Time': [3],
        'Alt_Supplier_Options': [1]
    })
    return df_template.to_csv(index=False).encode('utf-8')

# ---------- Scoring Logic ----------
def calculate_resilience_score(data):
    score = (
        data['Supplier_Count'] * 0.2 +
        data['Geo_Spread'] * 0.2 +
        (5 - data['Cost_Volatility']) * 0.2 +
        (5 - data['Lead_Time']) * 0.2 +
        data['Alt_Supplier_Options'] * 0.2
    ) * 20
    return round(score, 2)

def risk_level_color(score):
    if score >= 80:
        return "🟢 Low Risk"
    elif score >= 60:
        return "🟡 Medium Risk"
    else:
        return "🔴 High Risk"

# ---------- Sidebar Input ----------
st.sidebar.header("📂 Upload Data or Use Sample")
uploaded_file = st.sidebar.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])
st.sidebar.download_button(
    label="📥 Download CSV Template",
    data=generate_template(),
    file_name='SupplySight_Template.csv',
    mime='text/csv'
)

# ---------- Title & Layout ----------
st.markdown("""
    <h1 style='text-align: center; color: #0A5275;'>SupplySight — SME Resilience Dashboard (Beta)</h1>
    <p style='text-align: center;'>AI-powered insights for supplier risk and mitigation</p>
    <hr style='border: 1px solid #CCC;'>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# ---------- Input Column ----------
with col1:
    st.subheader("🔢 Input Your Data")
    if uploaded_file:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
        st.dataframe(df)
        data = df.iloc[0]
    else:
        data = {
            'Supplier_Count': st.slider("# Suppliers", 1, 5, 3),
            'Geo_Spread': st.slider("Geographic Spread", 1, 5, 3),
            'Cost_Volatility': st.slider("Cost Volatility (1=Low, 5=High)", 1, 5, 2),
            'Lead_Time': st.slider("Lead Time (1=Short, 5=Long)", 1, 5, 3),
            'Alt_Supplier_Options': st.slider("Alt Supplier Options", 1, 5, 2)
        }

# ---------- Output Column ----------
with col2:
    st.subheader("📊 Risk Score & Insights")
    score = calculate_resilience_score(data if isinstance(data, dict) else data.to_dict())
    risk_level = risk_level_color(score)
    
    st.markdown(f"<div style='padding: 1rem; border-radius: 10px; background-color: #F0F8FF;'>
    <h2>Resilience Score: {score}/100</h2>
    <p style='font-size: 18px;'>{risk_level}</p></div>", unsafe_allow_html=True)

    st.markdown("### 🤖 AI-Recommended Actions")
    if score < 60:
        st.error("⚠️ High Risk: Diversify supplier base and reduce lead times.")
    elif score < 80:
        st.warning("🟡 Medium Risk: Explore regional backups and reduce volatility.")
    else:
        st.success("✅ Low Risk: Maintain strategy but monitor volatility.")

# ---------- Spider Chart ----------
st.markdown("---")
st.subheader("📌 Resilience Profile (Radar Chart)")

categories = ['Supplier_Count', 'Geo_Spread', 'Cost_Volatility', 'Lead_Time', 'Alt_Supplier_Options']
values = [
    data['Supplier_Count'] if isinstance(data, dict) else data.Supplier_Count,
    data['Geo_Spread'] if isinstance(data, dict) else data.Geo_Spread,
    6 - (data['Cost_Volatility'] if isinstance(data, dict) else data.Cost_Volatility),
    6 - (data['Lead_Time'] if isinstance(data, dict) else data.Lead_Time),
    data['Alt_Supplier_Options'] if isinstance(data, dict) else data.Alt_Supplier_Options
]

fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=values + [values[0]],
                              theta=categories + [categories[0]],
                              fill='toself',
                              name='Resilience Profile'))
fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
                  showlegend=False)
st.plotly_chart(fig, use_container_width=True)

# ---------- Footer ----------
st.markdown("""
    <hr><small>🔒 SupplySight is a beta pilot for SME testing. No data is stored or shared. Version 0.2</small>
""", unsafe_allow_html=True)
