import json
from confluent_kafka import Producer

def create_producer():
    PRODUCER_CONFIG = {
        "bootstrap.servers": "localhost:9092"
    }
    return Producer(PRODUCER_CONFIG)  # type: ignore

def delivery_report(err, msg):
    if err:
        print(f" Delivery failed: {err}")
    else:
        print(f" Delivered {msg.value().decode("utf-8")}")


def send_data(data):
    value = json.dumps(data).encode("utf-8")
    producer = create_producer()
    producer.produce(
        topic="",
        value=value,
        callback=delivery_report  # type: ignore
                    )

    return producer.flush()