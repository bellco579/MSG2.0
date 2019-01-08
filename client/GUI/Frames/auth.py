import tkinter
from .core import BaseFrameStructure
from BL.Elements.auth import AuthProcessing
# from BL.IN_controller import IN_controller
class Auth(BaseFrameStructure):

    def send(self):
        print(self.username.get())
        # print(self.password.get())
        self.logData = {
            "username":self.username.get(),
            "password":self.password.get(),
        }
        AuthProcessing().init(self.logData)
        print(self.logData)
        # IN_controller(self.logData)
    def create_elements(self):
        tkinter.Label(self.Frame,text = 'username').pack()
        self.username = tkinter.Entry(self.Frame)
        self.username.pack()
        tkinter.Label(self.Frame,text='password').pack()
        self.password = tkinter.Entry(self.Frame)
        self.password.pack()
        self.send_btn = tkinter.Button(self.Frame,text = 'send',command = self.send)
        self.send_btn.pack()
    # def run(self):
    #     self.Frame = tkinter.Tk()
    #     self.elements()
    #     self.Frame.update()
    #     print('fdfdf')
# if __name__ == '__main__':
#     Auth()