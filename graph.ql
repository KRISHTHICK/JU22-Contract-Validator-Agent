contract-validator-agent/
├── app.py                     # Main Streamlit app
├── agent/
│   └── validator_agent.py     # Core logic combining rules + LLM
├── utils/
│   ├── extract_text.py        # Extract text from PDFs/DOCX
│   ├── rules.py               # Rule-based checks
│   └── llm_validator.py       # LLM-based suggestions
├── samples/
│   └── sample_contract.pdf    # Sample test file
├── requirements.txt
└── README.md
