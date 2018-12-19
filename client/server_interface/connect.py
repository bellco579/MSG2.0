from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

from .reseive import Reseive_Interface
from .send import Send_Interface

# GUI

class Main():

	def get_interface_of_implmets_object(self):
		print('connect is working')	

		host = "192.168.1.64"
		port = 5555
		ADDR = (host, port)

		client_socket = socket(AF_INET, SOCK_STREAM)
		client_socket.connect((host, port))
		print("connect to ", host)
		self.reseive = Reseive_Interface.choise_subclass()
		self.send    = Send_Interface.choice_subclass()

		self.reseive.client_socket = client_socket
		self.send.client_socket = client_socket 

		return {"reseive":self.reseive,"send":self.send}
		# return self.reseive, self.send

	# def run(self):

		# app_list = [GUI,]
		# OUT_ctr = OUT_Controller(app_list)
		# OUT_ctr_thread = Thread(target=OUT_ctr.run)
		# OUT_ctr_thread.start()

		# send_thread = Thread(target=self.send.run)
		# send_thread.start()


