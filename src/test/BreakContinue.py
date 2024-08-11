# break statement
friends = ['John','Eric','Peter']
for friend in friends:
    if friend == 'Eric':
        print('found ' + friend)
        break                                   # breaks out of the for loop
    print(friend)

print('for loop is done')

# Console:
# John
# found Eric
# for loop is done

# Console:
# John
# found Eric
# Peter
# for loop is done

# no break or no continue statement
friends = ['John','Eric','Peter']
for friend in friends:
    if friend == 'Eric':
        print('found ' + friend)
# goes to the next statement if there is no break or no continue statement
    print(friend)

print('for loop is done')

# Console:
# John
# found Eric
# Eric
# Peter
# for loop is done