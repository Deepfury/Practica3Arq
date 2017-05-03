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
t1 = 400
t2 = 0
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
mensaje = 'Pulsa para empezar'

#funcion que llama el evento de interrupcion
def interrupcion(pulsador):
	global flag
	global mensaje
	global lcd
	if (flag == 0):
		flag = 1
		print ('Empieza a contar el timepo de juego') 
		lcd.clear()
		mensaje = 'Empieza'
	elif flag == 1:
		global t2
		flag = 2
		t2 = tiempo
		print(t1)
		print ('Tiempo:' + str(t2))
		lcd.clear()
		mensaje = 'Fin'
	else:
		print('Tu tiempo es:' + str(t2))
		lcd.clear()
		mensaje = 'Termino el juego'

try:
	GPIO.add_event_detect(pulsador, GPIO.RISING, callback=interrupcion, bouncetime=200)
	while True:
		if flag == 1:
			tiempo += 1
			time.sleep(0.001)
			if(tiempo>1000):
				mensaje = 'Tiempo excedido'

		if(t2 != 0 ):
			#print('t1: ' + str(t1) + ' t2: ' + str(t2))
			tiempo_juego = 100 - abs(t2-t1)/100.0
			#print('Tiempo_juego:' + str(tiempo_juego))
			if (tiempo_juego>0.95):
				#GPIO.output(9, 1) 
				mensaje = 'Felicidades'
				#break
			else:
				mensaje = 'No acertaste'
				#break
		lcd.cursor_pos = (0, 0)
		lcd.write_string(mensaje)
finally:
	lcd.clear()
