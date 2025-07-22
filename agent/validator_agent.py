from utils.rules import rule_based_validation
from utils.llm_validator import llm_validate

def validate_contract(text):
    rule_issues = rule_based_validation(text)
    llm_feedback = llm_validate(text)

    return {
        "rule_issues": rule_issues,
        "llm_feedback": llm_feedback
    }
