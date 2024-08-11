# Betting Marble draw game
import random
gold = 1000
# bag = ('Green','Green','Green','Green','Green','Green','Green','Red','Red','Red')
bag = ('Green','Green','Green','Green','Green','Green','Black','Red','Red','White')
print('Welcome to the game')
no_of_draws = random.randint(1,10)
wins = 0
# loses = 0
win_or_lose = ''
marble = 'none'
for i in range(no_of_draws):
    bet = int(input(f'<--{win_or_lose}--> Welcome! gold : {gold}, last draw : {marble}, draws left : {no_of_draws-i} enter how much you want to bet(1-500):'))
    marble = random.choice(bag)
    if marble == 'Green':
        wins = wins + 1
        win_or_lose = 'You won the bet'
        gold = gold + bet
    elif marble == 'Black':
        gold = gold + (10*bet)
    elif marble == 'White':
        gold = gold - (5*bet)
    elif marble == 'Green' or 'Black':
        wins = wins + 1
    else:
        gold = gold - bet
        win_or_lose = 'You lost the bet'
    if gold <= 500:
        print('Game is over')
    print(f'gold : {gold}, last marble : {marble}, bet : {bet}')
print(f'you did {no_of_draws} draws and won {wins} draws and you are left with {gold} gold ')
