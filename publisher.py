#!/usr/bin/env python3

import time
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost",1883,60)
i = 0
while True:
    client.publish("topic/Ramp1", i);
  #  client.publish("topic/2", "200 | 350 | 420 | 110");
  #  client.publish("topic/3", "200 | 350 | 420 | 110");
    time.sleep(1)
    i = i + 1
client.disconnect();