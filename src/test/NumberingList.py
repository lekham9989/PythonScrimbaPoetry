# To get the list of friends with numbering
friends = ['John','Peter','Rocky','Superman']
i=0
for friend in friends:
    print(i+1,'.',friend)
    i=i+1

# Console: this has spaces
# 1 . John
# 2 . Peter
# 3 . Rocky
# 4 . Superman


friends = ['Rocy','Rice','Sweet','Mickey']
i=0
for friend in friends:
    print(f'{i+1}.{friend}')
    i=i+1

# Console:
# 1.Rocy
# 2.Rice
# 3.Sweet
# 4.Mickey

# In python, this is the way we write to get a numbered list from any group.
friends = ['manu','lavi','usha','swetha']
for num, friend in enumerate(friends,1):
    print(num,friend)