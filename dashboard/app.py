import streamlit as st
import json
import os

st.title("🛡️ INTELPATCH – Cyber Threat Intelligence Engine")

report_files = [f for f in os.listdir("data/reports/") if f.endswith(".json")]
selected = st.selectbox("Select Report", report_files)

with open(f"data/reports/{selected}") as f:
    report = json.load(f)

st.json(report)