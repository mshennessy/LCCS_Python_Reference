#Python Reference Guide Code Samples
#Ms G Hennessy - CUS
#Section A: Data Types

#A Boolean represents either True or False (or 1 or 0)
print("9 > 10 ?",9>10) # will print 9 > 10 ? False
# Declare a boolean variable this way
test = True
if test:
    print("Got here!")

# Integers are non-decimal numbers
myNum=7
print("My number is", myNum, "and it is type ", type(myNum))

# Floats are decimal values - short for floating point
# Note that I can redefine an integer as a float
myNum=3.14
print("My number is", myNum, "and it is type ", type(myNum))
print("My number + 0.86 is", myNum+0.86, "and it is type ", type(myNum+0.86))

# Strings are defined this way
myStr="Computer Science"
print(myStr, type(myStr))
# And can be easily added together
addStr=" is the best!!"
print(myStr+addStr)

# Lists are defined as either an empty list or with values
emptyList=[]
listWithContents=["Lisbon","Washington DC","Lima"]
listOfNumbers=[36.4,36.0,37.1,36.9]
# The elements of the list can be of different types
mixedList=[36.2,"Tampa",8,'N']
print(emptyList, listWithContents,"\n",listOfNumbers,mixedList)
