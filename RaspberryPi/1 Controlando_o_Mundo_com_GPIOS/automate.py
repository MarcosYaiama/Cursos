#Modulo para controlar as GPIOS
import RPi.GPIO as GPIO

#Para pegar os argumentos passados pelo na chamada do programa via terminal
import sys

def inicializaProboard():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

def define_pino_como_saida(porta):
    GPIO.setup(porta, GPIO.OUT)

def escreve_para_porta(numero_pino, estado_porta):
    GPIO.output(numero_pino, estado_porta)

#Setado pela linha de comando 
numero_pino = int(sys.argv[1])
estado_porta = int(sys.argv[2])

print(sys.argv)

inicializaProboard()
define_pino_como_saida(numero_pino)
escreve_para_porta(numero_pino, estado_porta)
