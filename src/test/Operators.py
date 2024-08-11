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
print(a == b)                               # a is equal to b
print(a is b)                               # are a and b occupying the same memory space? | Are a and b are identical objects?
print(id(a) == id(b))
print(id(a),id(b))

# When we allocate identical list to 2 variables
a =[23,15,8]
b =[23,15,8]                                # allocating a LIST IDENTICAL to b
print(a == b)                               # Then, a is equal to b? (true)
print(a is b)                               # But a and b are not occupying the same memory space | Is a identical to b? (False)
print(id(a) == id(b))                       # False as id(a) is 2, id(b) is 3
print(id(a),id(b))                          # 2,3


# Examples
a=7
b=3
print('a == b is', a == b)
print('a != b is', a != b)
print('a > b is', a > b)
print('a < b is', a < b)
print('a >= b is', a >= b)
print('a <= b is', a <= b)
print('o in John is ','o' in 'John')                        # membership
print('o in John is ','o' not in 'John')                    # non membership
print('John is John ','John' is 'John')                     # identity
print('John is not John is ','John' is not 'John')          # negative identity

# Console:
# ›a == b is False
# ›a != b is True
# ›a > b is True
# ›a < b is False
# ›a <= b is False
# ›o in John is True
# ›o in John is False
# ›John is John True
# ›John is not John is False