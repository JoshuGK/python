#types of methods-1.class method,instance method,static method
#class method-has no instance class
class demo:
    #a=10
    @classmethod
    def m2(self):
        print("this is class method")
demo.m2()
#instance method

#static method-used when there is no class or instance method
class demo:
    @staticmethod
    def m1():
        print("this is static method")
demo.m1()

class demo:
    @staticmethod
    def add(a,b):
        print(a+b)
demo.add(10,20)
#constructor
#destructor