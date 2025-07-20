import streamlit as st

st.set_page_config(page_title="🔐 Jira Credentials", layout="wide")

st.info("👉 Make sure your Jira API token has sufficient permissions for reading/updating issues.")

with st.form("jira_form"):
    st.subheader("Enter Jira Credentials")
    domain = st.text_input("Jira Domain (e.g., your-domain.atlassian.net)", value=st.session_state.get("domain", ""))
    email = st.text_input("Email", value=st.session_state.get("email", ""))
    api_key = st.text_input("API Key", type="password", value=st.session_state.get("api_key", ""))
    
    submitted = st.form_submit_button("Save Credentials")

    if submitted:
        if not domain or not email or not api_key:
            st.warning("All fields are required.")
        else:
            st.session_state["domain"] = domain
            st.session_state["email"] = email
            st.session_state["api_key"] = api_key
            st.success("✅ Credentials saved to session.")