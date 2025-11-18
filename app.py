import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(layout="wide", page_title="SupplySight")

st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(to right, #f97316, #facc15);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .card {
        background-color: #f9fafb;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }
    .metric-block {
        display: flex;
        justify-content: space-around;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='main-header'>
    <h1>SupplySight 🚀</h1>
    <h3>AI-Driven Resilience & Action Engine for SMEs</h3>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("### 📊 Resilience Score")
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=68,
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': "green"},
               'steps': [
                   {'range': [0, 50], 'color': "#f87171"},
                   {'range': [50, 75], 'color': "#facc15"},
                   {'range': [75, 100], 'color': "#4ade80"}]
              },
        domain={'x': [0, 1], 'y': [0, 1]}
    ))
    fig.update_layout(height=250, margin=dict(l=20, r=20, t=40, b=0))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("### 📊 Key Metrics")
    st.markdown("""
    <div class='card'>
        <p><b>Supplier Concentration:</b> 57%</p>
        <p><b>Cost Volatility:</b> Moderate</p>
        <p><b>Geographic Exposure:</b> 15 Countries</p>
        <p><b>Supply Risk:</b> High</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("### 🔧 Recommendations")
    st.markdown("""
    <div class='card'>
        <ul>
            <li>🌟 Evaluate alternate suppliers in East Asia</li>
            <li>📊 Increase buffer inventory for key items</li>
            <li>📂 <a href='#'>Download Project Brief</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

col4, col5 = st.columns([1, 1])

with col4:
    st.markdown("### 📈 Risk Insights")
    bar_fig = go.Figure([go.Bar(x=['Jan','Feb','Mar','Apr','May','Jun'], y=[2,4,6,8,10,14], marker_color="#60a5fa")])
    bar_fig.update_layout(height=250, margin=dict(l=20, r=20, t=30, b=0))
    st.plotly_chart(bar_fig, use_container_width=True)

with col5:
    st.markdown("### 📊 Supplier Diversification")
    pie_fig = go.Figure(go.Pie(labels=["Main Supplier", "Backup", "Other"],
                               values=[50, 30, 20],
                               hole=.4))
    pie_fig.update_traces(marker=dict(colors=["#f59e0b", "#10b981", "#3b82f6"]))
    pie_fig.update_layout(height=250, margin=dict(l=20, r=20, t=30, b=0))
    st.plotly_chart(pie_fig, use_container_width=True)

st.markdown("### 🚧 Mitigation Plan")
st.markdown("""
<div class='card'>
    <h4>🚀 Diversify Supplier Base</h4>
    <p><b>Objective:</b> Reduce single-source dependency</p>
    <p><b>Timeline:</b> 3-6 months</p>
    <p><b>Owner:</b> Supply Chain Manager</p>
    <p><b>KPIs:</b> Supplier mix, lead time</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 📂 Upload Your Data")
uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])
if uploaded_file:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
    st.write("Preview:", df.head())

st.download_button("Download Sample Template", data="Supplier,Location,RiskScore\n", file_name="sample_template.csv")

st.markdown("---")
st.markdown("<center><small>🔄 Beta v0.2 | ©2025 SupplySight</small></center>", unsafe_allow_html=True)
