from server_interfaces.connect import Connect
from server_interfaces.reseive import Reseive
from BL.main import BL
import asyncio
class Main(object):
    def __init__(self):
        Connect().connection()
        BL().event_loop()
    #     self.reseive = Reseive()
    #     self.tasks = [self.reseive.data_reseive]
    # def event_loop(self):
    #     loop = asyncio.get_event_loop()
    #     loop.run_until_complete(asyncio.wait(self.tasks))
if __name__ == '__main__':
    Main()
