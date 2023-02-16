#Python Reference Guide Code Samples
#Ms G Hennessy - CUS
#Section J: List Methods

#Define a list with just 2 items
cities=["Ankara","Barcelona"]

#Append an item to the list (at the end)
cities.append("Cork")
print(cities)

#Append another list to the list
otherCities=["Galway","Helsinki","Zagreb"]
cities.extend(otherCities)
print(cities)

#Insert an item into the list at a particular position
cities.insert(3,"Dublin")
print(cities)

#Remove an item from the list by name (not by index)
cities.remove("Barcelona")
print(cities)
#cities.remove("Madrid") would cause an error: Must be in the list
#print(cities)

#Remove an item from the list by index
#Note that pop() method returns a value
city=cities.pop(2)
print("Just popped", city," from the list which now looks like this :",cities)

#Remove all items from the list 
cities.clear()
print("After clear(), we have cities = :",cities)

#Reinstate my list of cities
cities=["Ankara","Barcelona","Cork","Dublin","Edinburgh","Faro"]

#Return the position of the first occurence of an item in the list
print("The city of Dublin occurs at position : ", cities.index("Dublin"))

#Return the number of occurences of an item in the list
print("The city of Dublin occurs this many times : ", cities.count("Dublin"))
cities.append("Dublin") #Add another occurrence to test the count
print("Now, the city of Dublin occurs this many times : ", cities.count("Dublin"))
#Remove the duplicate "Dublin" - note, this removes the first occurrence
cities.remove("Dublin")

# Sort the list
print("Before the sort :",cities)
cities.sort()
print("After the sort :",cities)

#Alternatively create a new list of sorted items, leaving the first list unchanged
cities.append("Helsinki")
cities.append("Galway")
newCities=sorted(cities)
print("Cities list :",cities)
print("Copied and sorted lust :",newCities)

#Reverse the order of elements in a list
cities.reverse()
print("Reverse order :",cities)

#Make a copy of a list
copyCities=cities.copy()
print("Copy of list:",copyCities)