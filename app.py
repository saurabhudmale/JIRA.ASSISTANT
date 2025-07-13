import streamlit as st

pages = [
    st.Page("pages/home.py", title="Home", default=True),
    st.Page("pages/ticket_summarizer.py", title="Ticket Summarizer"),
    st.Page("pages/test_case_generator.py", title="Test Case Generator"),
    st.Page("pages/comment_drafter.py", title="Comment Drafter"),
    st.Page("pages/sprint_report_assistant.py", title="Sprint Report Generator"),
    st.Page("pages/query_builder.py", title="JQL Builder"),
]

pg = st.navigation(pages, position="top")
pg.run()