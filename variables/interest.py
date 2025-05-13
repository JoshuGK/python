#python compound interest calculator
principle=0
rate=0
time=0

while principle<=0:
    principle=float(input("enter the principle amount"))
    if principle <=0:
        print("principle cant be zero")

while rate<=0:
    rate=float(input("enter the interest rate "))
    if rate <=0:
        print("rate cant be zero")

while time<=0:
    time=float(input("enter the time in yeras"))
    if time <=0:
        print("time cant be zero")

total= principle * pow((1+rate/100),time)
print(f"balance after {time} years: total is {total}")