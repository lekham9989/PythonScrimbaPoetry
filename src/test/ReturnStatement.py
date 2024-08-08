#RETURN STATEMENT:

# If we have multiple values in return statement, returns tuple by default and can return a list and set by specification
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return tax, total_amount, amount                                 # returning values come as a tuple by default

print(value_added_tax(amount=100))

# print(value,type(value))
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return [tax, total_amount, amount]                               # If we put square brackets, then returned value is a list

price = value_added_tax(amount=100)
print(price, type(price))                                            # Console: [25.0, 125.0, 100] <class 'list'>


def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return {tax, total_amount, amount}                               # If we put flower brackets, then returned value is a set

price = value_added_tax(amount=100)
print(price, type(price))                                            # Console:{25.0, 125.0, 100} <class 'set'>


def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return f"{tax}, {total_amount}, {amount}"                        # If we make it a string using 'formatted strings', then returned value is a string

price = value_added_tax(amount=100)
print(price, type(price))                                            # Console: 25.0, 125.0, 100 <class 'str'>

