# CLASSES AND OBJECTS
# class - representation of an abstract concept like blueprint
# class - is like a customised data type
# when you make something out of that class, you are creating object
# ex: concept of making a movie is class and movie 'Bahubali' is made using concept, which is an object of that class.
# when we create classes, they have variables, which we call attributes and functions inside which we call methods


# Classes are blueprints
# Objects are the actual things you built
# variables => attributes
# functions => methods

# when we name a class, we use capital letter and camel casing.
# to create a class, use keyword class followed by classname.

# creating a class
class Movie:
    # class-keyword  ClassName-camelcase
    # initiating an object
    def __init__(self,title,year,imdb_score,have_seen):
        # def-keyword  __init keyword__(self-Keyword, classAttributes or variables)
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen

        # creating a print function in movie class
    def nice_print(self):
        print('Title of the Movie: ', self.title)
        print('Year of the Movie: ', self.year)
        print('Imdb Score of the Movie: ', self.imdb_score)
        print('Have you seen the Movie:', self.have_seen)
# class attributes are created and defined using a function init, object is initiated with the __init__ function
film_1 = Movie('Bahubali',2012,9.5,True)
film_2 = Movie('Bahubali_2',2015,10,True)

print(film_1.title, film_1.imdb_score)
print(film_2.title, film_2.have_seen)
film_1.nice_print()
Movie.nice_print(film_1)

# create a data base of objects - films is a database
films = [film_1,film_2]
print(films[0].title, films[1].title)
films[0].nice_print()