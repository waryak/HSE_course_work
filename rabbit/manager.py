import pika

class ClusterManager:
    def __init__(self, url: str, name: str, connection=True):
        """
        Used to initialize cluster with full AMQP URL.
        Name parameter is used to create an exchange for all queues.
        """
        self.URL = url
        self.RMQPARAMETERS = pika.URLParameters(url)
        self.servers = []
        self.NAME = name
        print(' [x] {}: Cluster was initialized using url: {}'.format(
            self.NAME, url))
        if connection: self.establish_connection()


    def establish_connection(self):
        """
        Used to establish AMQP connection.
        """
        self.connection = pika.BlockingConnection(self.RMQPARAMETERS)
        self.channel = self.connection.channel()
        print(' [x] {}: Connection to RabbitMQ established.'.format(self.NAME))
        resp = self.channel.exchange_declare(
                exchange=self.NAME,
                exchange_type='direct')
        print(f' [x] {self.NAME}: Exchange "{self.NAME}" created.')
        return resp


    def clean(self):
        """
        Used to remove all declared queues and exchanges.
        """
        for server in self.servers:
            self.remove_server(name=server, remove_from_list=False)
        self.servers = []
        self.channel.exchange_delete(exchange=self.NAME)
        print(' [x] {}: Exchange "{}" deleted.'.format(self.NAME, self.NAME))


    def close_connection(self, clean=True):
        """
        Used to close AMQP connection.
        """
        if clean: self.clean()
        resp_close = self.connection.close()
        print(' [x] {}: Connection to RabbitMQ closed.'.format(self.NAME))
        return resp_close


    def add_server(self, name=None, label=None):
        """
        Used to add server to cluster. Literally adds name to
        list and declares a queue with the name of server.
        Server could be labeled so the messages could be sent bt label.
        """
        if not name:
            name = str(len(self.servers))
        if name in self.servers:
            raise Exception(self.NAME + ': This server already exists.')
        if name == 'all':
            raise Exception(self.NAME + ': Prohibited server name.')

        self.servers.append(name)
        queue_name = '{}:{}'.format(self.NAME, name)
        resp_queue = self.channel.queue_declare(queue=queue_name)

        resp_binding = self.channel.queue_bind(
                exchange=self.NAME,
                queue=queue_name,
                routing_key=name)

        resp_binding_all = self.channel.queue_bind(
                exchange=self.NAME,
                queue=queue_name,
                routing_key='all')

        if label:
            resp_binding_label = self.channel.queue_bind(
                    exchange=self.NAME,
                    queue=queue_name,
                    routing_key=label
                    )
        else:
            resp_binding_label = None

        print(' [x] {}: Server "{}" added and queue binded.'.format(
            self.NAME, name))
        return resp_queue, resp_binding, resp_binding_all, resp_binding_label


    def remove_server(self, name, remove_from_list=True):
        """
        Used to remove servers from cluster. Literally removes name from
        list and removes queue with the name of server.
        """
        if name not in self.servers:
            print(' [ ] {}: There is no server with the name "{}".'.format(
                self.NAME, name))
            return
        queue_name = '{}:{}'.format(self.NAME, name)
        resp = self.channel.queue_delete(queue=queue_name)
        if remove_from_list: self.servers.remove(name)
        print(' [x] {}: Server and queue "{}" removed.'.format(
            self.NAME, name))
        return resp


    def send_message(self, body, server='all', label=None):
        """
        Used to send messages to the servers.
        """
        routing_key = label if label else f'{self.NAME}:{server}'
        resp = self.channel.basic_publish(exchange=self.NAME,
                      routing_key=server,
                      body=body)
        print(' [x] {}: Message "{}" sent with routing key {}.'.format(
            self.NAME, body, routing_key))
        return resp

