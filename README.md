# 🚀 ResiliLytics — AI-Powered Resilience & Risk Dashboard for SMEs

**ResiliLytics** is an AI-powered dashboard that helps small and medium-sized enterprises (SMEs) evaluate, visualize, and strengthen their supply chain resilience — using minimal data inputs.

Powered by data and guided by insight, ResiliLytics:
- 🔍 Analyzes supplier risk exposure  
- 💡 Recommends mitigation strategies  
- 📈 Translates supply chain complexity into clear, actionable plans

---

## 🧠 What It Does

ResiliLytics analyzes uploaded supply chain data and provides:
- ✅ **Resilience Score** (color-coded)
- 📊 **Key Metrics**: Supplier concentration, geographic exposure, supply risk, etc.
- 🔍 **Risk Insights**: Charts, supplier diversification analysis
- 💡 **AI-Driven Recommendations**
- 🛠️ **Mitigation Plan Generator**
- 📬 **Contact form** to receive feedback or collaboration requests

All with a clean, interactive interface — no coding required.

---

## 📊 How Metrics Are Calculated

ResiliLytics uses a structured, data-driven scoring engine to evaluate supply chain resilience. Here’s an overview of the key calculations:

### 1️⃣ Resilience Score  
A composite indicator representing overall resilience:  
`Resilience Score = 100 - Supplier Concentration (%) - (Avg. Cost Volatility × 10)`  
The score decreases when dependency or volatility increases.

### 2️⃣ Supplier Concentration  
Measures dependency on the largest supplier:  
`Supplier Concentration = (Spend on Top Supplier ÷ Total Spend) × 100`  
High concentration ⇒ higher vulnerability.

### 3️⃣ Geographic Exposure  
Counts the number of unique supplier countries:  
`Geographic Exposure = Number of Unique Supplier Countries`  
More countries ⇒ better global diversification.

### 4️⃣ Cost Volatility  
Evaluates price stability using user-entered cost history:  
`Cost Volatility = Standard Deviation of Historical Cost Values`  
Example input: `12.5; 12.7; 14.1; 13.8`

### 5️⃣ Supply Risk Flag  
A qualitative categorization:  
- **High Risk**: Top supplier > 50% or volatility > 0.5  
- **Moderate Risk**: Volatility between 0.3 and 0.5  
- **Low Risk**: Top supplier < 30% and volatility < 0.3

---

## 📂 How To Use It

### 🔗 Try the App  
👉 [**Launch ResiliLytics App**](https://resililytics-app.streamlit.app/)

---

### 📤 Upload Your Data  
1. Prepare a `.csv` or `.xlsx` file with your supply chain data  
2. Upload it via the app interface  
3. Let ResiliLytics auto-generate your resilience score and action plan

Need help? Download a sample template below.

---

### ⬇️ Download Sample Template  
📥 [Sample Template (CSV)](https://raw.githubusercontent.com/AuraFusion/ResiliLytics/main/sample_template.csv)  
📥 [Sample Template (Excel)](https://raw.githubusercontent.com/AuraFusion/ResiliLytics/main/sample_template.xlsx)  
*(Right-click → “Save link as…”)*

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) — UI & dashboard framework  
- [Python](https://www.python.org/) — Core backend logic  
- [Plotly](https://plotly.com/python/) — Interactive visualizations  
- [GitHub](https://github.com/) — Version control and deployment  
- [Streamlit Cloud](https://streamlit.io/cloud) — Hosting  
- [Formspree](https://formspree.io/) — Contact form integration  

---

## 👩🏽‍💼 Use Case

This pilot app was developed to support academic and professional research on improving SME supply chain resilience through intelligent systems.  
Areas of focus include:
- 📊 Innovation in supply chain analytics  
- 🌍 National interest and resilience  
- 🚀 Entrepreneurial empowerment  

📌 The app is free to use for testing, learning, and research purposes.

---

## 📬 Contact

Have feedback, suggestions, or want to collaborate?

👉 Go to the **Contact** tab in the app and fill out the form — your message will be securely delivered via [Formspree.io](https://formspree.io).

> 🛡️ To improve spam protection, honeypot fields and Google reCAPTCHA are enabled on the form. 

---

> 🧡 *Built to help resilient entrepreneurs build resilient supply chains.*
