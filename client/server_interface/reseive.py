from .interfaces import Reseive_Data
from BL.in_controller import In_Controller as BL_in_controller

class Reseive(Reseive_Data):
	def run(self):
		BL = BL_in_controller()
		while True:
			try:
				BL.data = self.client_socket.recv(1024)
				# self.GUI.msg = msg
			except OSError:
				break

