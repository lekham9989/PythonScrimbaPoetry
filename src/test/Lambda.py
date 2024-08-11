
# LAMBDA FUNCTIONS
# lambdas are anonymous functions that exist in python and that allow you to write single line functions that you can use once and discard them or use them multiples times
def square(x):
    return x*x
print(square(3))


# lambda function returns value
# name = lambda parameter(s): expression
square1 = lambda x: x*x
print(square1(3))


# one line syntax
def square2(x): return x*x
print(square2(3))

# double multiply function - 2 variables x,y
doub_mult = lambda x,y: 2*x*y
print(doub_mult(3,2))

# name and alias function
# regular function


def name_and_alias(name,alias):
    return name.strip().title() + ':' + alias.strip().title()


def name_and_alias1(name,alias): return name.strip().title() + ':' + alias.strip().title()
# single line function
name_and_alias2 = lambda name,alias: name.strip().title() + ':' + alias.strip().title()
# lambda function
print(name_and_alias('john cEASER','hitlor'))
print(name_and_alias1('john cEASER','hitlor'))
print(name_and_alias2('john cEASER','hitlor'))

monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']
# sort the list using lambda function
monty_python.sort(key = lambda name : name.split(' '))
print(monty_python)
monty_python.sort(key = lambda name : name.split(' ')[-1])
print(monty_python)

def sort_names(name):
    return name.split(' ')
monty_python.sort(key = sort_names)
print(monty_python)


# lambda functions
def fun(n):
    return n
print(fun(3))
print(type(fun(3)))

# returning a function in a function using lambda
def fun(n):
    return lambda a:a*n
print(fun(3))

# a*2
doubler = fun(2)
print(doubler(3))

# a*5
quintipler = fun(5)
print(quintipler(5))

# create a price calculator function for walking customers and premium customers using lambda
def price_cal(start,hourly_rate):
    return lambda hours : start + hourly_rate*hours

walkin_cust = price_cal(10,30)
print(walkin_cust(2))
premium_cust = price_cal(1,20)
print(premium_cust(2))


# we can call the function immediately using lamba function
print((lambda a,b,c:a+b+c)(2,3,4))
print((lambda x,y,z:x+y-z)(8,5,2))

# we can give direct values and get the result using lambda
print(price_cal(10,30)(2))

# we can give default values in the lambda function
print((lambda a,b,c=4:a+b+c)(2,3))

# other way is by naming the arguments
print((lambda a,b,c=3:a+b+c)(b=2,a=4))

# without giving specific variables also we can use lambda
# print((lambda *args:sum(args))(2,3,4))
print((lambda *args:sum(args))(2,3,4,5))




def f(x): return x + 5
# f = ...insert equivalent lambda here
print(f(2))

# lambda function
func = lambda x : x+5
print(func(2))

print((lambda x : x+5)(2))

def f(x):
    return lambda y : y+x+5
print(f(2))
f1 = f(2)(3)
print(f1)

# regular function
def strip_spaces(str):
   return ''.join(str.split(' '))
print(strip_spaces('Monty Pythons Flying Circus'))

# write equivalent lambda and insert Lambda here
print((lambda str : ''.join(str.split(' ')))('Monty Pythons Flying Circus'))

# other from of lambda function
strip_spaces1 = lambda str : ''.join(str.split(' '))
print(strip_spaces1('Monty Pythons Flying Circus'))

print('Lambdas Exercise')

def join_list_no_duplicates(list_a,list_b):
   return list(set(list_a + list_b))
list_a = [1,2,3,4]
list_b = [3,4,5,6,7]
print(join_list_no_duplicates(list_a,list_b))

# write lambda below
join_list_no_duplicates1 = lambda list_a,list_b : list(set(list_a + list_b))
print(join_list_no_duplicates1(list_a,list_b))

# Complete the function so it returns a function
def create_quad_func(a,b,c,x):
    return a*x**2 + b*x + c
print(create_quad_func(1,2,3,2))

def create_quad_func1(a,b,c):
    return lambda x : a*x**2 + b*x + c
f = create_quad_func1(1,2,3)
g = create_quad_func1(3,4,6)
print(f(2))
print(g(2))

# write sorting by integer
signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
print(sorted(signups)) # Lexicographic sort
print(sorted(signups, key = lambda id : int(id[3:])))
# print(sort)


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score =  score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]

# Exercise: Sort this by score using lambda!
player_list.sort(key = lambda playyer : playyer.score)
print([player.name for player in player_list])

player_list.sort(key = lambda playyer : playyer.score, reverse = True)
print([player.name for player in player_list])
