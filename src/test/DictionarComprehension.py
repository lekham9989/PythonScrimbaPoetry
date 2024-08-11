# Dictionary comprehensions
movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
          "Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]
year =[1971,1975,1979,1982,1983,2014]
names = ['John','Eric','Michael','Graham','Terry','TerryG']

combo = zip(movies,year)
print(list(combo))

print(list(zip(movies,year)))

# give me a dict('movies': year) for each movies, year in zip(movies, year)
new_dict = dict()
for movie,yr in zip(movies,year):
    new_dict[movie] = yr
print(new_dict)

# comprehension
# new_dict1 = {movie:yr for movie,yr in zip(movies,year) if yr < 1983 and 'Monty Python' in movie }
new_dict1 = {movie:yr for movie,yr in zip(movies,year) if yr < 1983 and movie.startswith('Monty Python') }
print(new_dict1)

# list the prints movies with who likes it
n1 = [(name,movie,yr) for (name,movie,yr) in zip(names,movies,year)]
print(n1)

n2 = [[name + 's favourite movie is ' + movie + ' from the year ' + str(yr)] for (name,movie,yr) in zip(names,movies,year)]
print(n2)