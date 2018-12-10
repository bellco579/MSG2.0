from abc import abstractmethod,ABC
from threading import Thread

class In_Controller_interface(ABC):
	def __init__(self):
		super(In_Controller_interface, self).__init__()
		self.reseive = None
		self.data = None

	@abstractmethod
	def send_data_from_server_interface_to_Bl(self):pass
	@abstractmethod
	def run(self):pass	

	def choise_in_controller():
		return In_Controller()

		




class In_Controller(In_Controller_interface):

	def send_data_from_server_interface_to_Bl(self):
		# cache = None
		while True:
			cache = None
			if cache != self.reseive.data:
				print(self.reseive.data)
				self.reseive.data = None

	def run(self):
		Thread(target = self.send_data_from_server_interface_to_Bl).start()