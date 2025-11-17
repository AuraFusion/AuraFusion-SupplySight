>>> import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

# --- PAGE CONFIG ---
st.set_page_config(page_title="SupplySight - SME Resilience Engine", layout="wide")

# --- HEADER ---
st.title("📊 SupplySight Dashboard")
st.markdown("""
**Welcome to the Beta version of SupplySight!** 
This AI-powered SME resilience tool helps assess supply chain vulnerabilities and auto-generate mitigation strategies with minimal data.
""")

# --- SIDEBAR INPUTS ---
st.sidebar.header("🔍 Manual Data Input")
supplier_count = st.sidebar.number_input("Number of Suppliers", 1, 50, 3)
geo_spread = st.sidebar.slider("Geographic Spread (1=Local, 10=Global)", 1, 10, 5)
lead_time = st.sidebar.slider("Average Lead Time (days)", 1, 120, 30)
cost_volatility = st.sidebar.slider("Cost Volatility (1=Stable, 10=Unstable)", 1, 10, 5)
inventory_days = st.sidebar.slider("Inventory Days of Coverage", 0, 180, 30)

# --- SCORE CALCULATION ---
def calculate_score(supplier_count, geo_spread, lead_time, cost_volatility, inventory_days):
    score = (
        (supplier_count / 10) * 0.2 +
        (geo_spread / 10) * 0.2 +
        ((120 - lead_time) / 120) * 0.2 +
        ((10 - cost_volatility) / 10) * 0.2 +
        (inventory_days / 180) * 0.2
    ) * 100
    return round(score, 2)

score = calculate_score(supplier_count, geo_spread, lead_time, cost_volatility, inventory_days)

# --- RISK LEVEL ---
def risk_level(score):
    if score >= 80:
        return "🟢 Low Risk"
    elif score >= 50:
        return "🟡 Medium Risk"
    else:
        return "🔴 High Risk"

# --- LAYOUT ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📈 Resilience Score")
    st.metric("Resilience Score", f"{score}/100", delta=score - 50)
    st.write(f"**Risk Level:** {risk_level(score)}")

with col2:
    st.subheader("💡 AI-Powered Recommendations")
    if score < 50:
        st.warning("High supply chain risk detected.\n\nConsider supplier diversification, inventory buffers, and faster lead times.")
    elif score < 80:
        st.info("Moderate risk.\n\nExplore regional supplier options and cost tracking mechanisms.")
    else:
        st.success("Low risk.\n\nMaintain strategies and monitor trends quarterly.")

# --- DOWNLOAD MITIGATION PLAN ---
st.subheader("📄 Download Mitigation Plan")
report = f"""SupplySight Resilience Report\n\nResilience Score: {score}/100\nRisk Level: {risk_level(score)}\n\nInputs:\n- Supplier Count: {supplier_count}\n- Geographic Spread: {geo_spread}/10\n- Lead Time: {lead_time} days\n- Cost Volatility: {cost_volatility}/10\n- Inventory Days: {inventory_days}\n\nRecommendations:\n{ '- Diversify suppliers\n- Increase buffer stock\n- Monitor geopolitical risks' if score < 50 else '- Continue current strategy\n- Moderate regional backup planning' }
"""
st.download_button("📥 Download Resilience Report", report, file_name="SupplySight_Resilience_Plan.txt")

# --- TEMPLATE DOWNLOAD ---
st.subheader("📂 Download Sample Input Template")
sample_df = pd.DataFrame({
    "Supplier_Count": [3],
    "Geo_Spread": [5],
    "Lead_Time": [30],
    "Cost_Volatility": [5],
    "Inventory_Days": [30]
})
st.download_button(
    label="⬇️ Download CSV Template",
    data=sample_df.to_csv(index=False),
    file_name="SupplySight_Template.csv",
    mime="text/csv"
)

# --- FILE UPLOAD ---
st.subheader("📤 Upload Data for Automated Scoring")
file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])
if file is not None:
    try:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)

        st.write("📋 Your Uploaded Data:", df)

        uploaded_score = calculate_score(
            df['Supplier_Count'][0],
            df['Geo_Spread'][0],
            df['Lead_Time'][0],
            df['Cost_Volatility'][0],
            df['Inventory_Days'][0]
        )

        st.success(f"✅ Calculated Resilience Score: {uploaded_score}/100")
        st.info(f"Risk Level: {risk_level(uploaded_score)}")

    except Exception as e:
        st.error(f"❌ Error reading file or calculating score: {e}")

# --- FOOTER ---
st.markdown("---")
st.caption("SupplySight Beta • AI for SME Resilience • 2025")
```
