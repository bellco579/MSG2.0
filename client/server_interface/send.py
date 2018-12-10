from .interfaces import Send_Data


from abc import abstractmethod,ABC

class Send_Interface(ABC):
	# def __init__(self):
	# 	super(Send_Interface, self).__init__()
	
	def run(self):
		return 'send interface'




# class Send(Send_Data):
# 	def run(self):
# 		pass
# 		# cash = None
# 		# while True:
# 		# 	if (self.GUI.send_msg != None) and (self.GUI.send_msg != cash):
# 		# 		self.client_socket.send(bytes(self.GUI.send_msg, "utf8"))
# 		# 		cash = self.GUI.send_msg
