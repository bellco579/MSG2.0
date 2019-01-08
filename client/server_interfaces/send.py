# from .interfaces import Send_Data
# from abc import abstractmethod,ABC
#
from .connect import Connect
class Send(object):
	def __init__(self):
		self.client_coket = Connect().client_socket
	def send_to_server(self,data):
		data = str.encode(data)
		self.client_coket.send(data)



# class Send_Interface(ABC):
# 	def __init__(self,client_socket = None):
# 		super(Send_Interface, self).__init__()
# 		self.client_socket = client_socket
# 		self.data = None
# 	def choice_subclass():
# 		return Send(1)
#
#
#
# class Send(Send_Data):
# 	def run(self,data):
# 		self.data = data
# 		if self.data:
# 			self.client_socket.send(bytes(self.data, "utf8"))
