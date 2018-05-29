FROM python:3.6
ENV PYTHONBUFFERED 1

RUN mkdir /config
ADD requirements.txt /config/
RUN pip install -r /config/requirements.txt

RUN apt update
RUN apt install celeryd -y

RUN mkdir /bms
RUN mkdir /bms/data
ADD . /bms
WORKDIR /bms


EXPOSE 8000


#FROM node:carbon
#
#RUN apt-get update && apt-get install -y software-properties-common
#
#RUN add-apt-repository ppa:jonathonf/python-3.6
#RUN apt-get update
#RUN apt-get install -y python3.6 python3.6-dev python3-pip
#
#RUN apt update && apt install celeryd -y
#
#RUN mkdir /bms && mkdir /bms/data
#ADD . /bms
#WORKDIR /bms
#
#ENV PYTHONBUFFERED 1
#
#RUN pip3 install -r /bms/requirements.txt
#RUN npm install /bms/jeth
#
#EXPOSE 8000


#FROM python:3.6
#
#ADD jeth/geth /usr/local/bin/
#
#
#RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install -y nodejs && \
#    apt-get install -y build-essential && apt-get install npm -y
#RUN node -v
#RUN npm -v
#RUN npm install -g npm && npm install -g n && n stable
#RUN node -v
#RUN npm -v
#
#
#ENV PYTHONBUFFERED 1
#RUN mkdir /config
#ADD requirements.txt /config/
#RUN pip install -r /config/requirements.txt
#
#RUN apt update && apt install celeryd -y
#
#
#RUN mkdir /bms && mkdir /bms/data
#ADD . /bms
#WORKDIR /bms
#
#RUN npm install /bms/jeth
#
#EXPOSE 8000


#FROM python:3.6
#
#ADD jeth/geth /usr/local/bin/
#
#ENV PYTHONBUFFERED 1
#
#RUN mkdir /config
#ADD requirements.txt /config/
#RUN pip install -r /config/requirements.txt
#
#RUN apt update
#RUN apt install celeryd -y
#
#RUN mkdir /bms
#RUN mkdir /bms/data
#ADD . /bms
#WORKDIR /bms
#
#EXPOSE 8000

#ENTRYPOINT ["geth", "--help"]
#ENTRYPOINT ["python3", "-c", "print('asd')"]


#FROM ethereum/client-go
#
#ENV PYTHONBUFFERED 1
#RUN apk add --no-cache build-base && apk add --no-cache python3 && \
#    python3 -m ensurepip && \
#    rm -r /usr/lib/python*/ensurepip && \
#    pip3 install --upgrade pip setuptools && \
#    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
#    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
#    rm -r /root/.cache && apk add --no-cache postgresql-dev && apk add --no-cache python3-dev
#
#RUN mkdir /config
#ADD requirements.txt /config/
#RUN pip3 install -r /config/requirements.txt
#
#RUN mkdir /bms
#RUN mkdir /bms/data
#ADD . /bms
#WORKDIR /bms
#
#EXPOSE 8000
#
#ENTRYPOINT ["bash", "start-node.sh"]


