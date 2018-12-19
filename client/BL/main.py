from threading import Thread
from .out_controller import Out_Controller_interface
from .in_controller import In_Controller_interface
# from GUI.TK import Tkinter
from GUI.main import SetPage as GUI_main
# from out_controller import out_controller
class Work_with_GUI(object):
	def __init__(self,In_interface):
		super(Work_with_GUI, self).__init__()
		self.GUI_main = GUI_main()
	def data_processing(self,data):
		self.GUI_main.get(data)
	def run_GUI(self):
		self.GUI = self.GUI_main.run()
		self.GUI_main.GUI.msg = "hello"
		# Thread(target = self.GUI_main.run).start()
		

class Main(object):
	def __init__(self,IO_interface):
		super(Main, self).__init__()
		self.IO_interface = IO_interface
		self.Work_with_GUI = Work_with_GUI(IO_interface['reseive'])
		self.data  = None
		# self.GUI = Tkinter()


	def reseive(self,data):
		self.data = data
		self.GUI.msg = self.data

	def send_to_server(self):
		pass
		# out_controller = Out_Controller_interface.choice_out_controller(self.IO_interface["send"])
		# while True:
		# 	if self.GUI.send_msg:
		# 		self.msg = self.GUI.send_msg
		# 		self.GUI.send_msg = None
		# 		out_controller.run(self.msg)

	def run_GUI(self):
		data = "work send data"
		self.Work_with_GUI.run_GUI()
		# self.Work_with_GUI.data_processing(data)
		# Thread(target =self.GUI.run).start()
	
	def run_reseive_in_server_interface(self):
		Thread(target=self.IO_interface["reseive"].run).start()


	def run(self):
		self.run_GUI()
		self.run_reseive_in_server_interface()
		Thread(target = self.send_to_server).start()
