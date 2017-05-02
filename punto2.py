# #Import de las liberrias del BCM
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
#importlo la libreria del LCD como charLCD
from RPLCD import CharLCD

#configuracion de entrada del pulsador   
pulsador = 7
GPIO.setup(pulsador,GPIO.IN)

#definicion de variables
tiempo = 0
flag = 0
t1 = 0
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
mensaje = 'Pulsa para empezar'

#funcion que llama el evento de interrupcion
def interrupcion(pulsador):
	global flag
	global mensaje
	global lcd
	global t1
	if (flag == 0):
		flag = 1
		print ('Empieza a contar el timepo de juego') 
		lcd.clear()
		mensaje = 'Empieza a contar el tiempo'
	elif flag == 1:
		flag = 2
		t1 = tiempo
		print ('Tiempo:' + str(t1))
		lcd.clear()
		mensaje = 'Termina de contar'
	else:
		print('Tu tiempo es:' + str(t1))
		lcd.clear()
		mensaje = 'Ya tienes tu tiempo'



try:
	GPIO.add_event_detect(pulsador, GPIO.RISING, callback=interrupcion, bouncetime=200)
	while True:
		lcd.cursor_pos = (0, 0)
		lcd.write_string(mensaje)
		if flag == 1:
			tiempo = tiempo + 1
			time.sleep(1)
			print("Entro al if tiempo:" + str(tiempo))
finally:
	GPIO.cleanup()
	#lcd.clear()
