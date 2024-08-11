# generating Random strings-------------------------------------------------------------------------
# People use these so much that we have constants for these values and to get those constants we have to import 'string' module.
import random, string
smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

# inorder to access these constants we have to create a new one
letters_numbers = string.ascii_letters + string.digits
print(letters_numbers)

# ascii_letters holds the lowercase and uppercase letters. digits holds the digits
# If I want only lowercase letters, I say ascii.lowercase and if I need uppercase, I say ascii.uppercase
print(string.ascii_lowercase)
print(string.ascii_uppercase)

# create a random string with (upper & lower case)letters and numbers: count 7
letters_numbers1 = string.ascii_letters + string.digits
print(letters_numbers1)
word = ''
word1 = ''
for i in range(7):
    word = word + random.choice(letters_numbers1)
    word1 += random.choice(letters_numbers1)                                        # short form of above

print(word)
print(word1)

# to get no duplicates in the string, we can use sample function
word = ''.join(random.sample(letters_numbers1,7))
print(word)

# to bypass the for loop we can use choices() function, but this does not work in scrimba, it works in other python platforms, but it has dublicates
word = random.choices(letters_numbers, k=7)
print(word)
