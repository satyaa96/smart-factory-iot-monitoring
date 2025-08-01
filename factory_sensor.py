import ssl
import time
import json
import random
import paho.mqtt.client as mqtt

# AWS IoT endpoint (replace with yours)
endpoint = "a1e5i9tbhg3ut4-ats.iot.ap-northeast-1.amazonaws.com"
  # Replace this line

# Thing and topic
thing_name = "FactorySensor1"
topic = f"factory/{thing_name}/data"

# Paths to certs
ca_path = "AmazonRootCA1.pem"
cert_path = "cert.pem.crt"
key_path = "private.pem.key"

# MQTT client
client = mqtt.Client()
client.tls_set(ca_certs=ca_path,
               certfile=cert_path,
               keyfile=key_path,
               tls_version=ssl.PROTOCOL_TLSv1_2)

def connect():
    print("Connecting to AWS IoT...")
    client.connect(endpoint, 8883, 60)
    print("Connected.")

def publish_sensor_data():
    while True:
        payload = {
            "device": thing_name,
            "temperature": round(random.uniform(20, 80), 2),
            "humidity": round(random.uniform(30, 90), 2),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        client.publish(topic, json.dumps(payload), qos=1)
        print("Published:", payload)
        time.sleep(5)

connect()
publish_sensor_data()
