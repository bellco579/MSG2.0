from .IO import Send_Data


class Send(Send_Data):
	def run(self):
		cash = None
		while True:
			if (self.GUI.send_msg != None) and (self.GUI.send_msg != cash):
				self.client_socket.send(bytes(self.GUI.send_msg, "utf8"))
				cash = self.GUI.send_msg
