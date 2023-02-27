#Python Reference Guide Code Samples
#Ms G Hennessy - CUS
#Section I: List Operations

# Unlike strings, lists are meant to be updated, sorted, added to etc
# Define an empty list. Note that if you define a list this way,
# you must use list methods (see section J) to add items to the list
cities=[] # cities[0] = "Dublin" will return an out of range error

#Set up a list so we can demo the remaining list operations
fullCities=["Ankora","Barcelona","Cork","Dublin","Edinburgh","Faro"]
print(fullCities)
#Assign items to a list      list[i]=x
fullCities[0]="Ankara"
print(fullCities)

#Retrieve the item with index i
print(fullCities[2]) #the 3rd item

#Retrieve the last i items
print(fullCities[-2]) #the 2nd last item

#Retrieves a range from i to j or items
print(fullCities[2:5]) #the 3rd to 5th items (note we stop before item[5])

#Retrieves a range from i to the end
print(fullCities[3:]) #the 4th to the end

#Remove an item from the list
del fullCities[1] #Delete the 2nd item
print(fullCities)
