FROM python:latest

MAINTAINER dubirajara

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /code/requirements.txt
RUN pip install -q -r /code/requirements.txt

COPY . /code/
WORKDIR /code/

EXPOSE 8000