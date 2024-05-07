#oops principles
#inheritance-represents properties of a particular class in another ie methods variables
class A:
    def m1(self):
        print("m1 method")
class B(A):
    def m2(self):
        print("class b")
class C(B):
    def m3(self):
        print("class c")
o=C()
o.m2()
o.m1()
o.m3()
#example single 2
class A:
    def m1(self):
        print("m1 method")
class B(A):
    def m2(self):
        print("class b")
o=B()
#o.m1()
#o.m2()
#iradicle inheritance
class A:
    def m1(self):
        print("m1 method")
class B():
    def m2(self):
        print("class b")
class C(A,B):
    def m3(self):
        print("class b")
o=C()
o.m1()
o.m2()
o.m3()
#hybrid inheritance
class A:
    def m1(self):
        print("m1 method")
class B(A):
    def m2(self):
        print("class b")
class C(A):
    def m3(self):
        print("class c")
class D(C,B):
    def m4(self):
        print("class D")
o=D()
o.m1()
o.m2()
o.m3()
o.m4()
#abstraction-hides unnecesary information to user
from abc import ABC,abstractmethod
class demo(ABC):
    @abstractmethod
    def calculate(self):
        pass
class A(demo):
    def calculate(self,a):
        print("double",a*2)
o=A()
o.calculate()


#encapsulation-enhances security feature / binding of data in a single class
class demo:
    a=10
    def m1(self):
        print(demo.a)
o=demo()
o.m1#or
print(o.a)



#polymorphism:many forms of method
#method overiding-
class parent:
    def car(self):
        print("take this BMW")
class child:
    def car(self):
        print("i wnt Benz")
o=child()
o.car()
#method overloading-mehod name is saved but parameters are different(not supported)
class demo:
    def add(self):
        print("zero parameters")
    def add(self,a):
        print("parameter 1")
    def add(self,a,b):
        print("parameter 2")
o=demo()
o.add()
#abstraction