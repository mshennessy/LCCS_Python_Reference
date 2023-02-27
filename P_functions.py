#Python Reference Guide Code Samples
#Ms G Hennessy - CUS
#Section P: Functions

# Use functions in code to avoid repeating blocks
# Well written functions help with the process of abstraction

# You must define a function before you call it
# In this code, we are drawing a grid of columns
# for some parts of our code, the number of columns might vary
# In this function we have abstracted away the details of layout
def formatOutput(numColumns, numRows):
    # This is a complicated function that calulates the optimal width
    # for each column. Assuming total available width is 40 characters
    width= 40//numColumns
    for i in range(numRows):
        print("|", end='')
        for j in range(numColumns):     #print gap plus "|" for each column
            print(" " * width, "|", end='') 
        print("\n", end='')  #This makes the lines appear better 

#Somewhere in our later code we call the function formatOutput() without
# needing to do any calculations. Details are abstracted away!
print("Here is a 10 column layout")
formatOutput(10,4)    #Will print 10 columns and 4 rows
# A later call
print("Here is a 3 column layout")
formatOutput(3,6)     #Will print 3 columns and 6 rows

# A function may or may not return a value. The value could be an int, str or list.
# This function is simulating an Attacker's diceroll in Risk. The parameter is the
# number of dice we are attacking with, and it returns an ordered list of results.
import random as r

# This function will throw a dice the given number of times
# and returns a sorted list of dice rolls
def rolldice(num):
    dicethrow=[]
    for i in range(num):
        dicethrow.append(r.randint(1,6))
    dicethrow.sort()
    dicethrow.reverse()
    return dicethrow

attack=[]
defence=[]
# Call the function rolldice() with parameter 3 for the Attacker
attack = rolldice(3)
# Player2 defends with 2 dice
defence= rolldice(2)
print("\nRisk simulation")
print("Attack:",attack)
print("Defence:",defence)

        