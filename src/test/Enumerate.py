# Enumerate function creates tuples with a number and the name ex:(51,manu) (52,lavi)
# In python, this is the way we write to get a numbered list from any group.
friends = ['Peter','John','Rice','Rocy']
for num, friend in enumerate(friends,51):
    print(num,friend)


print(type(enumerate(friends)))
# When we find the type of enumerate(friends), we understand that enumerate(friends)is creating a class called 'ENUMERATE'
print(list(enumerate(friends)))
# makes a list of what enumerate(friends) does, ie, list of tuples



# In python, this is the way we write to get a numbered list from any group.
friends = ['Peter','Kale','Knight','Price']
for num, friend in enumerate(friends,51):
    print(num,friend)


print(type(enumerate(friends)))
# When we find the type of enumerate(friends), we undertand that enumerate(friends)is creating a class called 'ENUMERATE'
print(list(enumerate(friends)))
# makes a list of what enumerate(friends) does, ie, list of tuples

# In the process of enumerate function, computer will makes tuples and gives numbered list
# When we dont put'num' along with friend, then it does not make numbered list, instead directly gives tuples.
friends = ['Mary','Mickey','Mini','Street']
for friend in enumerate(friends,51):
    print(friend)


# enumerating the enumerate
# This creates a tuple with a number and tuple in it like (0, (51, 'manu'))
friends = ['Mary','Mickey','Mini','Street']
for friend in enumerate(enumerate(friends,51)):
    print(friend)


# more examples: If we give number to second enumerate too, it gives numbering to second enumerate like
# (-100, (51, 'manu'))
# (-99, (52, 'lavi'))
# (-98, (53, 'usha'))
for friend in enumerate(enumerate(friends,51),-100):
    print(friend)


# we can do enumerate with tuples, lists, strings
# with dictionaries and sets, not that much because they are not really sequences


# example with strings
for num, letter in enumerate('python',1):
    print(num,letter)

# Console:
# 1 p
# 2 y
# 3 t
# 4 h
# 5 o
# 6 n
