import streamlit as st

def show_kpi_cards(df):

    cols = st.columns(3)

    if "NETAMT" in df.columns:
        cols[0].metric("Total Sales", int(df["NETAMT"].sum()))

    if "BILLQTY" in df.columns:
        cols[1].metric("Total Quantity", int(df["BILLQTY"].sum()))

    if "COSTAMOUNT" in df.columns:
        margin = df["NETAMT"].sum() - df["COSTAMOUNT"].sum()
        cols[2].metric("Margin", int(margin))