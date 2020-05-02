# Creating a list
# list like array in other language programming
my_list = []
my_list = list()

# example of list
my_list1 = [1, 2, 3]
my_list2 = ["a", "b", "c"]
my_list3 = ["a", 1, "Python", 5]

# lists of lists
my_list = [1, 2, 3]
my_list2 = ["a", "b", "c"]

my_nested_list = [my_list, my_list2]
print(my_nested_list)  # [[1, 2, 3], ['a', 'b', 'c']]

# Combining two lists
combo_list = [1]
one_list = [4, 5]
combo_list.extend(one_list)
print(combo_list)  # [1, 4, 5]

my_list = [1, 2, 3]
my_list2 = ["a", "b", "c"]

combo_list = my_list + my_list2
print(combo_list)  # [1, 2, 3, 'a', 'b', 'c']

# Sort a list
alpha_list = [34, 23, 67, 100, 88, 2]
alpha_list.sort()
print(alpha_list)  # [2, 23, 34, 67, 88, 100]

# Slice a list #
alpha_list = [34, 23, 67, 100, 88, 2]
alpha_list.sort()
print(alpha_list[0:3])  # [2, 23, 34]

