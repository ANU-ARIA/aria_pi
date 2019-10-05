import serial
import time

#alpha = 'a'
#alpha = alpha.encode('utf-8')
ser = serial.Serial('/dev/ttyAMA0', 9600)

'''while True:
    #ser.write(alpha)
    #time.sleep(1)
    #print(string)
    print(ser.readline())'''

while ser is not None:
    data = ser.read(ser.in_waiting )
    if data:
        print("received: " + str(data, 'utf-8'))

