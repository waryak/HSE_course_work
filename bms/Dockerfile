FROM node:alpine

RUN apk add --no-cache build-base && \
    apk add --no-cache python3 python3-dev postgresql-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    rm -r /root/.cache

ENV PYTHONBUFFERED 1

RUN mkdir /config
ADD requirements.txt /config/
RUN pip install -r /config/requirements.txt

RUN apk add --no-cache curl

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN mkdir /bms
RUN mkdir /bms/data
ADD . /bms
WORKDIR /bms

RUN apk add --no-cache --virtual .gyp \
        python \
        make \
        g++ \
    && npm install /bms/jeth/ \
    && apk del .gyp

EXPOSE 8000
