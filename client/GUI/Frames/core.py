import tkinter as tk
from abc import ABC, abstractmethod
from threading import Thread
import asyncio
from BL.mainloop import mainloop
# from GUI.MainFrame import MainFrame

class BaseFrameStructure(ABC):
    def __init__(self,frame):
        self.Frame = frame
        self.create_elements()
    @abstractmethod
    def create_elements(self):
        print('hello')


class WinRoot(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(WinRoot, cls).__new__(cls)
        return cls.instance

    def New_Windows(self):
        self.root = tk.Tk()
        # Thread(target=self.windows_update).s
        # self.root.mainloop()

    def clear_screen(self):
        for item in self.root.winfo_children():
            item.pack_forget()

    def new_Frame(self,frame):
        print("yes")
        self.clear_screen()
        self.new_frame = tk.Frame(self.root)
        frame(self.new_frame)
        self.new_frame.pack()
        # new_frame.update()

    async def windows_update(self):
            await self.root.mainloop()


class InputDataIntoFrame(object):
    """docstring for IputDataIntoFrame"""
    def __init__(self, arg):
        super(InputDataIntoFrame, self).__init__()
        self.arg = arg
        WinRoot().new_frame.set(self.arg)
        