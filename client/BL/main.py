from threading import Thread
from .out_controller import Out_Controller_interface
from .in_controller import In_Controller_interface
from GUI.TK import Tkinter
# from out_controller import out_controller

class Main(object):
	def __init__(self,IO_interface = None):
		super(Main, self).__init__()
		self.IO_interface = IO_interface
		self.data  = None
		self.GUI = Tkinter()

	def reseive(self,data):
		self.data = data
		self.GUI.msg = self.data

	def send_to_server(self):
		out_controller = Out_Controller_interface.choice_out_controller(self.IO_interface["send"])
		while True:
			if self.GUI.send_msg:
				self.msg = self.GUI.send_msg
				self.GUI.send_msg = None
				out_controller.run(self.msg)

	def run_GUI(self):
		Thread(target =self.GUI.run).start()
	
	def run_reseive_in_server_interface(self):
		Thread(target=self.IO_interface["reseive"].run).start()


	def run(self):
		self.run_GUI()
		self.run_reseive_in_server_interface()
		Thread(target = self.send_to_server).start()
