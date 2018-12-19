
import unittest
import sys
import os

sys.path.append(os.getcwd())
from main import Main, Connect

# class Test_Run(unittest.TestCase):
# 	def

class TestConnected(unittest.TestCase):
	def setUp(self):
		self.connect = Connect()
	

if __name__ == '__main__':
	unittest.main()