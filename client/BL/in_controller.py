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
	def send_to_bl(self):pass	
	@abstractmethod
	def run(self):pass	

	def choise_in_controller():
		return In_Controller()

		


class MSG_Formation(object):
	def __init__(self, data):
		super(MSG_Formation, self).__init__()
		self.data = data

	def make_msg_from_data_dict(self):
		try:
			self.data_dict = json.loads(self.data)
			self.msg = str('%s: %s') % (self.data_dict["username"], self.data_dict["msg"])			
		except Exception as e:
			self.msg = None

	def run(self):
		self.make_msg_from_data_dict()
		return self.msg

class In_Controller(In_Controller_interface):
	def send_to_bl(self):
		self.BL.reseive(self.data)

	def run(self,data):
		self.data = MSG_Formation(data).run()
		self.send_to_bl()



