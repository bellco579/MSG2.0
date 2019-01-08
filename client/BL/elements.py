# from GUI.Frames.core import WinRoot
# from GUI.Frames.auth import Auth
# import asyncio
# from .mainloop import mainloop
# class auth(object):
#     def __init__(self):
#         self.AuthPage = WinRoot().new_Frame(Auth)
#         mainloop().add_task(self.get_logData)
#         print(self.AuthPage.password)
#     def login(self,data):
#         print(data)
#     async def get_logData(self):
#         pass
#         # print('geee')
#         # if self.AuthPage.logData != None:
#         #     self.login(self.AuthPage.logData)

class AuthProcessing(object):
    def __init__(self, logData):
        super(AuthProcessing, self).__init__()
        self.logData = logData
    def auth(self):
        print(self.logData)