"""Generate a loan-payment Python file; never execute the generated code."""
import ast
import os
import re
from pathlib import Path
from dotenv import load_dotenv
from google import genai

load_dotenv()

def main():
    if not os.getenv("GEMINI_API_KEY"):
        raise RuntimeError("GEMINI_API_KEY is not configured in repository secrets")
    client=genai.Client(api_key=os.environ["GEMINI_API_KEY"],http_options={"timeout": 45000})
    response=client.models.generate_content(model="gemini-3.1-flash-lite",contents="Write a Python function loan_payment(interest, term, present_value). Interest is an annual decimal rate, term is months. Handle zero interest and reject invalid negative input. Return only Python in one fenced code block. Do not import packages, access files, execute commands or make network calls.",config={"max_output_tokens":1200,"temperature":0})
    match=re.search(r"```(?:python)?\s*\n(.*?)```",response.text or "",re.S)
    if not match:
        raise ValueError("Expected one fenced Python code block")
    code=match.group(1).strip()+"\n"
    ast.parse(code)
    Path("loan_payment.py").write_text(code)
    print("Generated loan_payment.py; Python syntax validated. Generated code was NOT executed.")

if __name__=="__main__":
    main()
