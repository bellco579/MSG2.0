
class Ready_to_Send():
	def __init__(self, client_socket):
		super(Ready_to_Send, self).__init__()
		self.client_socket  = client_socket		
	def send(self,data):
		self.client_socket.send(b'test')
