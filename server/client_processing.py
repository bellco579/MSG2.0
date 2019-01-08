from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from abc import abstractmethod,ABC
import json 
from handle_client import Handle_Client_Interface as Handle_Client

class Client_Pocessing_Interface(ABC):
    def __init__(self, Server):
        super(Client_Pocessing_Interface, self).__init__()
        self.Server = Server
        with open('clients.json', encoding = "utf-8") as json_file:
            self.client_list = json.load(json_file)

    def run(Server):
        return Client_Processing(Server).run()

class Client_Processing(Client_Pocessing_Interface):
    
    def dump_to_file(self):
        with open('clients.json','w', encoding = "utf-8") as json_file:
            json.dump(self.client_list, json_file)

    def id_generation(self):
        if len(self.client_list) != 0:
            last_client = self.client_list[-1]
            # print(type(last_client["id"]))
            client_id = int(last_client["id"]) + 1
        else:
            client_id = 0
        return client_id

    def get_new_client(self):
        while True:
            new_client = {}
            client, client_address = self.Server.accept()
            print('new client:',client_address)
            new_client["id"] = self.id_generation()
            new_client["client_address"] = client_address
            self.client_list.append(new_client)
            self.dump_to_file()
            Handle_Client.run(client)
            client.send(b'connected')
            # Thread(target = handle_client, args = (client,))

    def run(self):     
        Thread(target = self.get_new_client).start()


class Run_Client_Pocessing_Interface():
    def __init__(self,Server):
        super(Run_Client_Pocessing_Interface, self).__init__()
        Client_Pocessing_Interface.run(Server)


