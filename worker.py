#!/usr/bin/env python
import time

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()


# channel.queue_declare(queue='hello')

# greet = 'Hello, World!'

# channel.basic_publish(exchange='', routing_key='hello', body=greet)

# print(" [x] Sent ", greet)

def callback(ch, method, properties, body):

    print(f" [x] Received {body.decode()}")

    time.sleep(body.count(b'.'))

    print("[x] done")




channel.basic_consume(queue='hello', on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')


channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)