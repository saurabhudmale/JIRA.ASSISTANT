import streamlit as st
import pandas as pd

from gpt_logic.jira_gpt import generate_jql
from utils.jira import search_jira

st.set_page_config(layout="wide")

st.title("🧠 JQL Generator")

st.markdown("Type your request in natural English, and I'll generate a JQL query for you.")

# Text input
prompt = st.text_area("🔍 What do you want to search in Jira?", height=100)

if st.button("Generate JQL"):
    if not prompt.strip():
        st.warning("Please enter a valid prompt.")
    else:
        with st.spinner("Generating JQL..."):
            try:
                jql = generate_jql(prompt)
                st.code(jql, language='sql')
                with st.spinner("Fetching Jira tickets..."):
                    st.markdown("The following are the 50 records retrieved from the above query")
                    tickets = search_jira(jql)
                    df = pd.DataFrame(tickets)
                    st.dataframe(df, use_container_width=True)
            except Exception as e:
                st.error(f"Error: {e}")
