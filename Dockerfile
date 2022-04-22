FROM python:3.9-alpine

MAINTAINER Thibault

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV FLASK_APP=api.py

CMD ["flask", "run"]
