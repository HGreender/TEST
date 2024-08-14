from  Tetsik import *

class MyTest(Test):
    _counter = 0
    def __init__(self):
        super().__init__()
        self.prit = 'PrInT'

        MyTest._counter += 1
        self.id = MyTest._counter

    def prt(self):
        print(self.prit)


cls1 = MyTest()
cls1.prt()
print(cls1.id)

cls2 = MyTest()
print(cls2.id)

cls3 = MyTest()
print(cls3.id)