import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def llm_validate(text):
    prompt = f"""
    You are a legal assistant. Analyze the following contract text and identify:
    - Ambiguous or risky language
    - Suggestions for clarity
    - Missing standard clauses

    Contract:
    {text[:4000]}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{ "role": "user", "content": prompt }],
        temperature=0.2,
        max_tokens=500
    )

    return response['choices'][0]['message']['content']
