



# class login(object):
# 	def __init__(self):
# 		super(login, self).__init__()
# class logout(object):
# 	"""docstring for logout"""
# 	def __init__(self, arg):
# 		super(logout, self).__init__()
# 		self.arg = arg
# class register(object):
# 	"""docstring for register"""
# 	def __init__(self, arg):
# 		super(register, self).__init__()
# 		self.arg = arg

class AuthProcessing(object):
	def init(self,logData):
		self.logData = logData
		print(self.logData)
		return True		