FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install pydantic[email]

COPY ./ /app
