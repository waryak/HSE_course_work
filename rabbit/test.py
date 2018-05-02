import cluster

# your AMQP URL here
url = 'amqp://sjsdxfpv:xGPz8wIdxFkniJubTY7Yato9sXyx4TYJ@hound.rmq.cloudamqp.com/sjsdxfpv'

c = cluster.Cluster(url=url, name='some cluster name')
c.add_server()
c.add_server()
c.add_server()
c.clean()
c.close_connection()
