# The if statement
if 2 > 1:
    print("This is a True statement!")  # This is a True Statement!

var1 = 1
var2 = 3

if var1 > var2:
    print("This is also True")
else:
    print("That was False!")

value = input("How much is that doggy in the window? ")
value = int(value)

if value < 10:
    print("That's a great deal!")
elif 10 <= value <= 20:
    print("I'd still pay that...")
else:
    print("Wow! That's too much!")

# or
x = 10
y = 20

if x < 10 or y > 15:
    print("This statement was True!")

# and
x = 10
y = 10
if x == 10 and y == 15:
    print("This statement was True")
else:
    print("The statement was False!")

# not
my_list = [1, 2, 3, 4]
x = 10
if x not in my_list:
    print("'x' is not in the list, so this is True!")

# not vs !
my_list = [1, 2, 3, 4]
x = 10
z = 11
if x not in my_list and z != 10:
    print("This is True!")

# Checking for Nothing
#  an empty string, tuple or list also evaluates to False.
#  There is also another keyword that basically evaluates to False which is called None
# The None value is used to represent the absence of value
# It’s kind of analogous to Null

empty_list = []
empty_tuple = ()
empty_string = ""
nothing = None

if empty_list == []:
    print("It's an empty list!")

if empty_tuple:
    print("It's not an empty tuple!")

if not empty_string:
    print("This is an empty string!")

if not nothing:
    print("Then it's nothing!")

# if __name__ == “__main__”
# You will see a very common conditional statement used in many Python examples.
if __name__ == "__main__":
    print("start")# do something!

# You will see this at the end of a file
# This tells Python that you only want to run the following code
# if this program is executed as a standalone file