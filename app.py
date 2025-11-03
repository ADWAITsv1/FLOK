# app.py

import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(page_title="FLOK Dashboard", layout="wide")

st.title("FLOK – Food Loss On Chain")
st.subheader("Live Batch Monitoring & Blockchain Reroute Log")

# Load food batch data
batch_df = pd.read_csv("data/food_batches_shibuya.csv")
st.write("### 📦 Current Food Batches")
st.dataframe(batch_df)

# Load blockchain log safely
log_path = "blockchain_log.json"
if os.path.exists(log_path) and os.path.getsize(log_path) > 0:
    with open(log_path, "r") as f:
        blockchain = json.load(f)
    log_df = pd.DataFrame(blockchain)

    st.write("### 🔗 Blockchain Log of Rerouted Items")
    st.dataframe(log_df)

    if not log_df.empty:
        st.write("### 📊 Reroute Summary")
        col1, col2 = st.columns(2)
        with col1:
            st.bar_chart(log_df["RecommendedReceiver"].value_counts())
        with col2:
            st.bar_chart(log_df["RiskLevel"].value_counts())

else:
    st.warning("No blockchain log found or it's empty. Run flok_blockchain.py first.")
