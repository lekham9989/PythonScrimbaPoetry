# iterables - zip command - combining 2 or more iterables like list,tuple
nums = [1,2,3,4]
numbers = '1234'
letters = ['a','b','c','d']
names =['John','Eric','Michael','Graham','Joe']

combo = list(zip(nums,letters))
print(combo)

combo1 = dict(zip(numbers,letters))
print(combo1)

# unzipping
combo3 = list(zip(numbers,letters,names))
print(combo3)
num,let,nam = zip(*combo3)
print(num,let,nam)

# ex:
keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'
keys = keys.split()
values = values.split()
en_sw_dict = dict(zip(keys,values))                                                         # zip
print(en_sw_dict)
# other way of making the dictionary
new_dict = {key:value for key,value in zip(keys,values)}                                    # zip
print(new_dict)

# unzip by using keys and values
en,sw = list(new_dict.keys()),list(new_dict.values())
print(en,sw)

en,sv = zip(*new_dict.items())
print(en,sv)