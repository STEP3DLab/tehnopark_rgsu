FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir poetry && poetry install --only main
CMD ["uvicorn", "entry_pass_generator.webhook:app", "--host", "0.0.0.0", "--port", "8080"]
