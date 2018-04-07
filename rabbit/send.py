import sys
import pika

url = 'amqp://wbetlvmi:4XFlePOe7o3lKdkiPlcRZATBsdaHiywC@golden-kangaroo.rmq.cloudamqp.com/wbetlvmi'

params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()


channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=sys.argv[1])
print(" [x] Sent '" + sys.argv[1] + "'")
connection.close()
