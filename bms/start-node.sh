#!/usr/bin/env bash

FILE_NAME="./data/queue_name.txt"
bash get-hostname.sh ${FILE_NAME}
HOST_NAME=$(cat ${FILE_NAME})
node jeth/main.js > jeth.log &
celery -A bms worker -Q ${HOST_NAME} --time-limit 30 --concurrency=1 -l info
