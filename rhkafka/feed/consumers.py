from confluent_kafka import Consumer
import json

consumer = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'feed_group',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(
    ['contractor.updated', 'ride.order.created', 'courier.order.created'])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    data = json.loads(msg.value().decode('utf-8'))
    print(f"Consumed message from {msg.topic()}: {data}")
    # Process and update feed state here

consumer.close()
