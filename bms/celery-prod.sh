#!/usr/bin/env bash
celery -A bms worker -Q queue1 --time-limit 30 --concurrency=1 -l info
