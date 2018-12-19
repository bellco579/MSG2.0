from abc import abstractmethod,ABC


class GUI(ABC):
	def __init__(self):
		super(GUI, self).__init__()
		# self.send_to_bl = send_to_bl
		# self.client_socket = client_socket

	@abstractmethod
	def send():
		pass
	@abstractmethod
	def get():
		pass
	@abstractmethod
	def run():
		pass	

