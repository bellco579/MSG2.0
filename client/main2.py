from server_interface import connect
from threading import Thread


class Main():
	# def __init__(self, arg):
	# 	super(Main, self).__init__()
	# 	self.arg = arg
	def run(self):
		server_interface = connect.Main()
		Thread(target = server_interface)




if __name__ == '__main__':
	Main().run()