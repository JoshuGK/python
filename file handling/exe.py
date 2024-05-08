#creating own exception
class MyException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return ()
#example using guess
class valuelowexception(Exception):
    pass
class valuehighexception(Exception):
    pass
number=80
while True:
    try:
        guess=int(input("enter a number:"))
        if guess<number:
            raise valuelowexception
        elif guess==number:
            print("your guess is correct")
            break
        else:
           raise valuehighexception
    except valuelowexception:
        print("your guess is low")
    except valuehighexception:
        print("your guess is high")
    except ValueError:
        print("enter only intergers")


    