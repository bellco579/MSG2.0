from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

# Beck-end
from BackEnd.reseive import Reseive
from BackEnd.send import Send

# GUI
from GUI.TK import Tkinter as GUIs

class Main():

	def run(self):
		host = "192.168.1.64"
		port = 5555
		ADDR = (host, port)

		client_socket = socket(AF_INET, SOCK_STREAM)
		client_socket.connect((host, port))
		print("connect to ", host)

		GUI = GUIs(client_socket)
		gui_thread = Thread(target=GUI.run)
		gui_thread.start()

		RS = Reseive(GUI, client_socket)
		receive_thread = Thread(target=RS.run)
		receive_thread.start()

		send = Send(GUI, client_socket)
		send_thread = Thread(target=send.run)
		send_thread.start()


Main().run()