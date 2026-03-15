import oracledb
from sqlalchemy import create_engine
import streamlit as st

# enable thick mode
oracledb.init_oracle_client(
    lib_dir=r"C:\oracle\instantclient_19_24\instantclient_23_0"
)

DB_URL = "oracle+oracledb://Report:Report@10.0.0.15:1521/?service_name=Ginesys"

@st.cache_resource
def get_engine():
    return create_engine(DB_URL, pool_size=10, max_overflow=20)

engine = get_engine()

# Test connection
try:
    with engine.connect():
        st.success("✅ Oracle Connected Successfully")
except Exception as e:
    st.error(f"❌ Connection Error: {e}")