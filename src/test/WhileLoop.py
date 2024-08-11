# SYNTAX for while loop
# while condition:
    # code
    # iterator

# What I have to repeat
# What I have to change
# How long it must be repeated

i=0
while i < 5:
    i+=1                                               # i=i+1
    print(f'{i}.{i*"*"}*Loops are great*{i*"*"}')

# Console:
# 1.**Loops are great**
# 2.***Loops are great***
# 3.****Loops are great****
# 4.*****Loops are great*****
# 5.******Loops are great******


# Example for While loop to create a guess game with 3 guesses
# simple way
i=0
while  i < 3:
    guess = int(input('Guess a number 1-20:'))
    if guess == 12:
        print(f'You Win! You guessed the correct number {guess}.')
        break
    else:
        print(f'No, not {guess}')
    i=i+1
if guess != 12:
    print(f'Sorry you lost, 12 is correct guess')


    # in detail

num = 12
guess_number=0
guess_limit =3
while  guess_number < guess_limit:
    guess = int(input('Guess a number 1-20:'))
    if guess == num:
        print(f'You Win! You guessed the correct number {num}.')
        break
    else:
        print(f'No, its not {guess}')
    guess_number=guess_number+1

if guess != num:
    print(f'Sorry! Correct guess was {num}')


num = 25
guess_limit =5
guess_number=1
guess = int(input('Guess a number 1-100:'))
while  guess_number < guess_limit:
    if guess != num:
        guess_number+=1
        if guess > num:
            guess = int(input(f'{guess} is high, Guess a number 1-100 again:'))
        else:
            guess = int(input(f'{guess} is low, Guess a number 1-100 again:'))
    else:
        print(f'You Win! You guessed the correct number {num}.')
        break
if guess != num:
    print(f'Sorry! Correct guess was {num}')
