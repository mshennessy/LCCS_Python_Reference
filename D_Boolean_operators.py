#Python Reference Guide Code Samples
#Ms G Hennessy - CUS
#Section D: Boolean Operators

# The basic Boolean Operators are AND, OR and NOT
# - the same operations you learned with logic gates
# Note that 1 = True and 0 = False 
a = True
b = 0
c = 1

print(a and c)
print(a or b)
print(not c)

# Mostly we use these in conditional statements
while True:
    #would loop forever so I'll insert a break
    break
d = 10 #Non boolean value for demonstration)
if(d>5 and a):
    print("d is greater than 5 (true) AND a is true (true)")

if(d<=20 or b):
    print("d is less than or equal to 20 (true) OR b is true (false)")
    
if(c and not b):
    print("c is true (true) AND NOT b is true (true)")
    
