FROM python:3.13-slim-trixie

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./src /app

CMD ["python", "/app/app.py"]