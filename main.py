import pyb

led_bleue=pyb.LED(4)
switch=pyb.Switch()

def on_off():
    led_bleue.toggle()

while True:
    switch.callback(on_off)

///////////////////////////////////////////////////////////////////////////
from pyb import Timer, Pin, ADC
import time

my_pin = pyb.Pin( 'X1', pyb.Pin.OUT_PP)
my_pin2 = pyb.Pin( 'X6', pyb.Pin.OUT_PP)

while True:
    my_pin.high()
    time.sleep(1)
    my_pin.low()
    time.sleep(1)
