import tkinter
from threading import Thread
from .GUI import GUI

class Tkinter(GUI):
	def __init__(self,client_socket):
		super(GUI, self).__init__()
		self.msg = None
		self.send_msg = None
		self.client_socket = client_socket
	def send(self,event=None):  
	    self.send_msg = self.my_msg.get()
	    self.my_msg.set("")  
	    if self.send_msg == "{quit}":
	        # self.client_socket.close()
	        self.top.quit()

	def on_closing(self,event=None):
	    self.my_msg.set("{quit}")

	def get(self):
		cash = None
		while True:
			if self.msg != cash:
				self.msg_list.insert(tkinter.END, self.msg)
				cash = self.msg

	def run(self):
		self.top = tkinter.Tk()
		self.top.title("Chatter")

		messages_frame = tkinter.Frame(self.top)
		self.my_msg = tkinter.StringVar()  
		self.my_msg.set("Type your messages here.")
		scrollbar = tkinter.Scrollbar(messages_frame)  

		self.msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
		scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
		self.msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
		self.msg_list.pack()
		messages_frame.pack()

		entry_field = tkinter.Entry(self.top, textvariable=self.my_msg)
		entry_field.bind("<Return>", self.send)
		entry_field.pack()
		send_button = tkinter.Button(self.top, text="Send", command=self.send)
		send_button.pack()

		Thread(target = self.get).start()
		self.top.protocol("WM_DELETE_WINDOW", self.on_closing)	
		tkinter.mainloop()


