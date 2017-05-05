# #Import de las liberrias del BCM
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
#importlo la libreria del LCD como charLCD
from RPLCD import CharLCD

#configuracion de entrada del pulsador y de las entradas del sw  
pulsador = 7
GPIO.setup(15,GPIO.OUT)
GPIO.setup(13,GPIO.IN)
GPIO.setup(11,GPIO.IN)
GPIO.setup(pulsador,GPIO.IN)
entrada_1 = 0
entrada_2 = 0

#definicion de variables
tiempo = 0
flag_2 = 0
flag_3 = 0
t1 = 0
t2 = 0
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
mensaje = 'Pulsa para empezar'
datos = ''

#Evento de interrupcion
def interrupcion(pulsador):
	global entrada_1
	global entrada_2
	global mensaje
	global t1
	global t2
	global flag_2
	global flag_3
	global tiempo
	print('entro al evento e1: '+str(entrada_1)+' e2: '+str(entrada_2))
	if entrada_1 == 0 and entrada_2 == 0:
		#evento punto 2
		if (flag_2 == 0):
			flag_2 = 1
			print ('Empieza a contar el timepo de juego') 
			mensaje = 'Empieza a contar el tiempo'
		elif flag_2 == 1:
			flag_2 = 2
			t1 = tiempo
			print ('Tiempo:' + str(t1))
			mensaje = 'Termina de contar'
			tiempo = 0
		else:
			print('Tu tiempo es:' + str(t1))
			mensaje = 'Ya tienes tu tiempo'
	elif entrada_1 == 1 and entrada_2 == 0:
		#evento punto 3
		if (flag_3 == 0):
			flag_3 = 1
			print ('Empieza a contar el timepo de juego') 
			mensaje = 'Empieza'
		elif flag_3 == 1:
			flag_3 = 2
			t2 = tiempo
			print(t1)
			print ('Tiempo:' + str(t2))
			mensaje = 'Fin'
		else:
			print('Tu tiempo es:' + str(t2))
			mensaje = 'Termino el juego'

try:
	GPIO.add_event_detect(pulsador, GPIO.RISING, callback=interrupcion, bouncetime=200)
	while True:
		entrada_1 = GPIO.input(11)
		entrada_2 = GPIO.input(13)
		#print('entro al evento e1: '+str(entrada_1)+' e2: '+str(entrada_2))
		if entrada_1 == 0 and entrada_2 == 0:
			#punto 2
			lcd.cursor_pos = (0, 0)
			lcd.write_string(mensaje)
			if flag_2 == 1:
				tiempo += 1
				time.sleep(0.001)
				print("Entro al if tiempo:" + str(tiempo))
		elif entrada_1 == 1 and entrada_2 == 0:
			#punto 3
			if flag_3 == 1:
				tiempo += 1
				time.sleep(0.001)
				if(tiempo>1000):
					mensaje = 'Tiempo excedido'

			if(t2 != 0 ):
				#print('t1: ' + str(t1) + ' t2: ' + str(t2))
				tiempo_juego = 100 - abs(t2-t1)/100.0
				#print('Tiempo_juego:' + str(tiempo_juego))
				if (tiempo_juego>0.95):
					GPIO.output(15, 1) 
					mensaje = 'Felicidades'
					#break
				else:
					mensaje = 'No acertaste'
					#break
			lcd.cursor_pos = (0, 0)
			lcd.write_string(mensaje)
		elif entrada_1 == 0 and entrada_2 == 1:
			#punto 4
			#abrir el archivo de texto
			with open("archivo.txt") as archivo:
				datos = archivo.read()
				mensaje = 'Datos almacenados'
			lcd.cursor_pos = (0, 0)
			lcd.write_string(mensaje)
		else:
			#punto 5
			contador_hot = datos.lower().count("hot")
			mensaje = 'Numero de HOT:' + str(contador_hot)
			lcd.cursor_pos = (0, 0)
			lcd.write_string(mensaje)
finally:
	lcd.clear()
