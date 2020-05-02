# The for Loop
print(range(5))  # range(0, 5) range object.
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]  start 1 end 10 increase 2

# print 1 ... 5
for number in range(5):  # for number in [0, 1, 2, 3, 4]:
    print(number)

# iterate over a dictionary.
a_dict = {"one": 1, "two": 2, "three": 3}
for key in a_dict:
    print(key)

a_dict = {10: "one", 2: "two", 5: "three"}
keys = a_dict.keys()
keys = sorted(keys)
for key in keys:
    print(key)

# The while Loop
i = 0

while i < 10:
    if i == 3:
        i += 1
        continue

    print(i)

    if i == 5:
        break
    i += 1
# more for
my_list = [1, 2, 3, 4, 5]

for i in my_list:
    if i == 3:
        print("Item found!")
        break
    print(i)
else:
    print("Item not found!")


