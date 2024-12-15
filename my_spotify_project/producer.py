import json
from kafka import KafkaProducer

def load_playlists(file_path):
    """Load playlists data from a JSON file"""
    with open(file_path) as file:
        return json.load(file)
    
def load_credentials(credentials_path):
    """Getting just de API address"""
    with open(credentials_path) as file:
        return json.load(file)
    

def send_to_kafka(playlists, topic = 'playlists', bootstrap_servers='localhost:9092'):
    """_summary_

    Send playlist data to Kafka.
    
    Args:
        playlists (_type_): _description_
        topic (str, optional): _description_. Defaults to 'playlists'.
        bootstrap_servers (str, optional): _description_. Defaults to 'localhost:9092'.
    """
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    
    for playlist in playlists['items']:
        producer.send(topic, value=playlist)

    producer.flush()
    producer.close()
    print("Data successfuly sent to Kafka!")

if __name__ == '__main__':
    playlists_data = load_playlists('playlists.json')
    send_to_kafka(playlists_data)
    credentials_path = 'credentials.json'
    load_credentials(credentials_path)
    print(credentials_path)

