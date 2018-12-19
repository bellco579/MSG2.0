from server_interface.connect import Main as serInt
from threading import Thread
from BL.main import Main as BL
class Main():
	def run(self):
		server_interface = serInt()
		IO_interface = server_interface.get_interface_of_implmets_object()
		bl = BL(IO_interface)
		IO_interface["reseive"].in_controller.BL = bl
		bl.run()
	
if __name__ == '__main__':
	Main().run()