import pika

class Cluster:
    def __init__(self, url: str):
        """
        Used to initialize cluster with full AMQP URL.

        :param url: AMQP URL in format amqp://user:password@host/
        :type url: str
        """
        self.URL = url
        self.RMQPARAMETERS = pika.URLParameters(url)
        print('Cluster was initialized using url:', url)


    def establish_connection(self):
        """
        Used to establish AMQP connection.
        """
        self.connection = pika.BlockingConnection(self.RMQPARAMETERS)
        self.channel = self.connection.channel()
        return self.connection, self.channel


    def close_connection(self):
        """
        Used to close AMQP connection.
        """
        return self.connection.close()
