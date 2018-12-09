from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

from .reseive import Reseive
from .send import Send

# GUI

class Main():
	def run(self):
		host = "192.168.1.64"
		port = 5555
		ADDR = (host, port)


		client_socket = socket(AF_INET, SOCK_STREAM)
		client_socket.connect((host, port))
		print("connect to ", host)

		# app_list = [GUI,]
		# OUT_ctr = OUT_Controller(app_list)
		# OUT_ctr_thread = Thread(target=OUT_ctr.run)
		# OUT_ctr_thread.start()


		RS = Reseive(client_socket)
		receive_thread = Thread(target=RS.run)
		receive_thread.start()

		send = Send( client_socket)
		send_thread = Thread(target=send.run)
		send_thread.start()


Main().run()