# MATH TUTOR APPLICATION
from random import randrange as r
no_of_questions = int(input('How many questions do you want?: '))
score = 0
for q in range(no_of_questions):
    num1,num2 = r(1,11),r(1,11)
    ans = num1 * num2
    u_ans = int(input(f'Q1--> {num1} * {num2} = ?:'))
    if u_ans == ans:
        score = score + 1
number_of_correct_answers = score
correct_answers = no_of_questions
fraction = number_of_correct_answers / correct_answers
per_correct = fraction*100
print(f'Thankyou for playing Math Tutor! Your score is {score} out of {no_of_questions}. And you got {number_of_correct_answers/correct_answers * 100}')



# MATH TUTOR APPLICATION
from random import randrange as r
from time import time as t
def math_tutor():
    no_of_questions = int(input('How many questions do you want?: '))
    max_num = int(input('Highest number used in practice:'))
    score = 0
    answer_list = []
    start = t()
    for q in range(no_of_questions):
        num1,num2 = r(1,max_num+1),r(1,max_num+1)
        ans = num1 * num2
        u_ans = int(input(f'Q1--> {num1} * {num2} = ?:'))
        answer_list.append(f'{num1} X {num2} = {ans} you:{u_ans}')
        if u_ans == ans:
            score = score + 1
        end = t()
    number_of_correct_answers = score
    correct_answers = no_of_questions
    fraction = number_of_correct_answers / correct_answers
    per_correct = fraction*100
    print(f'Thankyou for playing Math Tutor! Your score is {score} out of {no_of_questions}. And you got {round(number_of_correct_answers/correct_answers * 100)}% and you took {round(end-start,1)} seconds in total and {round((end-start)/no_of_questions,1)} seconds per question.')
    for a in answer_list:
        print(a)
math_tutor()
