How to localy run project
-
* Install redis: `https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04`
* Install python requirements:
`pip3 install -r bms/requirements.txt`

Install **pika** and run publisher with consumer
-

Then, install all libs from `requirements.txt`:

`pip install -r requirements.txt`

Now we are ready to consume or publish!

Consume:

`python[3] recieve.py`

Publish:

`python[3] send.py <message>`


