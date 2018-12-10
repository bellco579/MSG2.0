from threading import Thread

from .in_controller import In_Controller_interface
# from out_controller import out_controller

class Main(object):
	def __init__(self):
		super(Main, self).__init__()
		pass
	def run(self):
		In_controller = In_Controller_interface.choise_in_controller()
		In_controller.reseive = self.IO_interface['reseive']
		# In_controller.run()
