# example of prime number code program
no=int(input("enter an no:"))
if no>1:
    for i in range(2,no):
        if no%i==0:
            print(no,"is not a orime no")
            break
    else:
        print(no,"is a prime no")
        