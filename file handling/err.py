#types of errors
#syntax error-punctuationie wrong.responsible by developer
#logical error/bug-ie wrong arthmetic operation.responsible  by developer
#exception-is a runtime error responsible by the end user ie 100/0 giving zerodivision error

#Exception handling
#example using zero error division
a=int(input("enter a number:"))
b=int(input("enter second number"))
try:
    print("resource open")
    print(a/b)
    k=int(input("enter a number"))
    print(k)
    print("resource closed")
except ZeroDivisionError as e:
    print("hey,you cannot divide a number by zero",e)
    print("bye")
#or
a=int(input("enter a number:"))
b=int(input("enter second number:"))
try:
    print(a/b)
except:
    print("dont enter denominator 0")

#value error-ie when ender user gives a letter instead of a number
try:
   a =int(input("enter a number:"))
   b=int(input("enter second number"))
   print(a/b)
except ValueError:
    print("do not enter alphabets or special symbols")
except ZeroDivisionError:
    print("do not enter denominator 0")
    print("something went wrong")
finally:
    print("resource closed")

    
    
    
    

