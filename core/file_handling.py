# Python has a builtin function called open that we can use to open a file for reading

# open file & read file use mode 'r'
try:
    handle = open("test.txt", 'r') # add path of file
    # read file
    print(handle.read())
    # read just one line
    data = handle.readline()
    # read ALL the lines!
    data1 = handle.readlines()
    # close file
    handle.close() # better close file
except FileNotFoundError:
    print("File not found")

# How To Read Files Piece by Piece
#  read a file in chunks is to use a loop
# how to read a file line by line and
try:
    handle = open("test.txt", "r")
    for line in handle:
        print(line)
    handle.close()
except FileNotFoundError:
    print('File Not Found')

# how to read it a kilobyte at a time
try:
    handle = open("test.txt", "r")

    while True:
        data = handle.read(1024) # kilobyte is 1024 bytes or characters
        print(data)
        if not data:
            break
except FileNotFoundError:
    print('File Not Found')


# ########### How to Read a Binary File ###################
try:
    handle = open("test.pdf", "rb") #  changed the file mode to rb, which means read-binary
except FileNotFoundError:
    print("file not found")

# write in file will be overwritten with no warning!
try:
    handle = open("test.txt", "w")
    handle.write("This is a test!")
    handle.close()
except FileNotFoundError:
    print('File Not Found')

# Now let's read the file that we just wrote
try:
    handle = open("test.txt", "r")
    for line in handle:
        print(line)
    handle.close()
except FileNotFoundError:
    print('File Not Found')

# Using the with Operator
# Python has a neat little builtin called with which you can use to simplify reading and writing files
# The with operator creates what is known as a context manager in Python
# that will automatically close the file for you when you are done processing it
with open("test.txt") as file_handler:
    for line in file_handler:
        print(line)

# Catching Errors in file handling
file_handler = None
try:
    file_handler = open("test2.txt")
    for line in file_handler:
        print(line)
except IOError:
    print("An IOError has occurred!")
finally:
    if file_handler is not None:
        file_handler.close()

# Catching Errors in file handling
# use with
try:
    with open("test2.txt") as file_handler:
        for line in file_handler:
            print(line)
except IOError:
    print("An IOError has occurred!")