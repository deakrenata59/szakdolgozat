FROM python:3.12.7-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=server.py

CMD ["flask", "run", "--host", "0.0.0.0"]