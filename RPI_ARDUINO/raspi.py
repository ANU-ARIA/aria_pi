import serial 
from time import *
from multiprocessing import Queue, Process
from import_detect import *

BAUDRATE = 9600
    
def serial_open():
    ser = serial.Serial('/dev/ttyAMA0', baudrate = BAUDRATE)
    
    return ser

def command_arduino(ser, i):
    command = ["go\n", "stop\n", "rgrab\n", "fgrab\n"]
    
    command[i] = command[i].encode('utf-8')
    ser.write(command[i])

def receive_arduino(ser, q):
    if ser.readable():
        data = ser.readline()
        data = str(data[:-1].decode())
        q.put(data)
        
#def image_process(cap, ser, q, state_flag = 1):
    
    
def main_process(ser, q):

    cap = open_cam()
    command_arduino(ser, 0)
    state_flag = 1
    sleep(1)
    
    while True:
        goods_x, signal, barcode = cam(cap)
        
        if signal == 'P' and (goods_x >= 10 and goods_x <= 300):
            if state_flag == 1:
                command_arduino(ser, 1)
                state_flag = 2
            if len(barcode) > 5 and state_flag == 2:
                sleep(0.01)
                command_arduino(ser, 2)
                state_flag = 0
                
        elif signal == 'F' and (goods_x >= 10 and goods_x <= 300):
            if state_flag == 1:
                command_arduino(ser, 1)
                state_flag = 2
            if len(barcode) > 5 and state_flag == 2:
                sleep(0.01)
                command_arduino(ser, 3)
                
        else:
            if q.empty() == False and signal == 'N':
                rx_data = q.get()
                print(rx_data)
                if rx_data == "complete":
                    command_arduino(ser, 0)
                    state_flag = 1
                    
        if cv.waitKey(1) & 0xFF == 27:
            break 
            
    cap.release()
    cv.destroyAllWindows()  

def serve_process(ser, q):
    while True:
        receive_arduino(ser, q)
        
        
try:
    if __name__ == "__main__":
        print("start \n")
        q = Queue()
        ser = serial_open()
        p1 = Process(target = main_process, args = (ser,q))
        p2 = Process(target = serve_process, args = (ser,q))
        p1.start()
        p2.start()

except KeyboardInterrupt:
    print("exit() \n")
    p1.join()
    p2.join()