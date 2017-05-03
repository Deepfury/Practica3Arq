# #Import de las liberrias del BCM
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#importlo la libreria del LCD como charLCD
from RPLCD import CharLCD


#abrir el archivo de texto
with open("archivo.txt") as archivo:
	datos = archivo.read()
	datos.lower()
	print(datos)


contador_hot = datos.count("hot")

# for i in datos:
# 	palabras = i.split()
# 	if(palabras == 'hot'):
# 		contador_hot =+ 1


#punto 5
print("El numero de 'hot' es:" + str(contador_hot))