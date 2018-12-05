# class controller():

# 	def reseive(self,Data = None):
# 		global data
# 		data = Data
# 		# with ('chat_log.txt', 'a') as chat_log:
# 		# 	chat_log.writeln(data)

# 	# def getData(self):
# 	# 	with ('chat_log.txt', 'r') as chat_log:
# 	# 		Data = chat_log.read()

# 	# 	with ('chat_log.txt', 'w') as chat_log:
# 			# return Data	
		
# 	def send(self,data):
# 		print(data)


class Controller(object):
 			def __init__(self, data):
 				super(controller, self).__init__()
 				self.data = data

class Get_Data(Controller):
	from GUI.TK import Tkinter
	def __init__(self, data):
		super(controller, self).__init__()
		self.data = data
		print(self.data)

class Send_Data(Controller):
	def __init__(self, data):
		super(controller, self).__init__()
		self.data = data
		print(self.data)


