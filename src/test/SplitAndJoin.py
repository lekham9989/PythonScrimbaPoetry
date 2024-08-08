# Split and join

# string - when we split a string, it splits into a list.
# csv - when we split a csv it splits into a list.
# csv.split() - when we split a csv without anything, it splits into a list of single item
# csv.split(',') - when we split a csv with something like comma (,), it splits into a list of many items as it has.
# list - list object has no attribute split - we cannot use split on a list


msg = 'Welcome to Python 101: split and join'               # string
csv = 'john,rosy,peter'                                     # csv
friends_list = ['mini','mickey','snoopy']                   # list

# print(list(msg))
print(msg.split(), type(msg.split()))
print(msg.split(' '), type(msg.split(' ')))
print(csv.split(), type(csv.split()), len(csv.split()))
print(csv.split(','), len(csv.split(',')))

# print(str(friends_list), type(str(friends_list)))
print(''.join(csv.split(',')))
print('-'.join(csv.split(',')))
print('-'.join(friends_list))
print('-'.join(msg.split(' ')))
print('-'.join(friends_list + friends_list + friends_list))

print(''.join(msg.split()))
print(msg.replace(' ', ''))

# Exercise:

# csv example
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = (csv.replace(':', ',').replace(';', ',')).split(',')
print(friends_list)

friends_list = ','.join(','.join(csv.split(';')).split(':')).split(',')
print(friends_list)

# steps to understand above split and join
print(csv.split())
print(csv.split(';'))
print(','.join(csv.split(';')))
print(','.join(csv.split(';')).split(':'))
print(','.join(','.join(csv.split(';')).split(':')))
print(','.join(','.join(csv.split(';')).split(':')).split(','))