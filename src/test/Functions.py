# functions
# to define a function we use keyword 'def' followed by function name():
def greeting():
    print('hello friend!')


# to call the function write function name()
greeting()


# parameters in functions
# define function passing one parameter name
def greetings(name):
    print('hello ' + name + '!')


greetings('Brian')


# define function passing two parameters name, age
def greet(name, age):
    print('hello ' + name + '. You are ' + age + '!')
    # more convenient way for concatenation is - formating strings using f - gives same result as above
    print(f'hello {name}. You are {age}!')


greet('Brian', '10')


# Default value
# when we set a default value for one of the parameters in the function, if we don't send a value for parameter, it takes the default value.
def greetings(name, age='20'):
    print(f'Hello {name}. You are {age} now!')


greetings('Brain', '30')  # when we pass the age, it takes the value
greetings('John')  # when we don't pass the age, it takes the default value in the function.


# pass the name from an input box
def greetings1(name, age='20'):
    print('hello ' + name + '. You are ' + age + '!')
    print(f'Hellooo {name}. You are {age} now!')


name = input('Enter the name:')
greetings1(name, '30')
greetings1('John')


def game():
    print('Automation')


game()


# When we pass age as an integer

def greetin(name, age=20):
    print('hello ' + name + '. You are ' + str(age) + '!')  # we need int to str conversion for concatenation
    print(f'Hello {name}. You are {age} now!')  # here no need of str conversion as we use formatted strings


name = input('Enter the name:')
greetin(name, 30)


def greeting(name, age=28, color='red'):
    print('Hello ' + name.title() + ',you will be ' + str(age + 1) + ' years old next birthday!')
    print(f'Hello {name.title()}, you are {age}!')
    print(f'We here you like the color {color}.')


name = input('Enter your name: ')
age = input('Enter your age: ')
color = input('Enter the color:')
greeting(name, 32)


# NAMED NOTATIONS - naming the arguments along with value is named notation
def greeting5(name, age=28, color="red"):
    # Greets user with “name” from “input box” and “age”, if unavailable, default age is used
    print(f"Hello {name.capitalize()}, you will be {age + 1} next birthday!")
    print(f"We hear you like the color {color.lower()}!")


# Named Notations
greeting5('brain', 30, 'pink')
greeting5(age=30, name='heart', color='pink')
greeting5('Rex',20,'brown')

