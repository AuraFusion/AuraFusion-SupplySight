import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

st.set_page_config(page_title="SupplySight", layout="wide")

# ---------------------------------------
# Function: Downloadable template example
# ---------------------------------------
def generate_template():
    df_template = pd.DataFrame({
        'Supplier_Count': [3],
        'Geo_Spread': [4],
        'Cost_Volatility': [2],
        'Lead_Time': [3],
        'Alt_Supplier_Options': [1]
    })
    return df_template.to_csv(index=False).encode('utf-8')

# ---------------------------------------
# Function: Calculate Resilience Score
# ---------------------------------------
def calculate_resilience_score(data):
    score = (
        data['Supplier_Count'] * 0.2 +
        data['Geo_Spread'] * 0.2 +
        (5 - data['Cost_Volatility']) * 0.2 +
        (5 - data['Lead_Time']) * 0.2 +
        data['Alt_Supplier_Options'] * 0.2
    ) * 20
    return round(score, 2)

# ---------------------------------------
# Function: Risk Level Color
# ---------------------------------------
def risk_level_color(score):
    if score >= 80:
        return "🟢 Low Risk"
    elif score >= 60:
        return "🟡 Medium Risk"
    else:
        return "🔴 High Risk"

# ---------------------------------------
# Sidebar
# ---------------------------------------
st.sidebar.header("Upload Your Data or Use Manual Input")

uploaded_file = st.sidebar.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

st.sidebar.markdown("📥 Download Sample Template")
st.sidebar.download_button(
    label="Download CSV Template",
    data=generate_template(),
    file_name='SupplySight_Template.csv',
    mime='text/csv'
)

# ---------------------------------------
# Main App
# ---------------------------------------
st.title("📊 SupplySight – SME Resilience Dashboard (Beta)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Input Data")
    
    if uploaded_file:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        st.dataframe(df)
        
        data = df.iloc[0]
    else:
        st.markdown("Or fill in your data below:")
        data = {
            'Supplier_Count': st.slider("Number of Suppliers", 1, 5, 3),
            'Geo_Spread': st.slider("Geographic Spread", 1, 5, 3),
            'Cost_Volatility': st.slider("Cost Volatility (1=Low, 5=High)", 1, 5, 3),
            'Lead_Time': st.slider("Lead Time (1=Short, 5=Long)", 1, 5, 3),
            'Alt_Supplier_Options': st.slider("Alternative Supplier Options", 1, 5, 2)
        }

# Calculate score
if isinstance(data, pd.Series):
    data_dict = data.to_dict()
else:
    data_dict = data

score = calculate_resilience_score(data_dict)
risk_level = risk_level_color(score)

# ---------------------------------------
# Output: Score and Recommendation
# ---------------------------------------
with col2:
    st.subheader("📈 Resilience Score & AI Suggestions")

    st.metric("Resilience Score", f"{score} / 100", risk_level)

    st.markdown("### 🤖 AI-Powered Recommendations:")
    if score < 60:
        st.error("⚠️ High Risk Detected. Diversify your supplier base and reduce lead times immediately.")
    elif score < 80:
        st.warning("🟡 Moderate Risk. Explore regional alternatives and establish backup suppliers.")
    else:
       st.success("✅ Low Risk. Maintain current strategy but monitor cost volatility.")

