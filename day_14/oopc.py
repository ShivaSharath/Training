class cse:
    def __init__(self):
        print("default")
class two:
    def fun1(self):
        print("fun2-mother")
class three(two,cse):
    def fun5(self):
        print("5")
o=cse()
a=two()
b=three()
b.fun5()