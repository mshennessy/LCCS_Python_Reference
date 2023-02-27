#Python Reference Guide Code Samples
#Ms G Hennessy - CUS
#Section G: String Operations

# Set up some strings to work on:
job="Teacher"
yrsExp=input("How many years of experience ?")

# Important: Strings are immutable objects. This means that they cannot be changed.
# Try uncommenting this line of code, which looks like it should replace T with X
# job[0]="X"

# type() helps us to check if a variable is a string
# python will return <class 'str'> which means you can use string operations and methods
print(type(job),type(yrsExp))       # Both are strings

# Strings behave like lists in some ways
# It is very important to remember that the first character in the string has index=0
# Also index [1:5] gives us characters 2,3,4 and 5
# and index [-2] is the second last character
print(job[0],job[1:5],job[-2],job[-1])