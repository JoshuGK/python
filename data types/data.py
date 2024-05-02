#numerical data types include: int, float, complex, booleans
#strings -sequence of characters,are immutable
t="coming"
#string indexing
print(t[0])
print(t[1])
print(t[3])
print(t[-1])
#string slicing
print(t[1:4])
#strings are immutable-u cannot change if defined

#combining two strings
d="come"
print(t+d)

#assignment= write a program to read employee data from the keyboard and print the data which includes employer address salary and name

#string functions
a="coming home now"
print(a.capitalize()) # capitalizes first letter
print(a.title())      # converts every first letter to uppercase
print(a.islower())    # checks if string contains all lower case letters or not
print(a.isupper())    # opposite of islower function
print(a.upper())      # converts all letters to upper case , its opposite is lower
print(a.replace("home","school"))  #replaces given string with the required one
print(len(a))         # gives the leng of characters of the stings
print(a.count("o"))   #gives no of times a character is seen
print(a.split())

f="%%%home%%$"
print(f.strip("%"))    #removes the given character:adding l before strip removes the left side characters and adding r removes right side ones
#swapcase() fuction converts all lower case to upper case and vice varsa