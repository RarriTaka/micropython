CODE LED
import pyb

led_bleue=pyb.LED(4)
switch=pyb.Switch()

def on_off():
    led_bleue.toggle()

while True:
    switch.callback(on_off)

///////////////////////////////////////////////////////////////////////////
CODE DOUBLE LED
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
CODE DIMMAGE LED
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
///////////////////////////////////////////////////////////////////////////
CODE POTENTIOMETRE
from pyb import Pin, ADC
import time

pot=pyb.ADC( 'Y12' )

while True:
    val_pot=pot.read()
    print(val_pot)
    time.sleep(0.2)
///////////////////////////////////////////////////////////////////////////
CODE POT LED PWM
from pyb import Pin, ADC, Timer
import time

pot=pyb.ADC( 'Y12' )
timmer = pyb.Timer(4, freq=500)
channel = timmer.channel(2, Timer.PWM, pin=Pin('X10'), pulse_width_percent=100)

while True:
    val_pot=pot.read()
    val_pot=(val_pot/4096)*100
    print(val_pot)
    channel.pulse_width_percent(val_pot)
    time.sleep(0.2)
///////////////////////////////////////////////////////////////////////////
CODE PIEZO V1
from pyb import Pin, ADC, Timer
import time

timmer = pyb.Timer(5, freq=440)
channel = timmer.channel(3, Timer.PWM, pin=Pin('X1'), pulse_width_percent=30)
timmer.freq(261.63)
time.sleep(0.5)
timmer.freq(293.66)
time.sleep(0.5)
timmer.freq(329.63)
time.sleep(0.5)
timmer.freq(261.63)
time.sleep(0.5)
timmer.freq(261.63)
time.sleep(0.5)
timmer.freq(293.66)
time.sleep(0.5)
timmer.freq(329.63)
time.sleep(0.5)
timmer.freq(349.23)
time.sleep(0.5)
timmer.freq(392.00)
time.sleep(0.5)
timmer.freq(329.63)
time.sleep(0.5)
timmer.freq(349.23)
time.sleep(0.5)
timmer.freq(392.00)
time.sleep(0.5)
timmer.freq(392.00)
time.sleep(0.5)
timmer.freq(440)
time.sleep(0.5)
timmer.freq(392.00)
time.sleep(0.5)
timmer.freq(392.00)
time.sleep(0.5)
timmer.freq(440)
time.sleep(0.5)
timmer.freq(392.00)
time.sleep(0.5)
timmer.freq(493.88)
time.sleep(0.5)
timmer.freq(392)
time.sleep(0.5)
timmer.freq(493.88)
time.sleep(0.5)
timmer.freq(493.88)
time.sleep(0.5)
timmer.freq(392)
time.sleep(0.5)
timmer.freq(493.88)
time.sleep(0.5)
///////////////////////////////////////////////////////////////////////////
CODER PIEZO V2
from pyb import Pin, ADC, Timer
import time

def pause():
    channel.pulse_width_percent(0)
    time.sleep(0.1)
    channel.pulse_width_percent(100)

def note(freq, duree):
    dict_temps={"croche":0.25,"noire":0.5,"blanche":1}
    dict_freq={"Do":262,"Re":294,"Mi":330,"Fa":349,"Sol"392,"La":440,"Si":494}
    duree=dict_temps[temps]
    timmer.freq(freq)
    time.sleep(duree)
    pause()
    
joue("La","noire")
joue("La","noire")
joue("Re","noire")
///////////////////////////////////////////////////////////////////////////
CODE TM1637 NOMBRE
import tm1637
import time
display = tm1637.TM1637(clk=pyb.Pin('X7'), dio=pyb.Pin('X6'))

for i in range(501):
    display.number(i)
    time.sleep(0.01)
    
time.sleep(2)

for i in range(501):
    display.number(501-i)
    time.sleep(0.01)0
/////////////////////////////////////////////////////////////////////////
