from anthropic import Anthropic
import os
import streamlit as st

client = Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

def generate_sql(question):

    prompt = f"""
You are a Snowflake SQL generator.

Table: MARGIN

Column Mapping:
"c1" = SITECODE
"c2" = STORE_NAME
"c5" = REGION
"c9" = DEPARTMENT
"c6" = BILL_DATE
"c20" = BILLQTY
"c21" = NETAMT
"c22" = COSTAMOUNT

Always use column names with double quotes like "c1","c2".

Convert the question into Snowflake SQL.

Question:
{question}

Return only SQL.
"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt + question}]
    )

    sql = response.content[0].text

    # clean SQL
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql
