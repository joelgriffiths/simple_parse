FROM python:3.10.4-slim

RUN mkdir /app
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "simple_parse.py"]