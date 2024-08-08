# Sets - Exercise

# 1. Check if ‘Eric’ and ‘John’ exist in friends
# 2. combine or add the two sets
# 3. Find names that are in both sets
# 4. find names that are only in friends
# 5. Show only the names who only appear in one of the lists
# 6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

print('Eric' and 'John' in friends)
print(friends.union(my_friends))                    # for joining 2 sets, we use union
print(friends | my_friends)                         # for union, we also use |
print(friends.intersection(my_friends))             # for common items in set, we use intersection
print(friends.difference(my_friends))               # for items only in one set, we use difference
print(friends - my_friends)                         # for difference, we can use - also
print(friends.symmetric_difference(my_friends))     # for items in any one set only, we use symmetric difference
print(friends ^ my_friends)                         # for symmetric difference, other way use is ^
print(set(cars))                                    # set does not have any duplicates
print(list(set(cars)))                              # new cars list is created without duplicates