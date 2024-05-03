#functions in python-are of two types:1.built in functions,2.user defined functions
#built in functions:includes;print(),input(),type(),len(),range(),id() etc

#user defined functions:-include;functions with arguements,functions with return value,functions without arguements,functions without return value
 
#example

#keyword type
def add(a,b):
    print(a+b)
add(10,20)

#default type
def add(b=6,a=5):
    print(a+b)
add()

#variable length type

def add(*n):
    sum=0
    for i in n:
        sum=sum+i
        print(sum)
add(10,20,30,40)
#or
def add(*n):
    print(sum(n))
add(10,23)
add(5,7,8,9)

#local variable-defined inside a function; and global variable-defined outside a function
#example
a=10#global
b=20#glabal
def f1():
    print(a+b)
f1()
def f2():
    #glabal c-changes it to global variable
    c=30#local-
    print(a+b+c)
f2()
#defining a function inside a function
def f1():
    print("imout")
    def f2():
        print("im in")
        def f3():
            print("am on")
        f3()
    f2()   #calling f2
f1()     