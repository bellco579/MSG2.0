import tkinter
from Data_Entry import Data_Entry
from threading import Thread
# from controller import Send_Data 
from BackEnd.Ready_to_Send import Ready_to_Send
class Tkinter():
	"""docstring for Tkinter"""
	def __init__(self,client_socket = None):
		super(Tkinter, self).__init__()
		self.client_socket = client_socket
		self.RTS = Ready_to_Send(self.client_socket)
		self.data = None
	
	def send(self,event=None):  # event is passed by binders.
	    """Handles self.sending of messages."""	
	    msg = self.my_msg.get()
	    # print(msg)
	    self.RTS.send(msg)
	    self.my_msg.set("")  # Clears input field.
	    # self.client_socket.send(bytes(msg, "utf8"))
	    if msg == "{quit}":
	        self.client_socket.close()
	        self.top.quit()


	def on_closing(self,event=None):
	    """This function is to be called when the window is closed."""
	    self.my_msg.set("{quit}")
	    self.send()
	    self.get(brack = False)

	def run(self):
		self.top = tkinter.Tk()
		self.top.title("Chatter")

		messages_frame = tkinter.Frame(self.top)
		self.my_msg = tkinter.StringVar()  # For the messages to be sent.
		self.my_msg.set("Type your messages here.")
		scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
		# Following will contain the messages.
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

	def get(self):
		while True:
			self.msg_list.insert(tkinter.END,Data_Entry().get())

		receive_thread = Thread(target=self.get)
		self.top.protocol("WM_DELETE_WINDOW", self.on_closing)	
		tkinter.mainloop()
