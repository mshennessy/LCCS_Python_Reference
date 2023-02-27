#Python Reference Guide Code Samples
#Ms G Hennessy - CUS
#Section K: Functions

# The print function has some useful features, note that blanks are inserted
# as separators automatically, but these can be replaced
print("north","south","east","west")
print("north","south","east","west", sep='+')
# Also, (not on ref guide) a newline is automatic but can be replaced
print("north","south","east","west",end='')
print("appears on same line")

# input("question") prints "question" and waits for a response, which is
# returned as a string
years=input("How many years")
print(years, type(years))  # It's a string

# len() returns the length of a list or string
myList=["north","south","east","west"]
myStr="Directions"
print(len(myList), len(myStr))

# min(list) returns the minimum value in a list
# For myList, it returns the alphabetically first element
# The second pairs of lists are set up as temporary objects just to
# demonstrate that strings are just sorted by the 1st digit if numeric
print(min(myList),min([94,41,145]),min(["23","47","114"]))
print(max(myList),max([94,41,145]),max(["23","47","114"]))

# These return an error: print(sum(myList)) print(sum(["23","47","114"]))
print(sum([94,41,145])) # Only works for numeric lists

# We mostly use range() in a for loop  (see section M) but this works
rangeOutput = range(1,20,2)
print("Showing range() :",rangeOutput) #it just prints range(1,20,2)
for i in rangeOutput:
    print(i)

# Absolute value and rounding are important for maths functions
# Abs() makes the output always positive
# and round(num,n) returns num rounded to n decimal places
a=-5
b= 3.141592654
print(abs(a),round(b,2))

# The next batch of functions cover finding out what type of variable you
# have type(x) and then functions for converting it to a string str(),
# a list list(), an integer int(), or a floating point (decimal) float()
print(str(b), list(myStr), int(b), float(a))

# A Boolean represents either True or False (or 1 or 0)
# bool() converts the parameter to a boolean value
# Pretty much anything other than 0, [], "", False will return True
x=0
y=True
z=[]
print(bool(x),bool(y),bool(z))

# Another way to do powers (apart from 2**10)
print("2^10 :",pow(2,10))

# The next two functions are for changing to/from UniCode
# chr() returns the string of a Unicode and ord() does the reverse
print("from unicode :",chr(465))
print("to unicode:",ord('Ǒ'))
# A related function not on the reference guide
print(hex(465))

# If you have a function such as chr() or a function you wrote yourself you
# can apply to to every element of a list using map
def add5(x):
    return x+5
print(add5(3))
numList = [4,6,11,8]
x = map(add5,numList)
y = map(chr,numList)
print(numList,list(x),list(y))