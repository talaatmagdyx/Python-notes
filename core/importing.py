# A module is a single importable Python file whereas a package is made up of two or more modules
import math
print(math.sqrt(4)) # 2.0
#  syntax: module_name.method_name(argument)

# Using from to import
from math import pi, sqrt

# =================== Importing Everything! ================
# Python provides a way to import all the functions and values from a module as well.
# This is actually a bad idea as it can contaminate your namespace
# A namespace is where all your variables live during the life of the program
from math import sqrt
sqrt = 5 # this shadowing
print(sqrt(16)) # TypeError: 'int' object is not callable