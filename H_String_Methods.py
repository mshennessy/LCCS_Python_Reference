#Python Reference Guide Code Samples
#Ms G Hennessy - CUS
#Section H: String Methods

# Remember that strings are immutable objects in Python which means that
# in the following methods, the string itself doesn't change
# Methods return a new string or True/False
startStr ="12 Main St"
newStr1 = startStr.upper()
newStr2 = startStr.lower()

print("Original string", startStr, "and new strings:",newStr1,newStr2)
# Count how many blanks are in the string and find the first one
print("There are ",startStr.count(" "), "blanks in the string")
print("The frist blank occurs at position :",startStr.find(" "))
# Replace a blank with an underline_
print(startStr.replace(" ","_"))
print(startStr)         # To show that the original string hasn't changed

# isupper, islower, isalnum, isalpha and isdigit work as described in
# the reference guide. They return True/False. Note that alphanumeric
# includes letters and numbers only - no spaces or * & + etc
testStr="123abc"
print(testStr.islower(),testStr.isupper(),testStr.isalnum())
print(testStr.isalpha(),testStr.isdigit())

# To find a string inside another string, we look for St in startStr above
# Note that it is case sensitive and returns an error if substring isn't present
print(startStr.index("St"))

# Strip the first and last characters that equal the parameter from the string
print(startStr.strip("1")) # Removes 1 at the start, would remove from end also
blankStr="  string with leading and trailing blanks         "
print("Before strip >",blankStr,"<\nAfter strip >",blankStr.strip(),"<")