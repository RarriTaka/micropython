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
///////////////////////////////////////////////////////////////////////////
from pyb import Timer, Pin, ADC
import time

timer = pyb.Timer(5, freq=500)
channel_bleu = timer.channel(3, Timer.PWM, pin=Pin('X1'), pulse_width_percent=100)
channel_rouge = timer.channel(4, Timer.PWM, pin=Pin('X2'), pulse_width_percent=100)

while True:
    for i in range(101):
        channel_bleu.pulse_width_percent(i)
        channel_rouge.pulse_width_percent(100-i)
        time.sleep(0.1)
    
    for i in range(101):
        channel_bleu.pulse_width_percent(100-i)
        channel_rouge.pulse_width_percent(i)
        time.sleep(0.1)
