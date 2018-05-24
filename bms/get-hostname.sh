#!/usr/bin/env bash

FILE_NAME=$1

if [ ! -f $FILE_NAME ]; then
    HOST_NAME=$(curl http://rancher-metadata/2015-12-19/self/host/hostname)
    echo "Hostname: ${HOST_NAME}"
    echo $HOST_NAME > $FILE_NAME
fi
