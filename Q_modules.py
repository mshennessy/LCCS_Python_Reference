#Python Reference Guide Code Samples
#Ms G Hennessy - CUS
#Section Q: Modules

# Python would be very bloated if it automatically included all
# features : random numbers, date handling, graphing tools etc
# We must import the specific module we wish to use
# I've included import statements in the code below at various
# positions just to show how it works
# Always put all of your import statements at the top
# There are a few ways to do this
import datetime         # full datetime module, we'll refer to it as datetime
import pygame as pg     # full pygame module, we'll refer to is as pg         
import matplotlib.pyplot as mpl  # just pyplot and we'll refer to it as mpl
from random import randint # just the randint() function, not all of random
                           # See more examples of this below
# The next one is not advised, as it is not clear where functions come from
from turtle import *    # full turtle module, but we can call functions directly

# Using datetime, we refer to methods this way
paddysDay=datetime.date(2023,3,17)
print(paddysDay)

# Using pygame modules, we can use the shorthand pg
#pg.init()               # Instead of pygame.init()
#screen = pg.display.set_mode([500, 500])

# Using matplotlib, we can use the shorthand mpl which is easier
mpl.plot([3,1,7,2])     # Instead of matplotlib.pyplot.plot()
mpl.show()

# From random, we can only use the randint() function
print("Here's a random number :", randint(1,10))
# Because we imported only randint() from random, we can't access
# other methods such as choice() or shuffle()
# Alternative 1:
import random     # All modules
# Now we have to specify the library.method()
print("Random number between 1 and 10:",random.randint(1,10))
print("Random Head/Tails choice:",random.choice(["Heads","Tails"]))
lettersList=["A","B","C","D","E","F"]
random.shuffle(lettersList)
print("Shuffled list :",lettersList)
# Alternative 2:
from random import randint
from random import choice
from random import shuffle
# Now we csn just name the method()
# Note that we now don't need the random.randint() here, just randint()
print("Random number between 1 and 10:",randint(1,10))
print("Random Head/Tails choice:",choice(["Heads","Tails"]))
lettersList=["A","B","C","D","E","F"]
shuffle(lettersList)
print("Shuffled list :",lettersList)

# We have the full turtle library imported and can access functions directly
myPen = Turtle()        # instead of turtle.Turtle()
for i in range(8):      # Draw an octagon
    myPen.forward(100)
    myPen.right(45)
done()                  # instead of turtle.done()