from server_interfaces.connect import Connect
from server_interfaces.reseive import Reseive
from BL.mainloop import mainloop
from GUI.Frames.core import WinRoot
# import asyncio
# class Main(object):
#     def __init__(self):
#         Connect().connection()
#         BL().event_loop()
#
# if __name__ == '__main__':
#     Main()

class Main(object):
    def __init__(self):
        Connect().connection()
        self.mainloop = mainloop()
        self.WR = WinRoot()
        self.WR.New_Windows()
        self.inmplement_server_interface()
        self.mainloop.loop()
    def inmplement_server_interface(self):
        self.reseive = Reseive()
        self.mainloop.add_task(self.reseive.data_reseive)
        print(type(self.WR.windows_update))
        self.mainloop.add_task(self.WR.windows_update)

if __name__ == '__main__':
    Main()