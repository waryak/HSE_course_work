import pika
import time

class ClusterListener:
    def __init__(self, url: str, cluster_name: str,
            server_name: str, callback_function=None, connection=True):
        """
        Used to initialize cluster listener (or server listener).
        Name parameters are used to determine the queue.
        """
        self.URL = url
        self.RMQPARAMETERS = pika.URLParameters(url)
        self.CLUSTER = cluster_name
        self.SERVER = server_name
        if callback_function:
             self.CALLBACK_FUNCTION = callback_function
        else:
            self.CALLBACK_FUNCTION = self.default_callback_function
        print(f' [x] {cluster_name}:{server_name}: Server'\
               ' has been initialized')

        if connection: self.establish_connection()

    def establish_connection(self):
        """
        Used to establish AMQP connection.
        """
        self.connection = pika.BlockingConnection(self.RMQPARAMETERS)
        self.channel = self.connection.channel()
        print(f' [x] {self.CLUSTER}:{self.SERVER}: Connection to'\
               ' RabbitMQ established.')
        resp = self.channel.basic_consume(self.CALLBACK_FUNCTION,
                queue=f'{self.CLUSTER}:{self.SERVER}')
        return resp

    @staticmethod
    def default_callback_function(ch, method, properties, body):
        print(f' [x] {method.delivery_tag}: Messages received:\n'\
              f'    ch: {ch}\n'\
              f'    method: {method}\n'\
              f'    properties: {properties}'\
              f'    body: {body}')
        time.sleep(1)
        print(f' [x] {method.delivery_tag}: Done')
        ch.basic_ack(delivery_tag=method.delivery_tag)


    def start(self):
        """
        Used to call start_consume method for channel.
        """
        print(f' [x] {self.CLUSTER}:self.SERVER: Consuming started')
        return self.channel.start_consuming()
