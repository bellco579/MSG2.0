import tkinter



class Auth(object):
    def __init__(self):
        self.root = tkinter.Tk()
    def send(self):
        print(self.username.get())
        print(self.password.get())
    def elements(self):
        tkinter.Label(self.root,text = 'username').pack()
        self.username = tkinter.Entry()
        self.username.pack()
        tkinter.Label(text='password').pack()
        self.password = tkinter.Entry()
        self.password.pack()
        self.send_btn = tkinter.Button(self.root,text = 'send',command = self.send)
        self.send_btn.pack()
    def run(self):
        self.elements()
        return self.root