# #Import de las liberrias del BCM
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#importlo la libreria del LCD como charLCD
from RPLCD import CharLCD

#configuracion de entrada del pulsador   
pulsador = 4
GPIO.setup(pulsador,GPIO.IN)

flag = 0
t1 = 8
t2 = 0

#funcion que llama el evento de interrupcion
def interrupcion(pulsador):
	start_time = time.time()
	if (flag == 0):
		global flag
		flag = 1
		#print ('Empieza a contar el timepo de juego')
		lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23]) 
		lcd.write_string(u'Ready!')
	else:
		global t2
		t2 = time.time() - start_time


try:
	GPIO.add_event_detect(pulsador, GPIO.RISING, callback=interrupcion, bouncetime=200)
	if(t2 != 0 ):
		tiempo_juego = 100 - |t2 - t1| / 100
		if (tiempo_juego>95):
			GPIO.output(13, 1) #13 es un número cualquiera, undefined alarma
		else:
			lcd.write_string(u'No acertaste!')
	else:
		print("Aún no se ha presionado el pulsador, pulselo para empezar")

finally:
	GPIO.cleanup()