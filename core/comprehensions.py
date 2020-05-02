x = ['1', '2', '3', '4', '5']
y = [int(i) for i in x]
print(y)  # [1, 2, 3, 4, 5]

#  flatten multiple lists into one
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatVec = [num for elem in vec for num in elem]
print(flatVec)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# generate Dictionary from numbers
print({i: str(i) for i in range(5)})  # {0: '0', 1: '1', 2: '2', 3: '3', 4: '4'}

# swapping the dictionary’s keys and values
my_dict = {1: "dog", 2: "cat", 3: "hamster"}
print({value: key for key, value in my_dict.items()})  # {'dog': 1, 'cat': 2, 'hamster': 3}

# set form list
my_list = [1, 2, 2, 3, 4, 5, 5, 7, 8]
my_set = {x for x in my_list}
print(my_set) # {1, 2, 3, 4, 5, 7, 8}