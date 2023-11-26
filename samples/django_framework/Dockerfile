FROM python:3.9.18-alpine3.18

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT ["python", "./manage.py"]

CMD ["runserver", "0.0.0.0:3001", "--noreload"]
