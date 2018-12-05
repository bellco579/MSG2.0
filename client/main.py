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
		print("connect to ", host)

		GUI = Tkinter(client_socket)
		gui_thread = Thread(target=GUI.run)
		gui_thread.start()

		RS = Reseive(GUI, client_socket)
		receive_thread = Thread(target=RS.run)
		receive_thread.start()

Main().run()