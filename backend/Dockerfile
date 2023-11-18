FROM python:3.10-slim

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /app

EXPOSE 5002

ENV PYTHONPATH "${PYTHONPATH}:/app/submissions"

CMD ["python", "submissions/main.py"]