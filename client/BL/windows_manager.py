from GUI.Frames.core import WinRoot
from GUI.Frames.auth import Auth
class WinController(object):
	"""docstring for WinController"""
	def __init__(self, frame_name):
		super(WinController, self).__init__()
		self.frame_name = frame_name
		self.WR = WinRoot()
		self.frame_nameDict = {
		"auth":Auth
		}
		self.change_frame()

	def change_frame(self):
		print(self.frame_name)
		print(self.frame_nameDict[self.frame_name])
		self.WR.new_Frame(self.frame_nameDict[self.frame_name])

# class DataHubForWin(object):
# 	"""docstring for DataHubForWin"""
# 	def __init__(self, arg):
# 		super(DataHubForWin, self).__init__()
# 		self.arg = arg
		