from .interfaces import Send_Data
from abc import abstractmethod,ABC

class Send_Interface(ABC):
	def __init__(self,client_socket = None):
		super(Send_Interface, self).__init__()
		self.client_socket = client_socket
		self.data = None
	def choice_subclass():
		return Send(1)



class Send(Send_Data):
	def run(self,data):
		self.data = data
		if self.data:
			self.client_socket.send(bytes(self.data, "utf8"))
