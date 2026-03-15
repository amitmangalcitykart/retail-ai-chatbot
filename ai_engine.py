from anthropic import Anthropic
import os
import streamlit as st

client = Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

def generate_sql(question):

    prompt = f"""
You are a Snowflake SQL generator.

Table: MARGIN

Column Mapping:
"c1"=SITECODE
"c2"=STORE_NAME
"c3"=STORE_STATUS
"c4"=CLUSTER_TYPE
"c5"=REGION_TYPE
"c6"=BILL_DATE
"c7"=BILL_MONTH
"c8"=ICODE
"c9"=DIVISION
"c10"=SECTION
"c11"=DEPARTMENT
"c12"=ARTICLE_NAME
"c13"=ATTRIBUTE1
"c14"=ITEM_NAME
"c15"=CAT2
"c16"=LAST_IN_RATE
"c17"=MRP
"c18"=SEASON
"c19"=DISPLAY
"c20"=BILLQTY
"c21"=NETAMT
"c22"=TAXAMT
"c23"=COSTAMOUNT
"c24"=STORE_TAG
"c25"=PROJECT_FILTER
"c26"=STORE_TEHSIL_FILTER
"c27"=WEEK
"c28"=PROMOTION_TYPE
"c29"=MC_STATUS_AUG_24
"c30"=MC_LISTING_AUG_24

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
