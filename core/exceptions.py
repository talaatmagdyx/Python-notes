# ############ Common Exceptions #####################
# Exception (this is what almost all the others are built off of)
# AttributeError - Raised when an attribute reference or assignment fails.
# IOError - Raised when an I/O operation (such as a print statement, the built-in open() function or a method of a file object) fails for an I/O-related reason, e.g., “file not found” or “disk full”.
# ImportError - Raised when an import statement fails to find the module definition or when a from … import fails to find a name that is to be imported.
# IndexError - Raised when a sequence subscript is out of range.
# KeyError - Raised when a mapping (dictionary) key is not found in the set of existing keys.
# KeyboardInterrupt - Raised when the user hits the interrupt key (normally Control-C or Delete).
# NameError - Raised when a local or global name is not found.
# OSError - Raised when a function returns a system-related error.
# SyntaxError - Raised when the parser encounters a syntax error.
# TypeError - Raised when an operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.
# ValueError - Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as IndexError.
# ZeroDivisionError - Raised when the second argument of a division or modulo operation is zero.

# ############# How to Handle Exceptions ################
try:
    1 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")  # You cannot divide by zero!

# Bare Excepts
# Here’s another way to catch the error:
try:
    1 / 0
except:  # PEP 8: E722 do not use bare 'except'
    print("You cannot divide by zero!")

# another execption
my_dict = {"a": 1, "b": 2, "c": 3}
try:
    value = my_dict["d"]
except KeyError:
    print("That key does not exist!")

my_list = [1, 2, 3, 4, 5]
try:
    my_list[6]
except IndexError:
    print("That index is not in the list!")

# Here’s another way to catch multiple exceptions:
my_dict = {"a": 1, "b": 2, "c": 3}

try:
    value = my_dict["d"]
except (IndexError, KeyError):
    print("An IndexError or KeyError occurred!")

# The finally Statement
my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["d"]
except KeyError:
    print("A KeyError occurred!")
finally:
    print("The finally statement has executed!")

# The try/except statement also has an else clause
my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["a"]
except KeyError:
    print("A KeyError occurred!")
else:
    print("No error occurred!")