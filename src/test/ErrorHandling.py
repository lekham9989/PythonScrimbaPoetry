# ERROR HANDLING IN PYTHON
# try:
# code you want to run
# except:
# executed if error occurs
# else:
# executed if no error
# finally:
# always executed
try:
    num=int(input('Enter a number: 1-30'))
    num1= 30/num
    if num > 30:
        raise ValueError(num)
# err will specify what err we are getting
except ZeroDivisionError as err:   # ZeroDivisionError keyword used when 0 is entered to divide
    print(err,'you cannot divide by zero')
except ValueError as err: # ValueError keyword when bad value is given like string for arithmetic ope
    print(num, err, 'Bad value, you cannot enter value greater than 30')
except:
    print('Invalid input')
else:
    print("30 divided by",num, "is: ", 30/num)
finally:
    print("**Thank you for playing!**")

# Console:
# invalid literal for int() with base 10: 'df' Bad value -for string input
# division by zero you cannot divide by zero - for 'zero' input
