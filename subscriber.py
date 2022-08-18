#!/usr/bin/env python3

import paho.mqtt.client as mqttClient
import time
import json
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        client.subscribe("iotgateway", 0)


    else:
        print("Connection failed")

def on_message(client, userdata, message):
    # ENABLE THIS LINE FOR BASIC READING MQTT SUBSCRIPTION FROM THE PUBLISHER CODE.
    print("Message received : "  + str(message.payload) + " on " + message.topic)
    # ENABLE THE FOLLOWING FOR CONVERTING JSON FILE FROM MACHINE DATA TO USEFUL VARIABLES.
    # res_dict = json.loads((message.payload).decode('utf-8'))
    # timestamp = (res_dict['timestamp'])
    # time_rec = (datetime.fromtimestamp(int(timestamp/1000)))
    # data_rec = res_dict['values'][0]['v']
    # print(time_rec, data_rec)


broker_address= "localhost"
port = 1883

client = mqttClient.Client()
client.on_connect= on_connect
client.on_message= on_message
client.connect(broker_address, port=port)
client.loop_start()


try:
    while True:
        time.sleep(0.5)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()