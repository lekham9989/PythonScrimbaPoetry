# INHERITANCE
# There are various characters in a game. We are creating few characters.
class Person:
    def move(self):
        print('Moves 4 paces')

    def rest(self):
        print('Gains 4 health points')


class Doctor(Person):                                       # Doctor class is got inheritance from Person class

   def heal(self):
        print('Gains 6 health points')

class Fighter(Person):
    def move(self):
        print('Moves 6 paces')


class Wizard(Doctor,Fighter):                                # Wizard class got inheritance from 2 classes.
    def cast_spell(self):
        print('Turns invisible')
    def heal(self):
        print('Gains 10 heath points')


Character1 = Person()
Character2 = Person()
Character1.move()
Person.move(Character1)                                      # call the function from Person class and give self as Character1

Character3 = Doctor()
Character3.move()
Character3.heal()

Character4 = Fighter()
Character4.move()                                            # when there is same function in inheritance class and original class, it calls original class function

Character5 = Wizard()
Character5.move()                                            # when there is same function in inheritance class and inheritance class's inheritance class, it calls function from inheritance class. nearby function
Character5.heal()
