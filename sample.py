class Singleton(object):

    def __new__(cls):
        # Перекрываем создание объекта класса
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

        def __init__(self):
            self.data = 6

def a():

    s = Singleton()
    s.data = 10
    print(s)

def b():

    b = Singleton()
    print(b.data)

a()
b()