#Python Reference Guide Code Samples
#Ms G Hennessy - CUS
#Section R: Off-Piste

# These are some very handy python features which are not on the
# reference guide, but are worth knowing

# 1. First is the string.join() method.
print("*"*10,"1 The string.join() method","*"*10)
myString="*"
newString = myString.join(['a','b','c'])
print("myString after join",newString)  # Output is "a*b*c"

# This doesn't seem very useful UNLESS you have a list of characters
# which you want to convert into a string
myList=["D","O","G"]
print(str(myList))   # Doesn't do what you might expect
                     # Output includes "[" and """ etc
newString="".join(myList)
print(newString)     # This works. Note that the string that the method
                     # is operating on is just an empty string
newString="-".join(myList)
print(newString)     # This gives us D-O-G

# 2. string.__contains__() method
print("*"*10,"2. string.__contains__() method","*"*10)
# Works just like "in" for lists
myList=["North","South","East","West"]
if "East" in myList:
    print("It is in the list")

myString= "NorthSouthEastWest"
if myString.__contains__("East"):
    print("It is in the string (used __contains__())")
# Alternatively, we can use the "in" statement which is on the ref guide
# for lists. It works for strings also.
if "East" in myString:
    print("It is in the string (used \"in\")")

# 3. end=" " or end="" attribute
# BTW, notice in the next line that I have to escape the
# quote if I want to print " " or similar on the output
print("*"*10,"3. end=\" \" or end=\"\" attribute","*"*10)
# Usually used with print()
print("this", end=" ") # print automatically adds a space and a newline.
print("and this on the same line")
# You can make end ="anything"
print("print", end="anything")
print()     # You may have to manually add a newline
print("\n\n\n") # or three

# 4 Dictionaries
print("*"*10,"4. Fun with Dictionaries","*"*10)
# This is a whole different data structure, made up of key:value pairs
# You find an item in a list through its index.
# You find an item in a dictionary using its key
dict1={
    "A": "The first letter of the Alphabet",
    "B": "Might sting you",
    "C": "Go Sailing"
    }
print(dict1)      # Print the whole dictionary
print(dict1["C"]) # Prints the value corresponding to the Key given

# Also, the "in" statement works for dictionaries too
# It just returns a True/False, not the value of the dictionary entry
if "A" in dict1:
    print("A is in the dictionary")  
if "D" not in dict1:
    print("D is not in the dictionary")
    
#You can also create a dictionary using the dict() function
dict2 = dict(D = "Dee", E = 2.71828, F = "Eff")
print(dict2["E"])


# You can add items
dict2["newKey"] = "some random value"
print(dict2)

# A very useful feature: the value can be anything including a list
dict3={
    "name": "Tom Riordan",
    "age": 19,
    "subjects": ["Maths","English","Irish","ComputerScience"]
    }
print(dict3["name"],dict3["subjects"][1]) # Print name and second item in subjects list

# 5 Off off-piste we have the zip() function
print("*"*10,"5 The zip() function","*"*10)
# If you are a fan of dictionaries, you can create one from 2 lists by literlly (?) zipping them together
# Two lists with equal numbers of elements (if the lists are not equal length, surplus elements that
# don't pair off are ignored
names=["Larry","Paul","Adam","Frank","Martin"]
scores=[2,3,4,7,8]

zippedObject =zip(names,scores)
print("After zip", type(zippedObject),zippedObject)
dictFromZip=dict(zippedObject)
print("Now a dictionary",dictFromZip)

# 6 Weird print. You don't need to know this
# You can use the print function as it is shown
# in the reference guide
print("*"*10,"6  Weird print or f-strings","*"*10)
a =68
b = "Tom"
print(b, "is", a,"kg in weight")
# or using the f string
print(f"{b} is {a}kg in weight")
