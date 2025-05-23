from app.prompt_templates import PROMPT_TEMPLATE
import os

def generate_sql_with_mode(question: str, use_llm: bool) -> str:
    if use_llm:
        return llm_generate_sql(question)
    else:
        return rule_based_generate_sql(question)

def llm_generate_sql(question: str) -> str:
    from openai import OpenAI
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "-- ❌ ERROR: OPENAI_API_KEY not set"
    client = OpenAI(api_key=api_key)
    prompt = PROMPT_TEMPLATE.format(question=question)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"-- ❌ ERROR calling OpenAI: {str(e)}"

def rule_based_generate_sql(question: str) -> str:
    q = question.lower()
    if "diabetes" in q:
        return """SELECT person_id, condition_start_date
FROM condition_occurrence
WHERE condition_concept_id = 201826
AND condition_start_date >= date('now', '-1 year');"""
    elif "blood pressure" in q:
        return """SELECT person_id, measurement_date, value_as_number
FROM measurement
WHERE measurement_concept_id = 3012888;"""
    else:
        return "-- ❌ Sorry, I couldn't understand this question."

# 🔁 Wrapper for compatibility with main.py
def generate_sql_from_prompt(prompt: str) -> str:
    return generate_sql_with_mode(prompt, use_llm=True)
