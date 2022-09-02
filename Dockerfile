FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /missal
WORKDIR /missal
ADD . /missal
RUN pip install -r requirements.txt
