#format specifier= allows us to format a value based on what flags are inserted following: {value:flags}
#.(number)f = round to that many dp
#:(number) = allocates that many spaces
#:03 = allocates and zero pad that spaces
#:< = left justfy
#:> = right justify
#:^ = center align
#:+ = use a plus sign to indicate positive value
#:= = place asign to leftmost position
#:  = insert a space before positive numbers
#:, = comma separator
price=3.14567
price2= -33455.9
price3=12.98

print(f"price 1 is {price:.2f}")
print(f"price 2 is {price2:.1f}")
print(f"price 3 is {price3:.3f}")