# -*- coding: utf-8 -*-
'''Constantes de configuración de manejo.
Multivac-GT
'''

#Definicion de pines y vectores de movimiento para GPIOs
lst_motor_pins = [2, 3, 4, 17, 27, 22, 10, 9]

dic_direcciones = {
    'ADELANTE' : (1,0,1,0,1,0,1,0),
    'DERECHA'  : (0,1,0,1,1,0,1,0),
    'ATRAS'    : (0,1,0,1,0,1,0,1),
    'IZQUIERDA': (1,0,1,0,0,1,0,1),
    'DEFAULT'  : (0,0,0,0,0,0,0,0)
}

pwm_right = 19
pwm_left = 18
freq = 100000