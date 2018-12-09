# from BL import in_controller


# class out(object):
# 	# def __init__(self, Data):
# 	# 	super(out, self).__init__()
# 	# 	# self.Data = Data
		
# 	def send_if_change(self):
# 		pass
# 	def get_data(self):
# 		pass
# 	def run(self):
		






























# from abc import abstractmethod,ABC
# from threading import Thread
# import time
# import json

# class Interface_OUT_Controller(ABC):
# 	def __init__(self,APP_name):
# 		# super(OUT_Controller, self).__init__()
# 		self.data = None
# 		self.APP_name = APP_name

# 	@abstractmethod
# 	def get(self):pass

# 	@abstractmethod
# 	def send(self):pass

# 	@abstractmethod
# 	def run(self):pass


# class OUT_Controller(Interface_OUT_Controller):
# 	def send(self,data):	
# 		print(data)

# 	def get(self):
# 		cash = None
# 		while True:
# 			if self.data != cash:
# 				temp = str(str(time.clock()),':',str(self.data))
# 				with open('log.txt') as log:
# 					log.writeln(temp)
# 				self.send(self.data)
# 				cash = self.data



# 	def run(self):
# 		Thread(target = self.get).start()
# 		# Thread(target = send).start()


# '''
# packege sample {{}}

# {"security key":"jshsfgfgjk","APP":"GUI","msg":"masange"}

# '''