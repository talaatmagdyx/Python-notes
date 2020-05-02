# ======================================
# === How to Create a String # =========
# ======================================
my_string = "Welcome to Python!"
another_string = 'The bright red fox jumped the fence.'
a_long_string = '''This is a
multi-line string. It covers more than
one line'''  # or """ """

# convert any type to string use --> str(...)
print(str(123))

# convert string to int use --> int(...)
print(int('123'))

# string is one of Python immutable types
my_string = "abc"
my_string[0] = "d"  # TypeError: 'str' object does not support item assignment

# Python 2.x, strings can only contain ASCII characters. If you require unicode
my_unicode_string = u"This is unicode!"

# Concatenation
string_one = "My dog ate "
string_two = "my homework!"
string_three = string_one + string_two

# get a list of all the string methods
print(dir("Python"))
# You can safely ignore the methods that begin and end with double-underscores,
# such as __add__. They are not used in every day Python coding. Focus on the other ones instead

# you want to learn what capitalize is for
print(help("my_string".capitalize))

# what type the variable
my_string = "This is a string!"
print(type(my_string))  # <class 'str'>

# String Slicing
# word index is from 0
my_string = "I like Python!"
print(my_string[:1])  # 'I'
print(my_string[0:12])  # 'I like Pytho'
print(my_string[0:13])  # 'I like Python'
print(my_string[0:14])  # 'I like Python!'
print(my_string[0:-5])  # 'I like Py'
print(my_string[:])  # 'I like Python!'
print(my_string[2:])  # 'like Python!'

# You can also access individual characters in a string via indexing
my_string = "I like Python!"
print(my_string[0])
print(my_string[2])
print(my_string[7])
print(my_string[100])  # IndexError: string index out of range

# Ye Olde Way of Substituting Strings
my_string = "I like %s" % "Python"
print(my_string)  # 'I like Python'

var = "cookies"
newString = "I like %s" % var
print(newString)  # 'I like cookies'

another_string = "I like %s and %s" % ("Python", var)
print(another_string)  # 'I like Python and cookies'

my_string = "%i + %i = %i" % (1, 2, 3)
print(my_string)  # '1 + 2 = 3'

float_string = "%f" % (1.23)
print(float_string)  # '1.230000'

float_string2 = "%.2f" % (1.23)
print(float_string2)  # '1.23'

float_string3 = "%.2f" % (1.237)
print(float_string3)  # '1.24'

int_float_err = "%i + %f" % ("1", "2.00")
print(int_float_err)  # TypeError: %i format: a number is required, not str

# Templates and the New String Formatting Methodology
print("%(lang)s is fun!" % {"lang": "Python"})  # Python is fun!

print("%(value)s %(value)s %(value)s !" % {"value": "SPAM"})  # SPAM SPAM SPAM !

print("%(x)i + %(y)i = %(z)i" % {"x": 1, "y": 2})  # KeyError: 'z'

# string’s format method!
print("Python is as simple as {0}, {1}, {2}".format("a", "b", "c"))
# 'Python is as simple as a, b, c'

print("Python is as simple as {1}, {0}, {2}".format("a", "b", "c"))
# 'Python is as simple as b, a, c'

xy = {"x": 0, "y": 10}
print("Graph a point at where x={x} and y={y}".format(**xy))  # Graph a point at where x=0 and y=10


