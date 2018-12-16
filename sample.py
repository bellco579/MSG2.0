import pickle

class tst(object):
	"""docstring for tst"""
	def __init__(self, arg):
		super(tst, self).__init__()
		self.arg = arg


test = tst(4)
with open("test.pkl", "wb") as pk_file:
	pickle.dump(test,pk_file)