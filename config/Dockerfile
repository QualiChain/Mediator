FROM python:3.7-slim

RUN apt-get update && apt-get install -y netcat

WORKDIR /opt/qualichain_mediator

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD bash config/run.sh