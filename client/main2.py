from server_interface.connect import Main as serInt
from threading import Thread
from BL.main import Main as BL
class Main():
	# def __init__(self, arg):
	# 	super(Main, self).__init__()
	# 	self.arg = arg
	def run(self):
		server_interface = serInt()
		IO_interface = server_interface.get_interface_of_implmets_object()
		server_interface.run()
		# Thread(target = server_interface.run,name = "server_interface").start()
		# reseive = IO_interface["reseive"].in_controller
		bl = BL()
		# reseive.BL = bl
		bl.IO_interface = IO_interface
		bl.run()
		# Bl = BL(IO_interface.data)
		# Bl.IO_interface = IO_interface
		# Thread(target = Bl.run).start()



if __name__ == '__main__':
	Main().run()