#Python Reference Guide Code Samples
#Ms G Hennessy - CUS
#Section C: Comparison Operators

# Very important to use == when you are testing if two variables are equal
# Here we are assigning a value to a and b using a single "="
a = 1
b = 2
# Now we are comparing ... the result will be a Boolean "False"
print(a==b)
# Often used in an if statement
if(a==b):
    print("Equal")
else:
    print("Not equal")
    
# We use != in many languages to mean not equal
if(a!=b):
    print("Not equal")
else:
    print("Equal")
print(a!=b)

# Less than and greater than are as expected. For "less than or equal" or
# "greater than or equal" use <= and >=
print(a<=b,a<b,a>=b,a>b)
