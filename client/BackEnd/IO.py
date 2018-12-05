from abc import abstractmethod,ABC




class Reseive_Data(ABC):
	def __init__(self,  GUI, client_socket):
		super(Reseive_Data, self).__init__()
		self.GUI = GUI
		self.client_socket = client_socket
	
	@abstractmethod
	def run():
		pass


