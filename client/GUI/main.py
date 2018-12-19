import tkinter
import pickle
from .authPage import AuthPage
from .TK import Tkinter 
from threading import Thread

class SetPage(object):
	"""docstring for SetPage"""
	def __init__(self):
		super(SetPage, self).__init__()
	def GUI_run(self):
		self.GUI.run()
	def run(self):
		self.GUI = Tkinter()
		Thread(target = self.GUI_run).start()
		# return self.GUI



class Main():
	def __init__(self, send_to_bl):
		super(Main, self).__init__()
		self.send_to_bl = send_to_bl
		self.page = Tkinter()
		self.page.send_to_bl = self.send_to_bl
	# def run_Chat(self):
	# 	self.page = self.page(send_to_bl).run()

	def set_data(self,data):
		self.page.get(data)
	def start_chat(self):
		self.page.run()
	def run(self):

		Thread(target = self.start_chat).start()
		# print()
		# self.page.get(data)
		# self.data = data



# class Big_listening(object):
# 	"""docstring for Big_listening"""
# 	def __init__(self):
# 		super(Big_listening, self).__init__()
# 		self.objects_list = []
# 		while True:
# 			for obj in self.objects_list:
# 				self.data = obj.get_data


# class Main(object):
# 	"""docstring for Main"""
# 	def __init__(self):
# 		super(Main, self).__init__()
# 		self.big_listening = Big_listening()
# 		try:
# 			with open("	user.pkl") as pk_file:
# 				self.config = pickle.dump(pk_file)			
# 		except Exception as e:
# 			self.config = None

# 	def log_check(self):
# 		auth_page = AuthPage()
# 		self.big_listening.append(auth_page)
# 		self.root = auth_page.run()
# 	def run(self):
# 		self.log_check()
# 		self.root.mainloop()

if __name__ == '__main__':
	Main().run()