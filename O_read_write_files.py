#Python Reference Guide Code Samples
#Ms G Hennessy - CUS
#Section O: Read/Write Files

# This demo comes with the test text file M_read1.txt
print("Using a read()")
myRFile=open("./M_read1.txt",'r')
#Show some file object attrubutes
print(myRFile.name, myRFile.encoding)
# Read from the file, either a number of characters
print(myRFile.read(12))
# ... or the whole file (note that it continues from previous read)
print(myRFile.read())
#Always close your file. We will reopen and start again
myRFile.close()

print("Using a readline()")
myRFile=open("./M_read1.txt",'r')
# You can also read a file, line by line
a = myRFile.readline()
print(type(a),a)
myRFile.close()

print("Using a readlines()")
myRFile=open("./M_read1.txt",'r')
# Or read all lines into a list - note readlines (plural)
filedump = myRFile.readlines()
print(type(filedump), filedump)
myRFile.close()

print("Using a for loop with the file object")
# Another way to read from a file
myRFile=open("./M_read1.txt",'r')
for myLine in myRFile:
    # I use end='' in the next line as each line contains \n
    print(type(myLine), myLine, end='')
myRFile.close()
print("\n")

# Now for writing to a file
myWFile=open("./M_write.txt",'w')
myWFile.write("First line of my text file!\n")
myWFile.write("Second line of my text file!\n")
myWFile.close()
# If we open this file for writing again, it will overwrite
# so we open for "append"

myAFile=open("./M_write.txt",'a')
myAFile.write("Third line of my text file!\n")
myAFile.close()

# This is not on our course, but it is a handy way to
# open a file without needing to close it.
with open("./M_write.txt", "r") as myFile:
    fileContent = myFile.read()
    print(fileContent)