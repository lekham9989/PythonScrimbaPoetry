# RANDOM MODULE - this module is not truly random. It's pseudo random--------------------
# There is module called 'random' module in Python, which has a lot of functions that generate random numbers.
# We can import the random module and call various functions in it, and generate random numbers.Its becoms very easy to generate various types of random numbers, if once we import the module.
# import-keyword  random-moduleName
import random

# There is a function in random module called, random() which generates random numbers between 1 & 0
print(random.random())
# creates random number once

# create random number 5 times - for loop
for i in range(5):
    print(random.random())
    
# create random number 5 times between 1 and 6
for i in range(5):
    print(random.random()*6)
    
# create random numbers between 1,6 using uniform function
# uniform function takes 2 specific numbers values and gives random num between them
for i in range(5):
    print(random.uniform(1,7))
    
# To create random integers :we use randint function: we have to specify between what 2 numbers you need random integers
for i in range(5):
    print(random.randint(5,20))

# create random integers between 2 numbers with a step : we use randrange function
# generates 5 random numbers from, numbers between 1 and 100 by steps of 2, ie like 1,3,5,7....till 100 and not more than 100.
# generate odd numbers between 1 and 100
for i in range(5):
    print(random.randrange(1,100,2))
    
# generate even numbers
for i in range(5):
    print(random.randrange(2,100,2))

# we also can work with strings using random module not just numbers
friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']

# print a random name from friends_list
print(random.choice(friends_list))
# random is module, choice is function from random

# pick random name from friends_list 4 times : we use for loop
for i in range(4):
    print(random.choice(friends_list))
    
# draw few names from friends_list randomly : sample draws a specific number of names from the list, takes an argument, you have to specify how many names must be in the sample.(number can't be more than the length of the list)
# sample has no repeated values in it, it picks unique values in the sample
print(random.sample(friends_list,4))

# we can shuffle the list and get random shuffled list : use shuffle function
# you have to first shuffle and then print the list. cant do it in a single print statement
random.shuffle(friends_list)
print(friends_list)
