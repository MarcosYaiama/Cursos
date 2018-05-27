
import paho.mqtt.client as mqtt

mqttc = mqtt.Client()
mqttc.connect("iot.eclipse.org", 1883)

while(1):
    n = input("Digite um valor: ")
    mqttc.publish("nickgat", n)
    mqttc.loop(2)
    if(n == "0"):
        break