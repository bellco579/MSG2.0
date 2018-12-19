import asyncio
from server_interfaces.reseive import Reseive
from server_interfaces.send import Send
from concurrent.futures import ThreadPoolExecutor
from GUI.main import GUI
class BL(object):
    def __init__(self):
        self.reseive_interface = Reseive()
        self.send_interface = Send()
        self.pool = ThreadPoolExecutor(3)
        self.tasks = []
    def send_to_server(self,data):
        self.send_interface.send_to_server(data)
    def run_GUI(self):
        GUI()
    def event_loop(self):
        cache = None
        self.run_GUI()
        while True:
            self.futures = self.pool.submit(self.reseive_interface.data_reseive)
            data = self.futures.result()
            if data != cache:
                self.data = cache = data
            self.send_to_server('data')

if __name__ == '__main__':
    BL()