# JU22-Contract-Validator-Agent
Gen AI

Project Topic: "Contract Validator Agent"
An intelligent agent that validates uploaded legal or policy contracts for compliance, clarity, and completeness using a combination of rule-based checks and LLM reasoning.

💡 Features:
📄 Upload legal contracts in PDF or DOCX format.

🔍 Validate:

Missing required clauses (rule-based)

Ambiguous or risky language (LLM-based)

Specific fields like parties involved, dates, terms, signatures.

✅ Output:

Audit summary

Suggestions for improvement

JSON output

🤖 Includes a Validator Agent that runs both rules + LLM checks

🖼️ Streamlit UI with upload, result viewer, and export.



# 🧠 Contract Validator Agent

A lightweight AI agent that checks legal/policy documents using:
- ✅ Rule-based validation
- 🤖 LLM-based feedback (GPT-3.5 or GPT-4)

## 💻 Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
