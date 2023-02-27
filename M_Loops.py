#Python Reference Guide Code Samples
#Ms G Hennessy - CUS
#Section M: Loops

#Different types of for loops
# for <variable> in <list>:
#     <code>
#For loop that steps through elements of a list
countryList=["Ireland", "Germany", "France","Spain"]
for country in countryList:
    print("This is a country :",country)

#For loop that repeats a specific number of times
# for <variable> in range (start,stop,step):
#     <code>
# x will take the values 0,1 and 2 on each iteration
for x in range(3):
    print(x, end='')
print("\n")
#Combining both and using len() to return the length of a list
for y in range(len(countryList)):
    print(countryList[y],end='')
print("\n")   
#For variable in range (start,stop,step)
for z in range(0,100,7):
    print(z," ",end='')
print("\n")
#For loop with a simple string
simpleString = "Simple String"
for a in simpleString:
    print(a, "-", end = '')
print("\n") 
#Simple while loop
# while <condition>:
#     <code>
#Keep adding 5 to a value while it is less than 50
myValue=0
while myValue < 50:
    print(myValue, " ",end ='')
    myValue += 5
print("\n")    
#infinite while loop with Boolean True condition
while True:
    print("forever")
    # comment out the next line for an infinite loop
    break

# You can combine a Boolean expressions in a while loop condition
a=1
b=3
while a < 10 or b > 0:
    a+=1
    b-=1
    print("a = ",a,"b = ",b, "-", end = '')

    