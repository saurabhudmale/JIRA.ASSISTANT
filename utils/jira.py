import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_jira_ticket(ticket_id):
    url = f"{os.getenv('JIRA_BASE_URL')}/rest/api/latest/issue/{ticket_id}"
    auth = (os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))
    headers = {"Accept": "application/json"}

    res = requests.get(url, auth=auth, headers=headers)

    if res.status_code != 200:
        raise Exception(f"Failed to fetch Jira issue: {res.status_code} - {res.text}")

    data = res.json()
    title = data["fields"]["summary"]
    description = data["fields"]["description"]

    return title, description

def search_jira(query):
    url = f"{os.getenv('JIRA_BASE_URL')}/rest/api/latest/search"
    params = { "jql": query }
    auth = (os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))
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