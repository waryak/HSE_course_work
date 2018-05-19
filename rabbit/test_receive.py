import listener

# your AMQP URL here
url = 'amqp://sjsdxfpv:xGPz8wIdxFkniJubTY7Yato9sXyx4TYJ@hound.rmq.cloudamqp.com/sjsdxfpv'

l = listener.ClusterListener(url=url, cluster_name='kek', server_name='0')
l.start()
