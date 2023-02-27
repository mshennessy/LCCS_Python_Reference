#Python Reference Guide Code Samples
#Ms G Hennessy - CUS
#Section N: Loop Control

# Break is used to exit the current while or for loop
while True:
    print("infinite loop unless I \"break\"")
    break
for i in range(20):
    print (i," ", end='')
    if i == 10:
        break
print("\n")
# Another example
x=0
while x < 10:
    print(x, " ", end='')
    while True:
        break # This breaks out of inner block only
    x+=1
print("\n")    
# Continue is used to skip over the remaining statements in the loop
# This example skips even numbers
for i in range(20):
    if i%2 == 0:
        continue
    print (i, " ", end='')
print("\n")

# Pass is simply a placeholder for future code
# - you can't have an empty for loop, or class definition
for i in range(20):
    pass