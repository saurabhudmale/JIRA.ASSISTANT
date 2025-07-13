import streamlit as st

from gpt_logic.html_gpt import convert_to_html
from gpt_logic.jira_gpt import generate_test_cases
from utils.jira import fetch_jira_ticket

st.set_page_config(layout="wide")

st.title("🧪 Test Case Generator")

if "jira_id_input" not in st.session_state:
    st.session_state.jira_id_input = ""

jira_id = st.text_input(
    label="Enter Jira ID (e.g., PROJ-123)" if st.session_state.jira_id_input else "",
    placeholder="Enter Jira ID (e.g., PROJ-123)" if st.session_state.jira_id_input == "" else "",
    value=st.session_state.jira_id_input,
    key="jira_id_input"
)

if st.button("Generate Test Cases"):
    if not jira_id:
        st.warning("Please enter a Jira ID.")
    else:
        try:
            with st.spinner("Fetching Jira Story..."):
                title, description = fetch_jira_ticket(jira_id)

            with st.expander("Story Details", expanded=True):
                st.write(jira_id + " " + title, unsafe_allow_html=True)
                st.write("Description")
                st.write(convert_to_html(description), unsafe_allow_html=True)

            with st.spinner("Generating test cases..."):
                test_cases = generate_test_cases(title, description)

            with st.expander("Test Cases", expanded=True):
                st = st.container(border=True)
                st.write(test_cases, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")