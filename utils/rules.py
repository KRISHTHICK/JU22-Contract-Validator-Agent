def rule_based_validation(text):
    rules = {
        "Governing Law": "Check if governing law clause exists",
        "Termination Clause": "Check if termination clause is mentioned",
        "Confidentiality": "Ensure confidentiality clause exists"
    }

    missing = []
    for rule in rules:
        if rule.lower() not in text.lower():
            missing.append(f"Missing: {rule} - {rules[rule]}")

    return missing
