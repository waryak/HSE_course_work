How to localy run project
-
* Install redis: `https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04`
* Install python requirements:
`pip3 install -r bms/requirements.txt`
* Install npm
`apt install npm`
* Install js requirements:
`cd jeth && npm install`
* Run django app:
`python3 bms/manage.py runserver 8000`
* Run celery:
`celery -A bms worker -Q queue_name`
* Run node app:
`node jeth/main.js`
