#object oriented programmes-
#class-is a blueprint of an object(plan)
#object-physical existing of a plan
#method-function inside a class ie self
#attribute-are variables
#reference variable-points to the object
class employee:
    def m1(self):#self is a default parameter
        print("this is method")
dharma=employee()      
dharma.m1()  
#constructor-is a special method which is called automatically when an object is created
#types of variables
#1.instsnce variables-variables inside a class
#2.static variables/class varables-variables which are common to everyone
#3.local variables

#class variable/static
class bank:
    bank_name="andara bank"
    def display(self):
        print(self.bank_name)
    def update(self):
        self.bank_name="srilanka bank"
Jog=bank()
rani=bank()
tuna=bank()

Jog.display()
rani.display()
tuna.display()

rani.update() 
rani.display

#instance variable-used for data unique for everyone
class bank:
    bank_name="andara bank"
    def __init__(self,accno,phno,address):#constructor
        self.accno=accno
        self.phno=phno
        self.address=address
    def display(self):
        a=10 #local variable
        print(self.accno)
        print(self.phno)
        print(self.address)
        print(self.bank_name)
    def update(self):
        self.bank_name="srilanka bank"
        self.phno="99913345265"
Jog=bank(1234,777,"kenya")
rani=bank(2222,888,"uga")
tuna=bank(5555,998,"tanz")

#load
#rani.load()
#Jog.load()
#tuna.load()
#Jog.display()
#rani.display()
#tuna.display()

Jog.display()
rani.display()
tuna.display()



