Install & run Rabbit
-

First, we need to install RabbitMQ, which provides a broker for consuming and publishing messages.

MacOS: 

``brew install rabbitmq`` - Download

`brew services start rabbitmq` - Run server

Ubuntu:


 --



Install **pika** and run publisher with consumer
-

Then, install all libs from `requirements.txt`:

`pip install -r requirements.txt`

Now we are ready to consume or publish!

Consume:

`python[3] recieve.py`

Publish:

`python[3] send.py <message>`


