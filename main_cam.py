from import_detect import *
import RPi.GPIO as IO
import time as t 
from communication import * 

PIN1 = 17
PIN2 = 27

reconnect_step = 1

def MES_COM_SETUP():
    print(" setup complete!! ")
    mes = connection_MES(1)

    return mes 

def gpio_setup():
    IO.setmode(IO.BCM)
    IO.setup(PIN1, IO.OUT)
    IO.setup(PIN2, IO.OUT)
    
def image_process(cap):
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
def OnReceived_s2f41(item):

def OnReceived_s6f12(item):
    
def MES_COM_PROCESS(MES_COM):
    if MES_COM.isConnected() == True:
        if MES_COM.getReceived_data_count > 0:
            SECS_ITEM item = MES_COM.pop_item()
            if item.nS == 2:
                if item.nF == 41:
                    OnReceived_s2f41(item)
            elif item.nS == 6:
                if item.nF == 12:
                    OnReceived_s6f12(item)
    else:
        if reconnect_step == 1:
            MES_COM.disConnect()
            disconn_time = t.time()
            reconnect_step = 2

        elif reconnect_step == 2:
            spend_time = t.time() - disconn_time
            if spend_time > 5:
                MES_COM.connect()
                reconn_time = t.time()
                reconnect_step = 3
            else:
        elif reconnect_step == 3:
            spend_time = t.timne() - reconn_time
            if spend_time > 3:
                if MES_COM.isConnected() == False:
                    reconnect_step = 1

def main():
    cap = open_cam()
    gpio_setup()
    MES_COM = MES_COM_SETUP()
    
    while True:
        image_process(cap)

        MES_COM_PROCESS(MES_COM)

        if cv.waitKey(1) & 0xFF == 27:
            break 
            
    cap.release()
    cv.destroyAllWindows()     
    
try:
    if  __name__ == '__main__':

        main()

except KeyboardInterrupt:
    print("exit \n\n")
    