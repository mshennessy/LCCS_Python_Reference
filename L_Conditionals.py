#Python Reference Guide Code Samples
#Ms G Hennessy - CUS
#Section L: Conditionals

# An in an if/elif.../else statement only 1 of the conditions can be true
# The colon after the if, the elif and the else are vital!
# if  <condition>: 
#     <code>
# elif<condition>: 
#     <code>
# elif<condition>: 
#     <code>   (as many elifs as you need)
# else:
#     <code>
x=int(input("Enter a number between 1 and 10:"))
if (x == 5):
    print("Correct")
elif (x<5):
    print("Too low")
else:
    print("Too high")

# If a list contains a value
myList = ["north","south","east","west"]
if "north-west" in myList:
    print("in list")
else:
    print("not in list")

#Also works for a string or a list element
if 'n' in myList[0]:
    print("there's an n in the first element")
    
if 'x' not in "abc":
    print ("not in abc")