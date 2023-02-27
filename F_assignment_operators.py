#Python Reference Guide Code Samples
#Ms G Hennessy - CUS
#Section F: Assignment Operators

# =, +=, -= are very frequently used. The others are less important.
# if you have two variables note that the left variable is updated
a=5
b=7
a+=b
print("After a+=b: a is", a, "and b is",b)
a-=b
print("After a-=b: a is", a, "and b is",b)

# These are less used. The operator will just be shown directly
a*=b
print("After a*=b: a is", a, "and b is",b)
# Remember % gives the remainder
a+=1            #Add 1 so there will be a remainder
a%=b
print("After a%=b: a is", a, "and b is",b)
# /=
a/=b
print("After a/=b: a is", a, "and b is",b)
# Remember // is floor divide
a//=b
print("After a//=b: a is", a, "and b is",b)
print("Notice that b never changes")

