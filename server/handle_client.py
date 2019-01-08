from abc import abstractmethod,ABC
from threading import Thread



class Handle_Client_Interface(ABC):
    def __init__(self,client):
        super(Handle_Client_Interface, self).__init__()
        self.client = client

    def run(client):
        Handle_Client(client).run()

class Handle_Client(Handle_Client_Interface):
    def reseive(self):
        while True:
            try:
                data = self.client.recv(1024)
                if data:
                    self.client.send(data)
            except Exception as e:
                break
    def run(self):
        Thread(target = self.reseive).start()

