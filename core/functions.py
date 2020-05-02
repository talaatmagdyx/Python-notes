# create functions in python
def a_function():
    print("You just created a function!")

a_function()  # call function

# An Empty Function (the stub)
def empty_function():
    pass

# Passing Arguments to a Function
def add(a, b):
    return a + b

print(add(1, 2)) # 3

def add(a, b):
    return a + b

add(1) # TypeError: add() takes exactly 2 arguments (1 given)


# ======= args and kwargs ==========
# *args   get infinite arguments
# **kwargs infinite keyword arguments
def many(*args, **kwargs):
    print(args)
    print(kwargs)

many(1, 2, 3, name="Mike", job="programmer")

# (1, 2, 3)
# {'job': 'programmer', 'name': 'Mike'}