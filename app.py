import streamlit as st
from utils.extract_text import extract_text_from_file
from agent.validator_agent import validate_contract
import tempfile

st.title("📑 Contract Validator Agent")

uploaded = st.file_uploader("Upload Contract File", type=["pdf", "docx"])
if uploaded:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded.read())
        tmp_path = tmp.name

    st.success("📄 File uploaded successfully!")
    text = extract_text_from_file(tmp_path)

    if st.button("Run Validation"):
        result = validate_contract(text)

        st.subheader("🛠️ Rule-Based Issues")
        for issue in result["rule_issues"]:
            st.warning(issue)

        st.subheader("💡 LLM Feedback")
        st.info(result["llm_feedback"])

        st.download_button("⬇️ Download Report", result["llm_feedback"], file_name="llm_feedback.txt")
