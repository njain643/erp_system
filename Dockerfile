FROM python:3.7-alpine
MAINTAINER Nikhil

ENV PYTHONUNBUFFERED 1
EXPOSE 80

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
