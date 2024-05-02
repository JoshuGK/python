#LISTS-lists are mutable ie can be modified and no new object is formed
list1=[1,2,3,4,"come",True]
print(list1)
#indexing and slicing
print(list1[0])
print(list1[0:4])
print(list1[0:4:2]) # prints every second element i skips 2 elements

#list functions
print(len(list1))
#print(list1.max)
#list methods
list1.append("new") #adds new element to the list
list1.insert(1,"het") #inserts new element at given index
#list.extend
#list.pop
#list.remove
#list.reverse
#list.sort

#TUPLES-imutable ie cannot be modified does not necessarily need to be enclosed in ()
tup=1,2,3,4,True
#tuple functions
print(sorted(tup))
print(sum(tup))
print(max(tup))

#SETS-unordered collection of unique elements usually uses {}
set1={1,2,3,4,"true","$"}
u=3,44,5
set1.update(u)
print(set1)
#set1.pop()-removes any element
#set1.add()-adds
#set1.remove()-removes element available
#set1.discard()-removes element not available
#set1.union(b)-addstwo sets
#set1.intersection
#set1.difference(b)

#frozen set-same as sets but can be modified

#DICTIONARIES- represented with key value pairs and are mutable
#they dont suppoert operations like indexing slicing concatenation and multiplication
dict1={
    "name":"het",
    "age" : 20,
    "gender" :"male"
}
#dictionary functions
#.len()
#print(dict1.len())
#.clear()
#.get()
print(dict1.get(4))
#.pop()-removes
print(dict1.pop("name"))
#.popitem
#.keys
print(dict1.keys())
#.values
print(dict1.values())
#.copy
#.update
#dictionary methods


