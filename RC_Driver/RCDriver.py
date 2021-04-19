# -*- coding: utf-8 -*-
'''
Descripcion:
'''
try:
    import RPi.GPIO as gpio
except RuntimeError:
    print("Error al importar RPi.GPIO, puede que necesite permisos de super usuario.")

from config import lst_motor_pins, dic_direcciones, pwm_left, pwm_right, freq

class RCDriver():
    def __init__(self):
        self.motors_pins = lst_motor_pins
        self.pwm_left_pin = pwm_left
        self.pwm_right_pin = pwm_right
        self.pwm_left = None
        self.pwm_right = None
        self.freq = freq
        self.vel_values = [0, 0]
        self.movements = dic_direcciones

    def motors_init(self):
        #Inicialización de GPIOs
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        gpio.setup(self.motors_pins, gpio.OUT)
        gpio.setup((self.pwm_left_pin, self.pwm_right_pin), gpio.OUT)
        #Inicialización de PWMs
        self.pwm_left = gpio.PWM(self.pwm_left_pin, self.freq)
        self.pwm_left.start(0)
        self.pwm_right = gpio.PWM(self.pwm_right_pin, self.freq)
        self.pwm_right.start(0)

    def move(self, direction='DEFAULT', pwms=[0,0]):
        gpio.output(self.motors_pins, self.movements[direction])
        self.pwm_left.ChangeDutyCycle(pwms[0])
        self.pwm_right.ChangeDutyCycle(pwms[1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pwm_left.stop()
        self.pwm_right.stop()
        gpio.cleanup()
    
        