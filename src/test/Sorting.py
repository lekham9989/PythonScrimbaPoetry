# SORTING : Making the list ascending to descending or vice versa or changing to any order
# lists : mutable - can be changed - that's why they have sorting method
# tuples : immutable - cannot be changed -
# strings : immutable - cannot be changed - So, both tuples & strings naturally don't have a sorting function. If we want to change them , we have to turn them into something new.
# sort() and #reverse() functions will sort/reverse the list and original list changes. But sort() & reverse() functions does not print the list on console, instead console shows 'none'
# sorted() function will sort and print the list in the console, but original list does not change
# when a sorted() function is applied for a tuple, returns a sorted LIST
# when a sorted() function is applied for a string, returns a sorted LIST

# sort() & reverse() functions
list = ['manu','lavi','swetha','usha','abi']
print(list,'original')                                              # original list
print(list.sort())                                                  # sort function does not print & print statement gives none
print(list, 'new')
print(list.reverse())                                               # reverse function does not print & print statement gives none
print(list, 'new reverse')

# sorted() function
print(sorted(list))                                                 # sorted() function prints the sorted list
print(list, 'new1')                                                 # sorted() gave a sorted list, but it did not change the original list'''
numbers = [1,6,2,7,3,4]
my_tuple = ('d','c','e','a','b')
my_dict = {'car':4,'dog':2,'add':3,'bee':1}
my_string = 'python'
print(numbers, 'original')
print(numbers.sort())
print(numbers, 'new')
print(numbers.reverse())
print(numbers, 'new1')
print(sorted(numbers))                                      # sorted() will sort and print the list, but original list does not change
print(numbers, 'new1')

number_new = sorted(numbers)
print(number_new)
print(my_tuple,'original')
print(sorted(my_tuple))                                     # when a sorted() function is applied for a tuple, returns a sorted LIST
print(my_tuple, 'new')
print(my_string, 'original')
print(sorted(my_string))                                    # when a sorted() function is applied for a string, returns a sorted LIST
print(my_string,'new')

# sorted() on dictionary

# my_dict = {'car':4,'dog':2,'add':3,'bee':1}
print(my_dict, 'original')
print(sorted(my_dict))                                      # when we apply sorted()function to a dictionary, it returns a sorted list with keys.
print(sorted(my_dict.items()))                              # when we apply sorted().items, it returns a sorted list with tuples.
print(sorted(my_dict.values()))                             # when we apply sorted().values to a dictionary, returns a list with values from dict.
print(sorted(my_dict.keys()))                               # when we apply sorted().keys to a dictionary, returns a list with keys from dict.
print(my_dict, 'new')
print(sorted(my_dict.items(),reverse=True))                # returns a list of tuples which are sorted in reverse order using keys
print(sorted(my_dict.values(),reverse=True))               # returns a list of values in reverse order from dictionary
print(sorted(my_dict.keys(), reverse=True))                # returns a list of keys in reverse order from dictionary


# reversed() : #just like sorted() function, we also have reversed() function.
my_list = [1,5,3,7,2]
print(reversed(my_list))                                        # returns 'reversed object'
# print(list(reversed(my_list)))                                   # to see what a reversed object has, we have to turn it into a list

# Another way of reversing a list : using slicing syntax (::-1)
print(my_list[::-1])                                             # returns the same as reversed function()



# To make a reverse list, we use list(reversed()) function - no sorting is done here
# To make a reverse list, slicing syntax [::-1] also used.

# List with negative values
my_list = [1,5,-3,7,-2]
my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
print(sorted(my_list))                                           # when we sorted() a list with -ve values, gets sorted in integers order
print(sorted(my_list, key = abs))                                # when we want to get sorted with absolute values, then use abs, returns [1, -2, -3, 5, 7]
print(sorted(my_llist))
print(sorted(my_llist, key = lambda item: item[0]))
print(sorted(my_llist, key = lambda item: item[1]))
print(sorted(my_llist, key = lambda item: item[2]))



# reversed() : #just like sorted() function, we also have reversed() function.
my_list = [1,5,3,7,2]
print(reversed(my_list))                                          # returns 'reversed object'
# print(list(reversed(my_list)))                                    # to see what a reversed object has, we have to turn it into a list

# Another way of reversing a list : using slicing syntax (::-1)
print(my_list[::-1])                                              # returns the same as reversed function()
