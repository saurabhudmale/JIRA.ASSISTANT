import streamlit as st
from gpt_logic.gpt import gpt_request

st.set_page_config(page_title="🏠 Jira Assistant Dashboard", layout="wide")

st.title("🏠 Jira Assistant Dashboard")

st.markdown("Welcome to your **AI-powered Jira Assistant**! This app helps you streamline and automate key Jira workflows with the power of AI.")

if gpt_request(""):
    st.success("✅ Intelligence Awakened: AI is now online and ready to assist.")
else:
    st.error("⚠️ Our AI system is currently unavailable. We are working to resolve the issue as soon as possible.")

st.subheader("📋 Overview")
st.markdown("""
This tool provides a suite of AI-assisted features for Jira ticket management, including:

- 🔍 **Ticket Summarizer** – Instantly generate concise summaries of long Jira tickets using GPT.
- 🧪 **Test Case Generator** – Automatically generate test cases based on Jira ticket descriptions.
- 💬 **Comment Drafter** – Draft intelligent Jira comments using AI based on context.
- 📈 **Sprint Report Generator** – Build agile sprint reports from issue history and metadata.
- 🔎 **JQL Builder** – Generate and test JQL (Jira Query Language) expressions with AI assistance.

---
""")

st.subheader("🔐 Authentication")
st.markdown("""
Before using the tools, please enter your Jira credentials on the **Jira Credentials** tab:

- Your **Jira domain**
- The **email** used with Jira
- A valid **Jira API token**

Once saved, these credentials will be used across all tabs securely within this session.

---
""")

st.subheader("🛡️ Security Notes")
st.markdown("""
- Credentials are stored only in memory (for your session).
- We do not log or permanently store any Jira information.
---
""")