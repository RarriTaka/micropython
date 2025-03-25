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
CODE TEMPERATURE
from pyb import Pin, ADC
import time
import tm1637

TMP36 = pyb.ADC( 'Y6' )
display = tm1637.TM1637(clk=pyb.Pin('X7'), dio=pyb.Pin('X6'))

while True:
    valeur_lue = TMP36.read()
    temperature=((valeur_lue/4096)*330)-50
    print(temperature)
    display.number(temperature)
    time.sleep(1)
//////////////////////////////////////////////////////////////////////////
CODE EXAMEN BROUILLON
from pyb import Pin, ADC, Timer
import time

pot=pyb.ADC( 'Y12' )
timmer = pyb.Timer(4, freq=500)
channel_rouge = timmer.channel(2, Timer.PWM, pin=Pin('X10'), pulse_width_percent=100)

timmer = pyb.Timer(4, freq=500)
channel_bleu = timmer.channel(2, Timer.PWM, pin=Pin('X10'), pulse_width_percent=100)

timmer = pyb.Timer(4, freq=500)
channel_jaune = timmer.channel(2, Timer.PWM, pin=Pin('X10'), pulse_width_percent=100)

while True:
    val_pot=pot.read()
    val_pot=(val_pot/4096)*100
    print(val_pot)
    channel_rouge.pulse_width_percent(val_pot)
    channel_rouge.pulse_width_percent(val_pot-channel_rouge.pulse_width_percent)
    channel_rouge.pulse_width_percent(val_pot-channel_bleu.pulse_width_percent)
    time.sleep(0.2)
//////////////////////////////////////////////////////////////////////////////
CODE EXAMEN MAISON
from pyb import Pin, ADC, Timer
import time

pot = ADC('Y12')

limite_rouge = 2000 
limite_bleu = 1500 
limite_jaune = 1000 

timer_rouge = Timer(4, freq=500)
channel_rouge = timer_rouge.channel(1, Timer.PWM, pin=Pin('X10'), pulse_width_percent=0)

timer_bleu = Timer(4, freq=500)
channel_bleu = timer_bleu.channel(2, Timer.PWM, pin=Pin('X11'), pulse_width_percent=0)

timer_jaune = Timer(4, freq=500)
channel_jaune = timer_jaune.channel(3, Timer.PWM, pin=Pin('X12'), pulse_width_percent=0)

duree = 0.1

while True:
    val_pot = pot.read()
    
    if val_pot > limite_rouge:
        channel_rouge.pulse_width_percent(100)
    else:
        channel_rouge.pulse_width_percent(0)
    
    if val_pot > limite_bleu:
        channel_bleu.pulse_width_percent(100)
    else:
        channel_bleu.pulse_width_percent(0)
    
    if val_pot > limite_jaune:
        channel_jaune.pulse_width_percent(100)
    else:
        channel_jaune.pulse_width_percent(0)
////////////////////////////////////////////////////////////////////////////
CODE EXAMEN FINAL
from pyb import Pin, ADC, Timer
import time

pot = pyb.ADC('Y12')

timmer_rouge = pyb.Timer(4, freq=500)
channel_rouge = timmer_rouge.channel(2, Timer.PWM, pin=Pin('X10'), pulse_width_percent=100)

timmer_bleu = pyb.Timer(3, freq=500)
channel_bleu = timmer_bleu.channel(2, Timer.PWM, pin=Pin('X8'), pulse_width_percent=100)

timmer_jaune = pyb.Timer(5, freq=500)
channel_jaune = timmer_jaune.channel(2, Timer.PWM, pin=Pin('X4'), pulse_width_percent=100)

while True:
    val_pot=pot.read()
    val_pot=(val_pot/4096)*100
    print(val_pot)
    time.sleep(0.2)
    if val_pot<50:
       channel_rouge.pulse_width_percent(0)
       channel_bleu.pulse_width_percent(0)
       channel_jaune.pulse_width_percent(0)
    else:
       channel_rouge.pulse_width_percent(val_pot)
       channel_bleu.pulse_width_percent(val_pot)
       channel_jaune.pulse_width_percent(val_pot)
////////////////////////////////////////////////////////////////////////////
TEST CODE CAPTEUR PHOTORESISTANCE
from pyb import Pin, ADC, Timer
import time
import tm1637

ldr = pyb.ADC('X19')
display = tm1637.TM1637(clk=pyb.Pin('X10'), dio=pyb.Pin('X11'))
my_pin = pyb.Pin( 'X1', pyb.Pin.OUT_PP)

while True:
    lumiere = ldr.read()
    lumiere=(lumiere/4096)*100
    lumiere=int(lumiere)
    time.sleep(0.5)
    print(lumiere)
    display.number(lumiere)
    
    if lumiere > 60:
     my_pin.off()
    else:
        my_pin.on()
