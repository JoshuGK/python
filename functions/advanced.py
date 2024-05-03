#advanced functions

# 1.filter
def even(a):
    if a%2==0:
        return a
    else:
        return False
list1=[1,2,4,3,5,7,6]
print(list(filter(even,list1)))

#lambda function of above
print(list(filter(lambda a:a%2==0,list1)))

#lambda function for even numbers range of 100
print(list(filter(lambda a:a%2==0,range(100))))

# 2. map function-used to apply for all the elements in the list

list2=[1,2,3,4,5,6,7]

print(list(map(lambda a:a*2, list2)))
#reduce function
from functools import reduce
print(reduce(lambda a,b:a+b,list2))