# Data types
# list []
# set  {}   - has no order - blazingly fast unordered Lists
# tuple ()  - is immutable -  list that can't be changed
# dictionary
# string '' - is immutable
# csv

# csv example
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = (csv.replace(':', ',').replace(';', ',')).split(',')
print(friends_list)

friends_list = ','.join(','.join(csv.split(';')).split(':')).split(',')
print(friends_list)

# list example
family = ['Rex', 'Rovan','Rexy']
print(family)

# set - example
vehicles = {'car','bus','train','scooter'}
print(vehicles)
# 2 sets - union, intersection, difference
friends_set = {'Eric', 'John', 'Michael', 'Terry', 'Graham', 'TerryG', 'Brian'}
friend = {'Michael', 'Terry', 'Graham', 'TerryG'}
# union - all items in set with no duplicates
print(friend.union(friends_set))
# intersection of sets - in common
print(friends_set.intersection(friend))
# difference - must be in set1 but not in set2
print(friends_set.difference(friend))
print(friend.difference(friends_set))

# tuple - example
friends = ('Eric', 'John', 'Michael', 'Terry', 'Graham', 'TerryG', 'Brian')
print(friends[2:5])

# how to declare
# empty List
empty_list = []
empty_list1 = list()

# empty Tuple
empty_tuple = ()
empty_tuple1 = tuple()

# empty Set
empty_set = {}  # this is wrong, this is a dictionary
empty_set1 = set()

# example1
fruits = []  # a set named fruits
flowers = ()  # a tuple named flowers
trees = {}  # not a set named trees  - wrong way to create set, it creates dictionary
cars = set()  # a set named cars
print(fruits, flowers, trees, type(fruits), type(flowers), type(trees), type(cars))

# example2
fruit = list()
flower = tuple()
tree = set()
print(fruit, flower, tree, type(fruit), type(flower), type(tree))
