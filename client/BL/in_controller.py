from .elements import *
from .mainloop import mainloop
from .windows_manager import WinController
class Choose_Elements(object):
    def __init__(self,data):
    	WinController("auth")
        # mainloop().add_task(auth)



class IN_controller(object):
    def __init__(self,data):
        self.data = data
        Choose_Elements(data)
