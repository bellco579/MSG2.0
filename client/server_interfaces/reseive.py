from abc import abstractmethod,ABC
# from hammock import Hammock
import slumber
from .connect import Connect

import asyncio
from threading import Thread

from BL.IN_controller import IN_controller

class Reseive(object):
	def __init__(self):
		self.client_coket = Connect().client_socket
		self.cache = None
	async def data_reseive(self):
		api = slumber.API('http://localhost:8000/api/v1/',auth = ("bellco2", "antoha888"))
		# print(api.)
		# api = Hammock('localhost:8000/api/v1/')
		# print(api.profile)
		# print(api)
		test = api.profile.get()
		api.profile.send(test["id"] = 234)
		print(type(test))
		# api.profile.set(id =1 ,location = "efef")
		# print(api.profile.send('dfdf'))
		data = self.client_coket.recv(1024).decode()
		print(data)
		IN_controller(data)



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
