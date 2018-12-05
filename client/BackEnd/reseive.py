from .IO import Reseive_Data
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

class Send_MSG():
	def __init__(self, GUI,client_socket):
		super(Send_MSG, self).__init__()
		self.GUI = GUI
		self.client_socket = client_socket 
	def run(self):
		data = None
		while True:
			if (self.GUI.send_msg != None) and (self.GUI.send_msg != data):
				self.client_socket.send(bytes(self.GUI.send_msg, "utf8"))
				data = self.GUI.send_msg

class Reseive(Reseive_Data):

	def run(self):
		SMSG = Send_MSG(self.GUI, self.client_socket)
		Thread(target=SMSG.run).start()
		while True:
			try:
				msg = self.client_socket.recv(1024)
				self.GUI.msg = msg
				print(msg)
				# self.GUI.get(msg)
				# print(msg)
			except OSError:
				break

