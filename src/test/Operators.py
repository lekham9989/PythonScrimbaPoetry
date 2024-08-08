# COMPARISONS AND BOOLEANS

# OPERATORS(=,>,<)
a = 2
b = 3
# Booleans
print(a == b)           # Is a equal to b? Ans is boolean - ture or false
print(a != b)           # Is a not equal to b?
print(a > b)            # Is a greater than b?
print(a < b)            # Is a less than b?
print(a >= b)           # Is a greater tha or equal to b?
print(a <= b)           # Is a less than or equal to b?

# CHECK letter exist in a string
print('o' in 'John')                # Does the letter 'o' appears in String 'John'?
print('o' not in 'John')            # Is letter 'o' not in John?


# Identity - check if they are identical

a =[23,15,8]
b = a
print(a == b) # a is equal to b
print(a is b) # are a and b occupying the same memory space? | Are a and b are identical objects?
print (id(a) == id(b))
print (id(a),id(b))
