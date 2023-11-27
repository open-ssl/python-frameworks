FROM python:3.9.18-alpine3.18

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["gunicorn", "--bind", "0.0.0.0:3002",  "wsgi:app"]
