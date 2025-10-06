# This file is for OOP practising

# Assignment 1
class Game:
    def __init__(self, name, developer, year, price):
        self.name = name
        self.developer = developer
        self.year = year
        self.price = price

    def price_in_pounds(self):
        return str(float(self.price * 50)) + ' Egyptian Pounds'

game_one = Game('Ys', 'Falcom', 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is \"{game_one.price_in_pounds()}\", ", end="")

# O/P
# Game Name Is "Ys", Develper Is "Falcom", Release Date Is 2010, Price In Egype Is 2500.0 Egyptian Pounds


# Assignment 2
class User:
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

    def full_details(self):
        return f"Hello {('Mr' if self.gender == 'Male' else 'Mrs')} {self.fname} {self.lname[0]}. [{str(40 - self.age).zfill(3)}] Years To Reach 40"

user_one = User('Kareem', 'Ashraf', 20, 'Male')
user_two = User('Zeinab', 'Eid', 18, 'Female')
print(user_one.full_details())
print(user_two.full_details())

# O/P
# Hello Mr Kareem A. [020] Years To Reach 40
# Hello Mrs Zeinab E. [022] Years To Reach 40

# Assignment 3
class Message:
    @classmethod
    def print_message(cls):
        return 'Hello From Class Message'

print(Message.print_message())

# O/P
# Hello From Class Message


# Assignment 4
class Games:
    def __init__(self, games):
        self.games = games

    def show_games(self):
        if self.games == None: print("I Have No Games")
        elif type(self.games) == str: print(f"I Have One Game Called \"{self.games}\"")
        elif type(self.games) == int: print(f"I Have {self.games} Games")
        else:
            msg = "I Have Many Games:\n"
            for game in self.games:
                msg += f"-- {game}\n"
            print(msg)

my_game = Games("Shadow Of Mordor")
my_games_names = Games(['Ys II', 'Ys Oath In Felghana', 'YS Origin'])
my_games_count = Games(80)

my_game.show_games()
# O/P
# I Have One Game Called "Shadow Of Mordor"

my_games_names.show_games()
# O/P
# I Have Many Games:
# -- Ys II
# -- Ys Oath In Felghana
# -- YS Origin

my_games_count.show_games()
# O/P
# I Have 80 Games


# Assignment 5
class Members:
    def __init__(self, n, p):
        self.name = n
        self.permission = p

    def show_info(self):
        return f"Your Name Is {self.name} And You Are {self.permission}"
    
class Admins(Members):
    def __init__(self, n, p):
        super().__init__(n, p)

class Moderator(Members):
    def __init__(self, n, p):
        super().__init__(n, p)

member_one = Admins("Kareem", "Admin")
member_two = Moderator("Ahmed", "Moderator")

print(member_one.show_info())
# O/P
# Your Name Is Kareem And You Are Admin

print(member_two.show_info())
# O/P
# Your Name Is Ahmed And You Are Moderator



# Assignment 6
class A:
    def __init__(self, one):
        self.one = one

class B:
    def __init__(self, two):
        self.two = two

class C:
    def __init__(self, three):
        self.three = three

class Name(A, B, C):
    def __init__(self, one, two, three):
        A.__init__(self, one)
        B.__init__(self, two)
        C.__init__(self, three)

    def show_name(self):
        full_name = f"{self.one}{self.two}{self.three}"
        return f"The Name Is {full_name}"
    
the_name = Name("Ka", 're', 'em')
print(the_name.show_name())
# O/P
# The Name Is Kareem
