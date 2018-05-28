FROM ethereum/client-go as go_eth

FROM python:3.6

COPY --from=go_eth /usr/local/bin/ /usr/local/bin/

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


#FROM python:3.6
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
#
#EXPOSE 8000
