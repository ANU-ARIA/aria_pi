from import_detect import *
import RPi.GPIO as IO
import time as t 

PIN1 = 17
PIN2 = 27

def gpio_setup():
    IO.setmode(IO.BCM)
    IO.setup(PIN1, IO.OUT)
    IO.setup(PIN2, IO.OUT)
    
def main():
    cap = open_cam()
    gpio_setup()
    
    while True:
        goods_x, signal = cam(cap)
        
        if goods_x >= 80 and goods_x <= 400:
            if signal == 'P':
                IO.output(PIN1, 1)
                IO.output(PIN2, 0)
                
            elif signal == 'F':
                IO.output(PIN1, 0)
                IO.output(PIN2, 1)
        else:
            if signal == 'N':
                IO.output(PIN1, 1)
                IO.output(PIN2, 1)
        
        if cv.waitKey(1) & 0xFF == 27:
            break 
            
    cap.release()
    cv.destroyAllWindows()     
    
try:
    if  __name__ == '__main__':
        main()

except KeyboardInterrupt:
    print("exit \n\n")
    