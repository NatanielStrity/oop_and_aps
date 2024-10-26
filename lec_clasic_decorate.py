class MyClass:
    counts = 0

    def __init__(self):
        MyClass.counts = MyClass.counts + 1

    @classmethod
    def classmethod(cls):
        print(cls.counts)


MyClass.classmethod()
mc = MyClass()
MyClass.classmethod()