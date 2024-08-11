msg = 'Welcome to Python 101: Strings'
print('Python' in msg)   # boolean - true or false
print('Strings' in msg)
print('Strings' not in msg)

message = 'Hello! How are you doing your Automation on Python'

print('Automation' in message)                       # meaning - Is Automation in message - Ans true or false
print('Python' in message)
print('Hello' not in message)                        # meaning - Is Hello not in message - Ans true or false
print('Morning' not in message)



# Boolean Properties
# Boolean values of empty objects and zero's evaluates to False and rest evaluates to True.
print(bool('Parrot'))                               # Boolean value of 'String' - True
print(bool(' '))                                    # Boolean value of Space string is True
print(bool(''))                                     # Boolean value of empty string is False
print(bool(0))                                      # Boolean value of 0 is False
print(bool(1))                                      # Boolean value of any number is True
print(bool(42))                                     # True
print(bool([]))                                     # False
print(bool([2,3]))                                  # True

# Boolean values can be converted to 0 and 1

# trivial evaluates to 0 and non trivial evaluates to 1
print(int(True))                                    # Make an int out of boolean - evaluates to '1'
print(int(False))                                   # Make an int out of false its - '0'
print(42 + True)                                    # we get 43, bcs python adds 0 to 43, Python does that conversion automatically