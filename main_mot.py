#from import_detect import *
from motor import *
#from multiprocessing import Process, Queue
import RPi.GPIO as IO
import time as t

PIN1 = 17
PIN2 = 27

def gpio_setup():
    IO.setmode(IO.BCM)
    IO.setup(PIN1, IO.IN)
    IO.setup(PIN2, IO.IN)
    
def main():
    gpio_setup()
    d1, d2 = DC_setup()
    s1, s2 = SERVO_setup()
    
    while True:
        if IO.input(PIN1) == 1 and IO.input(PIN2) == 0: 
            DC_STOP(d1, d2)
            t.sleep(1.5)
            Grab_Regular_Object(s1, s2)
            
        elif IO.input(PIN1) == 0 and IO.input(PIN2) == 1:
            DC_STOP(d1, d2)
            t.sleep(1.5)
            Grab_Inferior_Object(s1, s2)
            
        elif IO.input(PIN1) == 1 and IO.input(PIN2) == 1:
            DC_PWM(d1, d2)
            
try:
    if __name__ == '__main__':
        main()
        
except KeyboardInterrupt:
    print("exit() \n\n")