import RPi.GPIO as IO
import time as t

IN1 = 19
IN2 = 26

SERVO_1 = 12
SERVO_2 = 21

SERVO_2_min_ang = 3
SERVO_2_max_ang = 12

def DC_setup():
    IO.setmode(IO.BCM)
    IO.setup(IN1, IO.OUT)
    IO.setup(IN2, IO.OUT)
    d1 = IO.PWM(IN1, 50)
    d2 = IO.PWM(IN2, 50)
    d1.start(0)       
    d2.start(0)
    
    return d1, d2           
 
def SERVO_setup():
    IO.setup(SERVO_1, IO.OUT)
    IO.setup(SERVO_2, IO.OUT)
    s1 = IO.PWM(SERVO_1, 50)
    s2 = IO.PWM(SERVO_2, 50)
    s1.start(0)
    s2. start(0)
    s1.ChangeDutyCycle(7.5)
    s1.ChangeDutyCycle(0)
    SERVO2_PWM1(SERVO_2_min_ang, s2) 
    s2.ChangeDutyCycle(0)
    
    return s1, s2
    
def DC_PWM(d1, d2):
    d1.ChangeDutyCycle(0)
    d2.ChangeDutyCycle(11)

def SERVO1_PWM(servo1_pulse, s1):
    s1.ChangeDutyCycle(servo1_pulse)
    t.sleep(1)
    
def SERVO2_PWM1(servo2_pulse, s2):
    for i in range(1,100):
        s2.ChangeDutyCycle(servo2_pulse)
        servo2_pulse += 0.09
        if servo2_pulse >= SERVO_2_max_ang:
            servo2_pulse = SERVO_2_max_ang
        t.sleep(0.05)

def SERVO2_PWM2(servo2_pulse, s2):
    for i in range(1,100):
        s2.ChangeDutyCycle(servo2_pulse)
        servo2_pulse -= 0.09
        if servo2_pulse <= SERVO_2_min_ang:
            servo2_pulse = SERVO_2_min_ang
        t.sleep(0.05)

def  Grab_Regular_Object(s1, s2):
    SERVO2_PWM2(SERVO_2_max_ang, s2)
    t.sleep(0.1)
    SERVO1_PWM(3, s1)
    t.sleep(0.1)
    SERVO2_PWM1(SERVO_2_min_ang, s2)
    t.sleep(0.1)
    SERVO1_PWM(7.5, s1)
    s1.ChangeDutyCycle(0)
    s2.ChangeDutyCycle(0)

def  Grab_Inferior_Object(s1, s2):
    SERVO2_PWM2(SERVO_2_max_ang, s2)
    t.sleep(0.1)
    SERVO1_PWM(12, s1)
    t.sleep(0.1)
    SERVO2_PWM1(SERVO_2_min_ang, s2)
    t.sleep(0.1)
    SERVO1_PWM(7.5, s1)
    s1.ChangeDutyCycle(0)
    s2.ChangeDutyCycle(0)
    
def DC_STOP(d1, d2):
    d1.ChangeDutyCycle(0)
    d2.ChangeDutyCycle(0)
    
def SERVO1_STOP(s1):
    s1.stop()

def SERVO2_STOP(s2):
    s2.stop()
