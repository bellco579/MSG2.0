from abc import abstractmethod,ABC




class Reseive_Data(ABC):
	def __init__(self, client_socket):
		super(Reseive_Data, self).__init__()
		self.client_socket = client_socket
	
	@abstractmethod
	def run():
		pass

class Send_Data(ABC):
	def __init__(self, client_socket):
		super(Send_Data, self).__init__()
		self.client_socket = client_socket
	
	@abstractmethod
	def run():
		pass