//////////////////////////////////////////////////////////////////////////////
BROUILLON LED PHOTORESISTANCE
from pyb import Pin, ADC, Timer
import time

ldr = pyb.ADC('X8')
pot = pyb.ADC('X19')
led = pyb.Pin( 'X1', pyb.Pin.OUT_PP)

while True:
    lumiere = ldr.read()
    lumiere=(lumiere/4096)*100
    lumiere=int(lumiere)
    val_pot = pot.read()
    val_pot=(val_pot/4096)*100
    val_pot=int(val_pot)
    
    if lumiere<50:
        led.on()
    else:
        led.off()
    
    print("Lum : ",lumiere)
    print("Pot : ",val_pot)
    time.sleep(0.5)
////////////////////////////////////////////////////////////////////////////////
from pyb import Pin, ADC, Timer
from time import sleep
from ultrasonic import Ultrasonic

timmer = pyb.Timer(2 , freq=440)
channel = timmer.channel(1, Timer.PWM, pin=Pin('X6'), pulse_width_percent=10)

TRIGGER_PIN = pyb.Pin.board.X1

ECHO_PIN = pyb.Pin.board.X2

sr04 = Ultrasonic( TRIGGER_PIN, ECHO_PIN )



def beep():
    channel.pulse_width_percent(60)
    sleep(0.5)
    channel.pulse_width_percent(0)
    sleep(1)
    
while True:
    try:
        distance=sr04.distance_in_cm()
    except:
        pass
    print(distance)
    if distance<50:
        beep()
    sleep(0.1)
///////////////////////////////////////////////////////////////////////////
CODE CAPTEUR DE DISTANCE
from time import sleep, ticks_ms, ticks_diff
from Ultrasonic import Ultrasonic
from pyb import Timer, Pin

#broche poue déclencher le senseur
TRIGGER_PIN = pyb.Pin.board.X1
#broche pour attendre le retour d'écho
ECHO_PIN = pyb.Pin.board.X2
#creation de l'objet sr04
sr04 = Ultrasonic(TRIGGER_PIN, ECHO_PIN)

#creation du piezo
timmer = pyb.Timer(1, freq=440)
channel = timmer.channel(1, Timer.PWM, pin=Pin('X8'), pulse_width_percent=0)

def beep():
    channel.pulse_width_percent(100)
    sleep(0.5)
    channel.pulse_width_percent(0)

def pause():
    start=ticks_ms() #on mesure à quel moment la fonction pause se met en route
    while True:
        try:
            distance=sr04.distance_in_cm()
        except:
            distance=10000
        duree_pause=distance/100
        temps_final=ticks_ms()
        delta_temps=ticks_diff(temps_final,start)
        if delta_temps>duree_pause*1000:
            break
    

while True:
    try:
        distance=sr04.distance_in_cm()
        print("Distance : ",distance)
    except:
        pass
    beep()
    pause()
///////////////////////////////////////////////////////////////////////////////
CODE PHOTORESISTANCE TEMPERATURE
from pyb import Pin, ADC, Timer
import pyb
import time
import tm1637

ldr = pyb.ADC('X19')
TMP36 = pyb.ADC( 'X2' )
display = tm1637.TM1637(clk=pyb.Pin('X7'), dio=pyb.Pin('X6'))
my_pin = pyb.Pin( 'X1', pyb.Pin.OUT_PP)
btn = pyb.Pin( 'Y9', pyb.Pin.IN, pull=pyb.Pin.PULL_UP )
device = 0
#Quand "device = 0" on affiche la lumière et quand "device = 1" on affiche la température

while True:
    lumiere = ldr.read()
    lumiere=(lumiere/4096)*100
    lumiere=int(lumiere)
    time.sleep(0.5)
    print(lumiere)
    display.number(lumiere)
    valeur_lue = TMP36.read()
    temp=((valeur_lue/4096)*330)-50
    temp=int(temp)
    print(temp)
    display.number(temp)
    time.sleep(0.5)
    if lumiere > 60:
     my_pin.off()
    else:
        my_pin.on()
    if btn.value() == 0:
       pyb.delay(500)
       if device == 0:
           device = 1
       else:
           display.number(temp)
           device = 0
//////////////////////////////////////////////////////////////////////////////////////////
CODE SERVO
#on branche le servo sur X1
servo1 = pyb.Servo(1)
servo2 = pyb.Servo(2)                               

servo1.angle(0)#l'angle peut varier entre -90 et +90
servo2.angle(0)

vertical = pyb.ADC('A0') 
horizontal= pyb.ADC('A1')
while True :
    x=vertical.read()
    y=horizontal.read()
    print("X : ",x," ; ","Y : ",y)
    
    angle1=((x/4095)*180)-90
    servo1.angle(angle1)
    
    angle2=((y/4095)*180)-90
    servo2.angle(angle2)
    pyb.delay(100)
/////////////////////////////////////////////////////////////////////////////////////////
