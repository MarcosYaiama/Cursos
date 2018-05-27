import paho.mqtt.subscribe as subscribe

while(1):
    print("Esperando a mensagem!")
    msg = subscribe.simple("nickgat", hostname="iot.eclipse.org", msg_count=1)
    print("Mensagem: " + str(msg.payload))