# project Euler #4 - largest palindrome of two 3 - digit numbers
# a palindrome is a number that is the same backwards and forwards, like 101 or 990099

import time

def is_palindrome(val):
    val = str(val)
    if val == val[::-1]:
        return(True)
    else:
        return(False)
# reversing syntax - reverses the value or flips it--> [::-1]
# print(is_palindrome(1031))

# function can be written as below too
# def is_palindrome(val):
# return str(val) == str(val)[::-1]

# print(is_palindrome(1031))

# brute force approach - multiplying each number from 100 to 999 to all the numbers from 100 to 999(100,999-smallest,highest 3 digit numbers) and check if they are palindromes, and make a list out of palindromes and find the highest of the list.
def palindrome():
    start_time = time.time()
    palindromes_list = []
    debug_list = []
    low_value =100
    high_value = 999
    iterations = 0
    
    for num1 in range(low_value,high_value):
        for num2 in range(low_value,high_value):
            iterations += 1
            # print(num1,num2)
            if is_palindrome(num1*num2) == True:
                palindromes_list.append(num1*num2)
                debug_list.append([num1,num2,(num1*num2)/high_value,low_value])
            if num1 == num2 :
                break  
    print('Degub_List: ', debug_list)  
    print('Palindrome_list: ', palindromes_list)
    print(f'Iterations: {iterations}')
    print('highest_palindrome: ' , max(palindromes_list))
    print(f'Run time: {time.time()-start_time}')
    print('---------------END RUN----------------')

palindrome()


def palindrome2():                                     # comment one of the 2 functions if runtime is more and pages are responsive
    start_time = time.time()
    palindromes_list = []
    debug_list = []
    low_value =100
    high_value = 999
    iterations = 0
    low_num2_val = 900

    for num1 in range(high_value,low_value,-1):        # stepping backward
        if num1 < low_value:
            break
        for num2 in range(high_value,low_num2_val,-1):
            iterations += 1
            # print(num1,num2)
            if is_palindrome(num1*num2) == True:
                palindromes_list.append(num1*num2)
                low_value = max((num1*num2)/high_value, low_value)
                low_num2_value = num2
                debug_list.append([num1,num2,num1*num2])
            if num1 == num2 :
                break
    print('Degub_List: ', debug_list)
    print('Palindrome_list: ', palindromes_list)
    print(f'Iterations: {iterations}')
    print('highest_palindrome: ' , max(palindromes_list))
    print(f'Run time: {time.time()-start_time}')
    print('---------------END RUN----------------')
palindrome2()

