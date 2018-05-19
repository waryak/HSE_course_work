import manager

# your AMQP URL here
url = 'amqp://sjsdxfpv:xGPz8wIdxFkniJubTY7Yato9sXyx4TYJ@hound.rmq.cloudamqp.com/sjsdxfpv'

c = manager.ClusterManager(url=url, name='kek')
c.add_server()
c.add_server()
c.add_server()

c.send_message('some message here')

c.clean()
c.close_connection()
