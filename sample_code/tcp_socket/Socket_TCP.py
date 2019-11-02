import threading
import socket
import enum
from time import sleep


#====================================================================================
# CLASS : Socket_TCP
#====================================================================================
class Socket_TCP():
	MAX_BUFF_SIZE = 99999
	m_data = ""

	#====================================================================================
	# 생성자
	#====================================================================================
	def __init__(self, _ip, _port, _recv_callback=None):
		self.ip = _ip
		self.port = _port
		self.recv_callback = None

		if _recv_callback:
			self.recv_callback = _recv_callback

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.start(self.ip, self.port)

		self.thread_recv = threading.Thread(target = self.recv_threadproc, args = (self,))
		self.thread_recv.start()

	def start(self, _ip, _port):
		try:
			self.sock.connect((_ip, _port))
			print("connect success")
		except Exception as ex:
			print("socket start error : ", ex)


	#====================================================================================
	# receive thread procedure
	#====================================================================================
	def recv_threadproc(self, _args):
		while True:
			sleep(0.01)
			try:
				# 수신된 메세지 처리
				rbuff = self.sock.recv(1024)
				received =  str(rbuff, encoding='utf-8')
				print('received : {0}'.format(received))
				self.recv_callback( received )
 
			except Exception as ex:
				print("recv_proc except : ", ex)
				self.m_data = ""
				pass


	#====================================================================================
	# send function
	#====================================================================================
	def send(self, _msg):
		try:
			self.sock.send(bytes(_msg, encoding='utf-8'))
			print("send data : ", _msg)
		except Exception as ex:
			print("send except : ", ex)
			pass

	