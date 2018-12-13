from abc import abstractmethod,ABC
from threading import Thread
import json
class In_Controller_interface(ABC):
	def __init__(self):
		super(In_Controller_interface, self).__init__()
		self.reseive = None
		self.data = None
		self.BL = None

	@abstractmethod
	def send_data_from_server_interface_to_Bl(self):pass
	@abstractmethod
	def get(self):pass	
	@abstractmethod
	def run(self):pass	

	def choise_in_controller():
		return In_Controller()

		


class MSG_Formation(object):
	"""docstring for MSG_Formation"""
	def __init__(self, data):
		super(MSG_Formation, self).__init__()
		self.data = data
		# if data = dict:
		# 	self.data_dict = data

	def make_msg_from_data_dict(self):
		try:
			self.data_dict = json.loads(self.data)
			self.msg = str('%s: %s') % (self.data_dict["username"], self.data_dict["msg"])			
		except Exception as e:
			self.msg = self.data

	def run(self):
		self.make_msg_from_data_dict()
		return self.msg

class In_Controller(In_Controller_interface):
	# def send(self):
	# 	Main.get
	def get(self,data):
		self.data = MSG_Formation(data).run()
		self.BL.reseive(self.data)
		# send_to_BL = Main.send()
		# next(send_to_BL)
		# while True:
		# 	send_to_BL.send((yield))
	
	def send_data_from_server_interface_to_Bl(self):
		# cache = None
		while True:
			cache = None
			if cache != self.reseive.data:
				print(self.reseive.data)
				self.reseive.data = None

	def run(self):
		Thread(target = self.send_data_from_server_interface_to_Bl).start()




