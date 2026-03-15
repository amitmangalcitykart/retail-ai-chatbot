import streamlit as st
import pandas as pd
from snowflake_conn import get_connection
from ai_engine import generate_sql
from charts import create_chart
from dashboard_layout import show_kpi_cards

st.set_page_config(layout="wide")

st.title("🤖 AI Data Chatbot")

# chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# user input
prompt = st.chat_input("Ask your business data")

if prompt:

    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append({"role":"user","content":prompt})

    # generate sql
    sql = generate_sql(prompt)

    with st.chat_message("assistant"):

        st.write("Generated SQL")
        st.code(sql)

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(sql)

        df = cursor.fetch_pandas_all()

        show_kpi_cards(df)

        chart = create_chart(df)

        if chart:
            st.plotly_chart(chart,use_container_width=True)

        st.dataframe(df)

    st.session_state.messages.append(
        {"role":"assistant","content":"Data returned"}
    )