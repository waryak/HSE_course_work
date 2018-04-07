Install & run Rabbit
-

First, we need to install RabbitMQ, which provides a broker for consuming and publishing messages.

MacOS: 

``brew install rabbitmq`` - Download

`brew services start rabbitmq` - Run server

Ubuntu:

``wget -O- https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc |
     sudo apt-key add -``  
``wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -``  
``sudo apt-get update``  
``apt-get install rabbitmq-server``  
``service rabbitmq-server start``  


Install **pika** and run publisher with consumer
-

Then, install all libs from `requirements.txt`:

`pip install -r requirements.txt`

Now we are ready to consume or publish!

Consume:

`python[3] recieve.py`

Publish:

`python[3] send.py <message>`


