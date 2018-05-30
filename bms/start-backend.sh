#!/usr/bin/env bash

NAME="bms-backend"                                  # Name of the application
DJANGODIR=/bms             # Django project directory
USER=root                                        # the user to run as
GROUP=root                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=bms.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=bms.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create migrations and apply them
python manage.py migrate --settings=$DJANGO_SETTINGS_MODULE
# python manage.py loaddata initial_data.json --settings=$DJANGO_SETTINGS_MODULE

FILE_NAME="./data/queue_name.txt"
bash get-hostname.sh $FILE_NAME
HOST_NAME=$(cat $FILE_NAME)
celery -A bms worker -Q $HOST_NAME --time-limit 30 --concurrency=1 -l info > celery.log &

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=0.0.0.0:8000 \
  --log-level=error \
  --log-file=-
