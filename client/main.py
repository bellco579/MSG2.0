from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from BackEnd.reseive import Reseive
from GUI.TK import Tkinter
# from resieve import resive
import sys
# from send import send
# tkinter.mainloop()

class Main():



	def run(self):
		host = "192.168.1.64"
		port = 5555
		ADDR = (host, port)

		client_socket = socket(AF_INET, SOCK_STREAM)
		client_socket.connect((host, port))
		client_socket.send(b'send')
		RS = Reseive(client_socket)
		receive_thread = Thread(target=RS.run)
		receive_thread.start()
		print("connect to ", host)
		Tkinter(client_socket).run()

Main().run()