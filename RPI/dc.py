import RPi.GPIO as IO
import time as t

IN1 = 19
IN2 = 26

def DC_setup():
    IO.setmode(IO.BCM)
    IO.setup(IN1, IO.OUT)
    IO.setup(IN2, IO.OUT)
    d1 = IO.PWM(IN1, 50)
    d2 = IO.PWM(IN2, 50)
    d1.start(0)       
    d2.start(0)
    
    return d1, d2
   
d1, d2 = DC_setup()

while True:
    d1.ChangeDutyCycle(9)
    d2.ChangeDutyCycle(0)
    
