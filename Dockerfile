FROM python:3.7

RUN apt-get update && apt-get install -y gettext
RUN mkdir /code
COPY . /code/
WORKDIR /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=true
