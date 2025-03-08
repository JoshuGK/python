# example of prime number program
no=int(input("enter a no:"))
if no>0:
    for i in range(2,no):
        if no%2==0:
            print(no,"is not a prime number")
            break
        

    else:
        print(no,"is a prime no")
        
elif no==1:
    print(no,"is neither prime or composite")


else:
    print(no,"is not a prime number")
#code to check leap years
def year():
    

