from GUI.Data_Entry import Data_Entry
from socket import AF_INET, socket, SOCK_STREAM

class Reseive():
	def __init__(self, client_cocket):
		super(Reseive, self).__init__()
		self.client_socket = client_cocket
		# self.Data_Entry = Data_Entry
	def run(self):
		while True:
			try:
				msg = self.client_socket.recv(1024)
				
				Data_Entry(msg)
				print(msg)
				# testmsg = "work"
				# self.Data_Entry(testmsg)
			except OSError:  # Possibly client has left the chat.
				break

