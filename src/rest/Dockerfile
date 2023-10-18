FROM python:3.8

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get -y update
RUN apt-get install -y curl nano wget nginx git

ENV ENV_TYPE staging
ENV MONGO_HOST mongo
ENV MONGO_PORT 27017
ENV DATABASE adb
ENV TODO_COLLECTION todos

ENV PYTHONPATH=$PYTHONPATH:/src/

COPY requirements.txt .

RUN pip install -r requirements.txt
