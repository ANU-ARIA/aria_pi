import threading
from time import sleep
import tokenize
from Socket_TCP import *


#====================================================================================
# 상수
#====================================================================================
MIN_SLEEP_TIME = float( 0.05 )


#====================================================================================
# receive function
#====================================================================================
def on_recv( _data ):
	print( "received : " , _data )

#====================================================================================
# 전역 변수
#====================================================================================
tcp_socket = Socket_TCP( "127.0.0.1", 7000, on_recv )


#====================================================================================
# main function
#====================================================================================
def main():
    while True:
        sleep( MIN_SLEEP_TIME )
        #------------------------------
        # write application code here (start)
        #------------------------------
        sleep( 5 )
        data = "Hello my application"
        tcp_socket.send( data )
        #------------------------------
        # write application code here (end)
        #------------------------------
    
#====================================================================================
# 
#====================================================================================
try:
    if  __name__ == '__main__':
        main()

except KeyboardInterrupt:
    print("exit \n\n")
    
