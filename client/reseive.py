from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def reseive(client_socket):	
	while True:
		try:
			msg = client_socket.recv(1024).decode("utf8")
			print(msg)
			# msg_list.insert(tkinter.END, msg)
		except OSError:  # Possibly client has left the chat.
			break
