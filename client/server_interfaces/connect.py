from socket import AF_INET, socket, SOCK_STREAM
import pickle

# GUI
class Connect(object):

	def __new__(cls):
		# Перекрываем создание объекта класса
		if not hasattr(cls, 'instance'):
			cls.instance = super(Connect, cls).__new__(cls)
		return cls.instance



	def connection(self):
		host = "localhost"
		port = 8000
		ADDR = (host, port)
		self.client_socket = socket(AF_INET, SOCK_STREAM)
		self.client_socket.connect((host, port))
		print("connect to ", host)
if __name__ == '__main__':
	Connect()