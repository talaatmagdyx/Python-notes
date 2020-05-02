# Python dictionary is basically a hash table or a hash mapping
# They are indexed with keys, which can be any immutable type
# keys must be unique

# create a dictionary
my_dict = {}
another_dict = dict()
my_other_dict = {"one": 1, "two": 2, "three": 3}

print(my_other_dict)  # {'three': 3, 'two': 2, 'one': 1}

# how to access a value in a dictionary
print(my_other_dict['one'])  # 1

# if a key is in a dictionary or not
my_dict = {"name": "Mike", "address": "123 Happy Way"}
print("name" in my_dict)  # True
print("state" in my_dict)  # False

# get a listing of all the keys in a dictionary
my_dict = {"name": "Mike", "address": "123 Happy Way"}
print(my_dict.keys())  # dict_keys(['name', 'address'])

"name" in my_dict         # this is good
"name" in my_dict.keys()  # this works too, but is slower
