#Python Reference Guide Code Samples
#Ms G Hennessy - CUS
#Section B: Numeric Operators

# Addition, subtraction and division are all obvious
# Multiplication is the asterisk *
print(5+2, 5-2, 5*2, 5/2)

# Exponent means "to the power of" and is done using ** double asterisk
print("5 to the power of 2 =", 5**2)
# From maths, remember that "to the power of 1/2" means square root
print("25 to the power of 1/2 =", 25**0.5)

# Modulus is the name given to a remainder when two numbers are divided
# The 15 modulus 7 is 1 (as the remainder when 15/7 is 1)
# Tip: checking for x%y == 0 is a test for divisibilty
print(15%7)

# Floor division is like the other half of modulus. It is the whole number
# result of the division ... always rounded down (hence "floor")
print(15//7)

print("15 divided by 7 equals",15//7, "remainder",15%7)

