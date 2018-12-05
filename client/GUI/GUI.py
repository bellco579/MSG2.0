from abc import abstractmethod,ABC


class GUI(ABC):
	def __init__(self, client_socket):
		super(GUI, self).__init__()
		self.client_socket = client_socket

	@abstractmethod
	def send():
		pass
	@abstractmethod
	def get():
		pass
	@abstractmethod
	def run():
		pass	

