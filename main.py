# Exercise 00: Write a program to find the type of the variable name
# Variable, name=”Hello there”, number=9876, list = [1, 'a'] etc.
def variable__type (variable__name):
    return type(variable__name)

name = 'Hello there'
print(variable__type(name))

number = 9876
print(variable__type(number))

name_list = ['Hello there', 123]
print(variable__type(name_list))

name_dict = {'age': 20, 'area': 'dhaka'}
print(variable__type(name_dict))

# Exercise 01: Write a program to find the length of the variable name
# Variable, name=”Hello there”

def length__fn(variable__name):
    return len(variable__name)

name = 'Hello there'
print(length__fn(name))


# Exercise 02: Write a program to find the type of the variable name
# name=”Hello there”

name = 'Hello there'
print(type(name))


# Exercise 03: Write a function that takes 2 numbers as arguments
# (age of two brothers) and find who is elder
# Hints: Use condition inside the function

def find__elder (age1, age2):
    if age1 > age2:
        return 'Brother 1 is elder'
    return 'Brother 2 is elder'

print(find__elder(39, 35))


# Exercise 04: Write a program to find the index of 7
# numbers=[3, 5, 1, 9, 7, 2, 8 ]

def find__index (variable__name, query):
    return variable__name.index(query)

numbers=[3, 5, 1, 9, 7, 2, 8 ]

print (find__index(numbers, 7))

for index, number in enumerate(numbers):
    print('{} index is {}'.format(index, number))


# Exercise 05: Write a program to sort the numbers in Ascending order
# numbers=[3, 5, 1, 9, 7, 2, 8 ]

numbers=[3, 5, 1, 9, 7, 2, 8 ]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

t = sorted(numbers)
print(t)

t = sorted(numbers, reverse = True)
print(t)

# Exercise 06: Write a function named “isLandscape” that
# takes 2 numbers (image width and height) as arguments 
# and the function returns Landscape if image width has higher value than height. 
# Returns Portrait otherwise
# Hints: Use condition inside the function

def isLandscape (width, height):
    if width > height:
        return 'Landscape image'
    return 'Portrait image'

print(isLandscape(480, 360))

def isIMGLandscape (urlPhrase):
    splitted_url = urlPhrase.split('.')
    splitted_size = splitted_url[2].split('x')
    if splitted_size[0] > splitted_size[1]:
        return 'Landscape image'
    return 'Portrait image'

url = 'https://adsfh.com/size.500x400.png'
print(isIMGLandscape(url))


# Exercise 07: FizzBuzz Exercise
# Write a function that takes 1 number as argument. 
# The function should return “Fizz” if the number is divisible by 3, 
# the function should return “Buzz” if the number is divisible by 5, 
# the function should return “FizzBuzz” if the number is divisible by both 5 and 3,
# otherwise return “Not a Fizz-buzz number”
# Hints: Use condition inside the function

def FizzBuzz (number):
    if number % 3 == 0 and number % 5 == 0:
        return '{} is a Fizz-buzz number'.format(number)
    elif number % 3 == 0:
        return '{} is a Fizz number'.format(number)
    elif number % 5 == 0:
        return '{} is a Buzz number'.format(number)
    return '{} is not a Fizz-buzz number'.format(number)

print(FizzBuzz(45))