import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path

st.set_page_config(page_title="Data Governance Portal", layout="wide")

DB_PATH = "metadata/metadata.db"

USERS = {
    "admin": {"password": "admin123", "role": "Admin"},
    "viewer": {"password": "viewer123", "role": "Viewer"}
}

def authenticate(username, password):
    if username in USERS and USERS[username]["password"] == password:
        return USERS[username]["role"]
    return None

if "role" not in st.session_state:
    st.session_state.role = None

if st.session_state.role is None:
    st.title("Enterprise Data Governance Portal")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        role = authenticate(username, password)
        if role:
            st.session_state.role = role
            st.success(f"Logged in as {role}")
            st.rerun()
        else:
            st.error("Invalid credentials")
    st.stop()

st.sidebar.success(f"Role: {st.session_state.role}")

conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT * FROM metadata_registry", conn)

st.title("Data Governance & Metadata Management Portal")

st.subheader("Dataset Registry")
st.dataframe(df)

selected_table = st.selectbox("Select Dataset", df["table_name"].unique())

table_info = df[df["table_name"] == selected_table]

st.subheader("Metadata Details")
st.write(table_info)

profile_path = Path(f"profiles/{selected_table}_profile.csv")

if profile_path.exists():
    profile_df = pd.read_csv(profile_path)
    st.subheader("Column Profiling")
    st.dataframe(profile_df)

report_path = Path(f"gx_reports/{selected_table}.html")

if report_path.exists():
    with open(report_path, "rb") as f:
        st.download_button(
            label="Download Great Expectations Report",
            data=f,
            file_name=f"{selected_table}_dq_report.html",
            mime="text/html"
        )

if st.session_state.role == "Admin":
    st.subheader("Admin Controls")
    st.info("Simulated governance admin actions")
    st.button("Approve Dataset")
    st.button("Trigger Validation")