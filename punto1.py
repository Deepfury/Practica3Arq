# #Import de las liberrias del BCM
# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BCM)

# #importlo la libreria del LCD como charLCD
# from RPLCD import CharLCD

# #Escritura en conexion de 8bits
# #la funcion de escritura funciona así: pins_data=[D0, D1, D2, D3, D4, D5, D6, D7]	
# lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23]) 
# lcd.write_string(u'Hello world!')

# #Escritura en conexión de 4bits
# lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
# lcd.write_string(u'Hello world!')


# #posición donde se va a mostrar
# lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
# #lcd.cursor_pos = (ROW, COLUMN)
# lcd.cursor_pos = (1, 3) 
# lcd.write_string(u'Hello world!')

# #Para limpiar la pantalla del lcd
# lcd.clear()

# #Clásico
# time.sleep()

# #para que sea intermitente un bloque 
# lcd.cursor_mode = CursorMode.blink

# #Cursor en modo de "linea"
# lcd.cursor_mode = CursorMode.line

# #desaparecer el cursor
# lcd.cursor_mode = CursorMode.hide

# #salto de linea
# #\n\r
# lcd.write_string(u'Hello\n\rworld!')


#_________________________________________________________________________________
#Para imprimir la hora y la fecha

import time
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])


while True:
    lcd.write_string("Time: %s" %time.strftime("%H:%M:%S"))
    
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Date: %s" %time.strftime("%m/%d/%Y"))
