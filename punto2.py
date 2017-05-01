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
t1 = 0

#funcion que llama el evento de interrupcion
def interrupcion(pulsador):
	start_time = time.time()
	if (flag == 0):
		global flag
		flag = 1
		#print ('Empieza a contar el timepo de juego')
		lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23]) 
		lcd.write_string(u'Empieza a contar el tiempo!')
	else:
		global t1
		t1 = time.time() - start_time


try:
	GPIO.add_event_detect(pulsador, GPIO.RISING, callback=interrupcion, bouncetime=200)
finally:
	GPIO.cleanup()