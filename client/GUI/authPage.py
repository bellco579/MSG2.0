import tkinter
import pickle

# from user import User
class User(object):
	"""docstring for User"""
	def __init__(self, username,password):
		super(User, self).__init__()
		self.username = username
		self.password = password
		

class AuthPage():
	def __init__(self):
		super(AuthPage, self).__init__()
		self.root = tkinter.Tk()
		self.log_dict = None
	def get_data(self):
		return self.log_dict
	def send(self,event = None):
		# username = self.username.get()
		# password = self.password.get()
		self.log_dict = {
			"username":self.username.get(),
			"password":self.password.get()
		}
		send(self.log_dict)
		# with open('user.pkl', 'wb') as pk_file:
		# 	user = User(username, password)
		# 	pickle.dump(user,pk_file)
		# print(username,password)

	def eliments(self):
		tkinter.Label(self.root, text = "username").pack()
		self.username = tkinter.Entry(self.root)
		self.username.pack()
		tkinter.Label(self.root, text = "password").pack()
		self.password = tkinter.Entry(self.root)
		self.password.pack()
		send_button = tkinter.Button(self.root, text="Send", command=self.send)
		send_button.pack()
	def run(self):
		self.eliments()
		# self.root.mainloop()
		return self.root
if __name__ == '__main__':
	AuthPage().run()