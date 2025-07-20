import requests
import streamlit as st

st.set_page_config(layout="wide")

if "domain" not in st.session_state or "email" not in st.session_state or "api_key" not in st.session_state:
    st.error("Please set your Jira domain, email, and API key in the **JIRA Credentials** page.")
    st.stop()
else:
    JIRA_BASE_URL = st.session_state["domain"]
    JIRA_EMAIL = st.session_state["email"]
    JIRA_API_TOKEN = st.session_state["api_key"]
    auth = (JIRA_EMAIL, JIRA_API_TOKEN)

def fetch_jira_ticket(ticket_id):
    url = f"{JIRA_BASE_URL}/rest/api/latest/issue/{ticket_id}"
    headers = {"Accept": "application/json"}

    res = requests.get(url, auth=auth, headers=headers)

    if res.status_code != 200:
        raise Exception(f"Failed to fetch Jira issue: {res.status_code} - {res.text}")

    data = res.json()
    title = data["fields"]["summary"]
    description = data["fields"]["description"]

    return title, description

def search_jira(query):
    url = f"{JIRA_BASE_URL}/rest/api/latest/search"
    params = { "jql": query }
    headers = {"Accept": "application/json"}

    res = requests.get(url, params=params, auth=auth, headers=headers)

    if res.status_code != 200:
        raise Exception(f"Failed to fetch Jira issue: {res.status_code} - {res.text}")

    data = res.json()

    tickets = []

    for issue in data["issues"]:
        ticket_info = {
            "Key": issue["key"],
            "Summary": issue["fields"]["summary"],
            "Status": issue["fields"]["status"]["name"]
        }
        tickets.append(ticket_info)

    return tickets