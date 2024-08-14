from  Tetsik import *

class MyTest(Test):
    def __init__(self):
        super().__init__()
        self.prit = 'PrInT'

    def prt(self):
        print(self.prit)


cls = MyTest()
cls.prt()