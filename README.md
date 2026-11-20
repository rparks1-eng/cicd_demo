# CI/CD Demonstration

OIM3641 Activity 17. Python 3.11, uv, Black and the Google GenAI SDK.

```sh
uv sync --locked
uv run black --check .
uv run python demo_make_llm_call.py
```

The instructor workflow expects `demo_make_llm_call.py` and `loan_payment.py`,
while the current class example uses different names. This project matches the
workflow filenames. The fixed Gemini request is bounded to 1,200 output tokens
and a 45-second request timeout. The result is parsed for Python syntax and
saved, never executed. `GEMINI_API_KEY` is a repository Actions secret, not a file
in Git. Repository permissions are read-only for the job, concurrency is one,
and the job timeout is three minutes. Disable the workflow from Actions to stop
future calls. This is a class demonstration, not a deployed service.
