from abc import abstractmethod,ABC
import json
class Out_Controller_interface(ABC):
	"""docstring for Out_Controller_interface"""
	def __init__(self, send):
		super(Out_Controller_interface, self).__init__()
		self.send_interface = send
	
	@abstractmethod
	def sending(self):pass
	# def is_valid(self):pass
	# def preparation_to_sending(self):pass
	def choice_out_controller(send):
		return Out_Controller(send)






# class chacking_validation():
# 	def __init__(self, data_dict):
# 		super(chacking_validation, self).__init__()
# 		self.data_dict = data_dict
	
# 	def if_GUI(self):
# 		if data_dict["GUI"]["msg"]:
# 			return True

# 	def run(self)
class work_with_data_dict(object):
	def __init__(self, data,config):
		super(work_with_data_dict, self).__init__()
		if data != dict:
			self.data_dict = {}
			self.data_dict["msg"] = data
		else:
			self.data_dict = data
		self.config = config

	def insert_username_to_data_dict(self):
		self.data_dict["username"] = self.config["username"]
		return(self.data_dict)

	def run(self):
		self.insert_username_to_data_dict()
		print("data_dict:",self.data_dict)
		return(self.data_dict)

class Out_Controller(Out_Controller_interface):
	# def preparation_to_sending(self):
	def sending(self):
		data = json.dumps(self.data)
		self.send_interface.run(data)

	def run(self,data):
		with open('config.json', encoding ="utf-8") as jcon_file:
			config = json.load(jcon_file)
		self.data = work_with_data_dict(data,config).run()
		self.sending()
		