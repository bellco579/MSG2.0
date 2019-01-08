import asyncio
class mainloop(object):
    def __new__(cls):
        # Перекрываем создание объекта класса
        if not hasattr(cls, 'instance'):
            cls.instance = super(mainloop, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        self.ioloop = asyncio.get_event_loop()
        self.tasks = []
    def add_task(self,task):
        print(type(task))
        self.tasks.append(self.ioloop.create_task(task()))
    def loop(self):
        wait_tasks = asyncio.wait(self.tasks)
        self.ioloop.run_forever()


