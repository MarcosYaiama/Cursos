import paho.mqtt.client as mqtt
from time import sleep
from random import randint
mqttc = mqtt.Client()
mqttc.connect("192.168.1.45", 1883)
while(1):
    for i in range(200,-1,-1):
        mqttc.publish("nickWmV", i)
        print(str(i))
        sleep(1)
    break

print("FIM DO PROGRAMA")

mqttc.loop(2)