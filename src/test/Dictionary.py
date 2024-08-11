# DICTIONARY
movie = {
    'title' : 'life of pi',
    'year' : 2000,
    'cast' : ['manu', 'usha', 'swetha', 'lavi', 'abi']
}

print(movie)                                                 # To print the complete dictionary
print(movie['title'])                                        # To print the value of a particular key in dictionary
print(movie['year'])
print(movie['cast'])
print(movie.get('budget'))                                   # use get method to get rid of error, for key that does not exist in dict
print(movie.get('title'))
print(movie.get('budget', 'not found'))                      # we can specify what we get, by a default value for a key

# UPDATE A DICTIONARY
movie['title'] = 'Bahubali'                                  # to update the existing key value of a dictionary
print(movie['title'])
print(movie)

movie['year'] = 2012
movie['budget'] = 200000
print(movie.get('year'))                                     # to add a new key value to the dictionary
print(movie.get('budget'))
print(movie)                                                 # to retrieve the value of key in dict

# update command - updating the whole dictionary at the same time
movie.update({'title' : 'bahubali 2', 'year' : 2019, 'cast' : ['manu', 'usha', 'swetha', 'lavi', 'abi']})
print(movie)


movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}
# pop command - pops out or deletes the key value from the dictionary
year = movie.pop('year')
print(year)
# length of the dictionary - entries available
print(len(movie))

# items() method, print all the entries in the dictionary- as tuples
# keys() methods, print all the keys
# values() method, print all the values
print(movie.items())
print(movie.keys())
print(movie.values())

# to get a sequence of keys in dictionary - use for loop
for key in movie:
    print(key)

# to get sequence of keys,values both in dictionary -using for loop
for key,value in movie.items():
    print(key,value)


    python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

# the keys in a dictionary must not repeat
# membership test
print('Eric' in python)
if 'Abi' not in python:
    print('He is not here')

# combining 2 or more dictionaries together
# method1 - update
people = {}
people1 = {}
people2 = {}
people.update(python)
people.update(holy_grail)
people.update(life_of_brian)
print(people)
# sorting it to get same way as other dicts
print(sorted(people.items()))

# method2 - comprehension
for groups in (python,holy_grail,life_of_brian) : people1.update(groups)
print(people1)
# sorting it to get same way as other dicts
print(sorted(people1.items()))

# method3 - unpacking 3.5 or later
people2 = {**python,**holy_grail,**life_of_brian}
print(people2)
# sorting it to get same way as other dicts
print(sorted(people2.items()))

# add the values in the dictionary
print('sum of the values:', sum(people.values()))


# EXERCISE FOR DICTIONARY - USING FOR LOOP WITH DICTIONARIES, UPDATE METHOD(UPDATING KEY VALUE PAIR IN AN EMPTY DICTIONARY)

freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

cart = {}

for shop in (freelancers,antiques,pet_shop):
    item_name = input(f'Welcome to {shop["name"]}! what do you want to buy: {shop}')
    cart.update({item_name : shop.pop(item_name)})
print(f'items purchased are {", ".join(list(cart.keys()))}')

