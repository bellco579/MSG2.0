from .IO import Reseive_Data


class Reseive(Reseive_Data):
	def run(self):
		while True:
			try:
				msg = self.client_socket.recv(1024)
				self.GUI.msg = msg
			except OSError:
				break

