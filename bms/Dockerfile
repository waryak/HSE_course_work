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
