from abc import abstractmethod,ABC
from BL.in_controller import In_Controller
class Reseive_Interface(ABC):
	def __init__(self,client_socket = None):
		super(Reseive_Interface, self).__init__()
		self.client_socket = client_socket
		self.data = None
	@abstractmethod
	def run(self):pass

	def choise_subclass():
		return Reseive()








# from .interfaces import Reseive_Data
# from BL.in_controller import In_Controller as BL_in_controller

class Reseive(Reseive_Interface):
	def run(self):
		while True:
			try:
				for i in range(101):
					if i == 100:
						self.data = self.client_socket.recv(1024)
				# BL_in.data = self.client_socket.recv(1024)
				# self.GUI.msg = msg
			except OSError:
				break

