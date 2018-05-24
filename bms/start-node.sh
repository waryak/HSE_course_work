#!/usr/bin/env bash

FILE_NAME="./data/queue_name.txt"
./get-hostname.sh $FILE_NAME
HOST_NAME=$(cat $FILE_NAME)
celery -A bms worker -Q $HOST_NAME --time-limit 30 --concurrency=1 -l info
