# COMPREHENSIONS
# Python comprehensions are cool tool to create tuple,list,sets and dictionaries with less code.
# maps,filters with lambda
# Anything you do with comprehension, you can do with for loop, but for loops require more core than comprehensions. So, comprehensions are smart to use.
# How to create a new list :
# name_of_the_list  gets(=) empty_square_braces[] -> creates a newlist
# ex: new_list = [] ---> creates an empty new list with name, new_list


numbers = [1,2,3,4,5,6,7,8,9]

# give me a list with num squared for each num in numbers
new_list = []
for num in numbers:
    new_list.append(num*num)
print(new_list)

# give me a list with num squared for each num in numbers - other way
new_list1 = [num*num for num in numbers]
print(new_list1)

# give me a list with num for each num in numbers if num is even
new_list3 = []
for num in numbers:
    if num % 2 == 0:
        new_list3.append(num)
print(new_list3)

# comprehension
new_list4 = [num for num in numbers if num % 2 == 0]
print(new_list4)

# give me a list with num for each num in numbers if num is odd
# new_list5 = [num, for num in numbers if num % 2 == 1]
new_list5 = [num for num in numbers if num % 2 != 0]
print(new_list5)

# using filter and lambda get a even list
new_list6 = list(filter(lambda num : num % 2 == 0, numbers))
print(new_list6)

# I want a (letter, num) pair for each letter in 'spam' and each number in '0123'
letters = 'spam'
nums = '0123'
pairs = []
for letter in letters:
    for num in nums:
        pairs.append((letter,num))
print(pairs)

new_list7 = []
for letter in 'spam':
    for num in range(4):
        new_list7.append((letter,num))
print(new_list7)

# comprehension
new_list8 = [(letter,num) for letter in 'spam' for num in range(4)]
print(new_list8)

# comprehensions actually contain the same code as in for loop