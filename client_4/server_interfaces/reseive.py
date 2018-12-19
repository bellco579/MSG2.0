from abc import abstractmethod,ABC
from .connect import Connect

import asyncio
from threading import Thread



class Reseive(object):
	def __init__(self):
		self.client_coket = Connect().client_socket
		self.cache = None
	def data_reseive(self):
		data = self.client_coket.recv(1024).decode()
		return data



class Reseive_Interface(ABC):
	def __init__(self):
		super(Reseive_Interface, self).__init__()
		self.client_socket = None
	async def data_reseive(self):
		self.data = self.client_socket.recv(1024)




	# @abstractmethod
	# def run(self):pass
	# @abstractmethod
	# def reseive_data_from_server(self):pass
	# def choise_subclass():
	# 	return Reseive()

# class Reseive(Reseive_Interface):
# 	def __init__(self):
# 		self.in_controller = In_Controller_interface.choise_in_controller()
# 		self.send_to_in_controller = self.in_controller
#
# 	def reseive_data_from_server(self):
# 		while True:
# 			try:
# 				self.data = self.client_socket.recv(1024)
# 				self.send_to_in_controller.run(self.data)
# 			except Exception:
# 				pass
#
# 	def run(self):
# 		self.reseive_data_from_server()
