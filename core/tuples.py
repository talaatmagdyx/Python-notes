# A tuple is similar to a list,
# but you create them with parentheses instead of square brackets.
# The main difference is that a tuple is immutable while the list is mutable.

# create tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0:3])  # (1, 2, 3)

another_tuple = tuple()

# casting

abc = tuple([1, 2, 3])  # list to tuple
abc_list = list(abc)  # tuple to list
print(abc_list)
print(abc)

