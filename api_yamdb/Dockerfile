FROM python:3.7-slim

WORKDIR /app

COPY api_yamdb/requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

RUN apt-get update && apt-get install -y postgresql-client

COPY . .

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000"]
