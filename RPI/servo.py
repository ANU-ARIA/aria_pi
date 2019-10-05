import RPi.GPIO as GPIO  
from time import sleep

GPIO.setmode(GPIO.BCM) 

#GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
 
p1 = GPIO.PWM(12, 50)   
#p2 = GPIO.PWM(21, 50)   

p1.start(0)            
#p2.start(0)            

val = 12

while(1):
    p1.ChangeDutyCycle(3)
    sleep(2)
    p1.ChangeDutyCycle(7.5)
    sleep(2)
    p1.ChangeDutyCycle(12)
    sleep(2)

p1.stop()                
#p2.stop()

GPIO.cleanup() 






