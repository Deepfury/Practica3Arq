# #Import de las liberrias del BCM
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#importlo la libreria del LCD como charLCD
from RPLCD import CharLCD

#configuracion de entrada del pulsador   
pulsador = 4
GPIO.setup(pulsador,GPIO.IN)

#definicion de variables
flag = 0
t1 = 4
t2 = 0
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
mensaje = 'Pulsa para empezar'

#funcion que llama el evento de interrupcion
def interrupcion(pulsador):
	start_time = time.time()
	global flag
	global mensaje
	global lcd
	if (flag == 0):
		flag = 1
		print ('Empieza a contar el timepo de juego') 
		lcd.clear()
		mensaje = 'Empieza a contar el tiempo'
	elif flag == 1:
		global t2
		flag = 2
		t2 = time.time() - start_time
		print(t1)
		print ('Tiempo:' + str(t2))
		lcd.clear()
		mensaje = 'Termina de contar'
	else:
		print('Tu tiempo es:' + str(t2))
		lcd.clear()
		mensaje = 'Ya tienes tu tiempo'


try:
	GPIO.add_event_detect(pulsador, GPIO.RISING, callback=interrupcion, bouncetime=200)
	if(t2 != 0 ):
		tiempo_juego = 100 - |t2 - t1| / 100
		if (tiempo_juego>95):
			GPIO.output(13, 1) #13 es un número cualquiera, undefined alarma
		else:
			lcd.write_string(u'No acertaste!')
	else:
		lcd.write_string(mensaje)

finally:
	GPIO.cleanup()
