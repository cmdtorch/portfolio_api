from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])


def send_visit_message(ip: str, country: str, platform: str):
    producer.send(
        'visits',
        {
            'ip': ip,
            'country': country,
            'platform': platform,
        }
    )