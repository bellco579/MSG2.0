from threading import Thread

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
		print("BL:",self.data)
		self.GUI.msg = self.data

	def send_to_server(self):
		while True:
			if self.GUI.send_msg:
				self.msg = self.GUI.send_msg
				self.GUI.send_msg = None
				self.IO_interface["send"].run(self.msg)

	def run_GUI(self):
		Thread(target =self.GUI.run).start()
	
	def run_reseive_in_server_interface(self):
		Thread(target=self.IO_interface["reseive"].run).start()

	# def send_to_GUI(self):
	# 	while True:
	# 		self.GUI.msg = self.data
			# self.GUI.msg_list.insert(tkinter.END, self.data)
		# self.data = (yield)
		# print("BL:",self.data)
		# in_controller = self.IO_interface['reseive'].in_controller
		# print(in_controller)
		# in_controller.run()

	def run(self):
		self.run_GUI()
		Thread(target = self.send_to_server).start()
		# In_controller = In_Controller_interface.choise_in_controller()
