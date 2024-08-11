# CONDITIONALS (if, elif, else)

# IF STATEMENT with 1 condition
is_raining = False
print('Good Morning!')
if is_raining:
    print('Bring Umbrella')
else:
    print('Umbrella is Optional')

# IF STATEMENT with 2 conditions
# 'OR' operator - any one condition must be true for the execution of if statement
is_raining = False                                              # When 2 conditions are false
is_cold = False
print('Good Morning!')
if is_raining or is_cold:
    print('Bring Umbrella or Jacket or both')
else:
    print('Umbrella is Optional')

is_raining = False                                          # When any one condition is true
is_cold = True
print('Good Morning!')
if is_raining or is_cold:
    print('Bring Umbrella or Jacket or both')
else:
    print('Umbrella is Optional')

# 'AND' Operator: 2 conditions must be true for the execution of if statement
is_raining = False                                           # When any one condition is true
is_cold = True
print('Good Morning!')
if is_raining and is_cold:
    print('Bring Umbrella and Jacket')
else:
    print('Umbrella is Optional')


is_raining = True                                             # When two conditions are true
is_cold = True
print('Good Morning!')
if is_raining and is_cold:
    print('Bring Umbrella and Jacket')
else:
    print('Umbrella is Optional')


# ELIF statement
is_raining = False
is_cold = True
print('Good Morning!')
if is_raining and is_cold:                                   # when it is raining & cold
    print('Bring Umbrella and Jacket')
elif is_raining and not(is_cold):                            # elif statement, when it is raining but not cold
    print('Bring Umbrella')
elif not(is_raining) and is_cold:                            # elif statement, when it is not raining but cold
    print('Bring Jacket')
else:
    print('Umbrella is Optional')                            # when it is not raining and not cold



amount = 51
if amount <= 50:
    print("Purchase approved")
else:
    print("Please enter your pin!")

# CALCULATOR
mode = input('Enter the math operator (+,-,*,/) or f for celsius to faranheit conversion:')
num1 = float(input('Enter the first number:'))
if mode == 'f':
    print(f'{num1} Celsius is equivalent to {((num1*9)/5)+5} Farenheit')
else:
    num2 = float(input('Enter the second number:'))
    if mode == '+':
        print(f'Answer is {num1 + num2}')
    elif mode == '-':
        print(f'Answer is {num1 - num2}')
    elif mode == '*':
        print(f'Answer is {num1 * num2}')
    elif mode == '/':
        print(f'Answer is {num1 / num2}')
    else:
        print ('Input Error')


# Example for if conditions using operators and months

def num_days(month):

    if month in {'apr','jun', 'sep','nov'}:
        print('number of days in',month,'is',30)
    elif month == 'feb':
        print('number of days in',month,'is',28)
    else :
        print('number of days in',month,'is',31)


num_days('mar')



