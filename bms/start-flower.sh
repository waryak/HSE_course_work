#!/usr/bin/env bash
flower -A bms --address=0.0.0.0 --port=5555 --basic_auth=bms:bms-secret-password
