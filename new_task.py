#!/usr/bin/env python
import sys

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel =  connection.channel()


channel.queue_declare(queue='hello')

greet = ' '.join(sys.argv[:1]) or 'This is a massage'

channel.basic_publish(exchange='', routing_key='hello', body=greet)

print(" [x] Sent ", greet)


connection.close()