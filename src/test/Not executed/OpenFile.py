# open file, close file, read file

my_file = open('greeting.txt', 'r')                                 # to open the file
print(my_file.read(50))                                             # to read the data in the file
print(my_file.readline())                                           # to read line by line gives first line -repeat the code
print(my_file.readline())                                           # to get read the second line

line_by_line = my_file.readlines()                                  # read data line by line
line_by_lines = my_file.read().splitlines()                         # read data line by line
print(line_by_lines)
print(line_by_line)

my_file.close()                                                     # to close the file


with open('friends.csv', 'r') as f:                              # open the file, given it a name as f
    print(f.read())                                              # read the data in the file f
    print(f.readline())                                          # reads first line
    print(f.readline())                                          # reads second line
    print(f.readlines())                                         # reads lines correctly
    friends = f.read().splitlines()                              # reads the lines the best way by breaking
    print(friends)
    for friend in friends:
        friend = friend.split(',')
        name = friend[0]
        year = int(friend[1].strip())
        print(f'In 20 years, {name} will become {2024-year} years old')



with open('movies.txt', 'r') as f:
    # for line in f works in python not in scrimba
    for line in f.readlines():
        print(line)
