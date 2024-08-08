# List - and methods related to list
# list is not immutable
friends = ['rosy', 'jackson', 'peter', 'smith']
family = ['victor', 'kelly', 'johny', 'mini', 'mickey']
print(friends)
print(family)
print(family[0])                 # print item, index = 0 from the list 'family'
print(family[1])                 # print item, index = 1 from the list 'family'
print(family[-1])                # print last time from the list 'family'
print(family[2],family[3])       # print items,whose index = 2, index =3 from the list 'family'. Index starts from 0 and we count from left to right
print(family[1:3])               # print items, from index = 1 to index = 3 from the list 'family' leaving 3.
print(family[:4])                # print items from index = 0 to index = 4 from the list 'family'
print(family[:])                 # print all the items in the list family
print(len(family))               # print length of the list 'family'
print(family.index('victor'))     # print index of the item vikky from the list 'family'
print(friends.index('rosy'))     # print index of the item usha from the list 'friends'
print(friends.count('peter'))     # print count of the list 'friends'

friends.sort()                   # sort the list in ascending order - sort method changes the list
print(friends)
friends.sort(reverse=True)       # sort the list in descending order
print(friends)
friends.reverse()                # reverse the existing list
print(friends)

cars = [23,25,46,78,94,38]
print(min(cars))
print(cars)
print(cars[2])
print(max(cars))
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars.reverse()
print(cars)

# Modify list
friends.append('john')
print(friends)
family.append('rex')
print(family)
family.insert(1,'paul')
print(family)


# remove the old value and replace it with new value in the list
family[1]='Ramu'
print(family)
family.extend(friends)               # extend the list, or put two lists together
print(family)
family.remove('Ramu')                # delete or remove an item from the list
print(family)
friends.pop()                        # remove the last item in the array
print(friends)
friends.pop(2)
print(friends)
friends.clear()
print(friends)

# delete
del friends                          # to delete the entire list
print(family)
del family[2]                        # to delete a part of the list by index
print(family)

new_friends = family[:]              # copy the list and create a new list - method1
print(new_friends)
new_family = family.copy()           # copy the list and create a new list - method2
print(new_family)
new_group = list(family)             # copy the list and create a new list - method3
print(new_group)


# methods used
# sort() - to sort the list in ascending order
# sort(reverse=True) - to sort the list in descending order
# reverse() - to reverse the order of the list
# min() - gives minimum item of the list
# max() - gives maximum item of the list
# list.index() - gives the index of the item in the list
# list.count() - gives the count of the list


# Exercise - on lists
sales_w1 =  [7,3,42,19,15,35,9]                           # lemonades sold in a week
sales_w2 = [12,4,26,10,7,28]
sales = []
sales_new_day = input('enter sale on new day')            # a new day sales is given as input
sales_w2.append(int(sales_new_day))                       # new day sales is appended to the sale on week2 after converting it to int
print(sales_w2)
sales.extend(sales_w1)
sales.extend(sales_w2)
print(sales)
sale_best_day = max(sales)*1.5
sale_worst_day = min(sales)*1.5
sale_total = sum(sales)
print(f'best day sale: {sale_best_day}')
print(f'worst day sale: {sale_worst_day}')
print(sale_total)
