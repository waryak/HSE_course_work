import pika

url = 'amqp://wbetlvmi:4XFlePOe7o3lKdkiPlcRZATBsdaHiywC@golden-kangaroo.rmq.cloudamqp.com/wbetlvmi'

params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

# print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

