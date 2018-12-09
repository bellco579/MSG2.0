# from main import Main
from threading import Thread


class In_Controller():
	def __init__(self):
		super(In_Controller, self).__init__()
		self.data = None

	def send_data_to_main(self):
		pass
	def get_data_from_server_interface(self):
		cache = None
		while True:
			if cache != self.data:
				print(self.data)

	def run(self):
		Thread(target = get_data_from_server_interface).start()