#Modulo para controlar as GPIOS
import RPi.GPIO as GPIO
#Modulo para dar "sleep"
from time import sleep

#O setando o modo como identificaremos os pinos
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)

#Impedir que a GPIO fique jogando mensagens na tela
GPIO.setwarnings(False)

#Definindo pinos
GPIO.setup(7, GPIO.OUT)



GPIO.output(7, GPIO.HIGH)
sleep(1)
GPIO.output(7, GPIO.LOW)
sleep(1)

#Reseta todas as configuracoes setadas pelo script ao final da execucao
GPIO.cleanup()
