import pika

class Cluster:
    def __init__(self, url: str, name: str, connection=True):
        """
        Used to initialize cluster with full AMQP URL. Name parameter is used to create an exchange for all queues.
        """
        self.URL = url
        self.RMQPARAMETERS = pika.URLParameters(url)
        self.servers = []
        self.NAME = name
        print(' [x] Cluster was initialized using url:', url)
        if connection: self.establish_connection()


    def establish_connection(self):
        """
        Used to establish AMQP connection.
        """
        self.connection = pika.BlockingConnection(self.RMQPARAMETERS)
        self.channel = self.connection.channel()
        print(' [x] Connection to RabbitMQ established.')
        resp = self.channel.exchange_declare(
                exchange=self.NAME,
                exchange_type='direct')
        print(' [x] Exchange "{}" created.'.format(self.NAME))
        return self.connection, self.channel, resp


    def clean(self):
        """
        Used to remove all declared queues and exchanges.
        """
        for server in self.servers:
            self.remove_server(name=server, remove_from_list=False)
        self.servers = []
        self.channel.exchange_delete(exchange=self.NAME)
        print(' [x] Exchange "{}" deleted.'.format(self.NAME))


    def close_connection(self, clean=True):
        """
        Used to close AMQP connection.
        """
        if clean: self.clean()
        resp_close = self.connection.close()
        print(' [x] Connection to RabbitMQ closed.')
        return resp_close


    def add_server(self, name=None):
        """
        Used to add server to cluster. Literally adds name to list and declares a queue with the name of server.
        """
        if not name:
            name = str(len(self.servers))
        if name in self.servers:
            raise Exception('This server already exists.')
        if name == 'all':
            raise Exception('Prohibited server name.')

        self.servers.append(name)

        resp_queue = self.channel.queue_declare(queue=name)

        resp_binding = self.channel.queue_bind(
                exchange=self.NAME,
                queue=name,
                routing_key=name)

        resp_binding_all = self.channel.queue_bind(
                exchange=self.NAME,
                queue=name,
                routing_key='all')

        print(' [x] Server "{}" added and queue binded.'.format(name))
        return resp_queue, resp_binding, resp_binding_all


    def remove_server(self, name, remove_from_list=True):
        """
        Used to remove servers from cluster. Literally removes name from list and removes queue with the name of server.
        """
        if name not in self.servers:
            print(' [ ] There is no server with the name "{}".'.format(name))
            return
        resp = self.channel.queue_delete(queue=name)
        if remove_from_list: self.servers.remove(name)
        print(' [x] Server and queue "{}" removed.'.format(name))
        return resp
