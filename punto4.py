#importlo la libreria del LCD como charLCD
from RPLCD import CharLCD

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

#abrir el archivo de texto
with open("archivo.txt") as archivo:
	datos = archivo.read()
	mensaje = 'Datos almacenados'
	


contador_hot = datos.lower().count("hot")
mensaje = 'Numero de HOT:' + str(contador_hot)
# for i in datos:
# 	palabras = i.split()
# 	if(palabras == 'hot'):
# 		contador_hot =+ 1


#punto 5

lcd.cursor_pos = (0, 0)
lcd.write_string(mensaje)
#print("El numero de 'hot' es:" + str(contador_hot))
