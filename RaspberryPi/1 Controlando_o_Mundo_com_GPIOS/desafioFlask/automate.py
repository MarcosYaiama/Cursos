#Modulo para controlar as GPIOS
import RPi.GPIO as GPIO

#Para pegar os argumentos passados pelo na chamada do programa via terminal
import sys

def inicializaBoard():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

def define_pino_como_saida(porta):
    GPIO.setup(porta, GPIO.OUT)

def escreve_para_porta(numero_pino, estado_porta):
    inicializaBoard()
    define_pino_como_saida(numero_pino)
    GPIO.output(numero_pino, estado_porta)

def resetar():
    GPIO.cleanup()
    print("PORTAS RESETADAS")
