# Some Small Applications on User Defined Functions in Python

# Application_1
# prime Number Generator
print('-' * 10, 'prime Number Generator', '-' * 10)
def is_prime(num):
    for i in range(2, num): 
        if num%i == 0: return False
    return True
def generate_primes(limit):
    for num in range(2, limit+1):
        if is_prime(num): print(num)
generate_primes(int(input("Enter The Limit: ").strip()))
# print(is_prime(13))
print('*' * 70)
####################################################################################################

# Application_2
# Password Strength Validator
print('-' * 10, 'Password Strength Validator', '-' * 10)
# Password Limits
# - At least 8 characters long
# - At least one uppercase letter
# - At least one lowercase letter
# - At least one digit
# - At least one special character (e.g., !@#$%^&*)

def is_strong(password):
    password = str(password)
    if len(password) < 8: return False          # - At least 8 characters long VALIDATION
    else:
        if password.isupper(): return False     # - At least one lowercase letter VALIDATION
        if password.islower(): return False     # - At least one uppercase letter VALIDATION
        for character in password:              # - At least one digit VALIDATION
            if character.isdecimal(): break
        else: return False
        for character in password:              # - At least one special character (e.g., !@#$%^&*) VALIDATION
            if character in ('!', '@', '#', '$', '%', '^', '&', '*'): break
        else: return False
    return True

while True:
    password = input("""# Password Limits
# - At least 8 characters long
# - At least one uppercase letter
# - At least one lowercase letter
# - At least one digit
# - At least one special character (e.g., !@#$%^&*)
    Enter Your New Password: """).strip()
    if is_strong(password): print(f"Your password {password} is strong. Confirm it!"); break
    else: print(f"Your password {password} is NOT strong enough. Try a stronger one!")
print('*' * 70)
####################################################################################################

# Application_3
# Digital Cash Register
print('-' * 10, 'Digital Cash Register', '-' * 10)
total = float(input("Enter the total cost: ").strip())
paid  = float(input("Enter the paid money: ").strip())
quarter, dime, nickel, penny = 20, 10, 5, 1

def change_calc(total, paid):   
    if total > paid: print(f"Sorry! You paid {paid}. We need {total - paid} more.")
    else:
        rest = paid - total
        quarters, dimes, nickels, pennies = 0, 0, 0, 0
        while rest >= 1:
            if rest >= 20: rest -= 20; quarters += 1
            elif rest >= 10: rest -= 10; dimes += 1
            elif rest >= 5: rest -= 5; nickels += 1
            elif rest >= 1: rest -= 1; pennies += 1
        else: return {
            '20s': quarters, 
            '10s': dimes, 
            '5s': nickels, 
            '1s': pennies
        }

print(change_calc(total, paid))
print('*' * 70)
####################################################################################################


# Application_4
# Sentence Formatter
print('-' * 10, 'Sentence Formatter', '-' * 10)
sentence = input("Enter the messy sentence: ")
def format_sentence(sentence): 
    sentence = str(sentence).strip().lower().capitalize()
    return sentence + '.'
print(f"The formated sentence: {format_sentence(sentence)}")
print('*' * 70)
####################################################################################################


# Application_5
# Multiplication Table Generator
print('-' * 10, 'Multiplication Table Generator', '-' * 10)
num = int(input("Enter Your Number: ").strip())
def mult_table(num):
    for x in range(1, num+1):
        print(f"# {str(x).zfill(3)} * {str(x).zfill(3)} = {x * x:,}")
mult_table(num)
print('*' * 70)
####################################################################################################


# Application_6
# List Duplicate Remover
print('-' * 10, 'List Duplicate Remover', '-' * 10)
mylist = [1, 2, 2, 1, 3, 3, 2, 4, 5, 4, 6, 6, 7, 8, 8, 4, 8, 9]
def remove_duplicates(mylist):
    pass    
print('*' * 70)
####################################################################################################



# Application_7
# Simple Unit Converter
print('-' * 10, 'Simple Unit Converter', '-' * 10)
def unit_converter():
    while True:
        choise = input("""Choose The Operation!
    Write (mile)    if you want to convert miles to kilometers
    Write (fehr)    if you want to convert fehrenheit to celsius
    Write (kgram)   if you want to convert kilograms to pounds
    Write (cm)      if you want to convert cente meters to inches
    Write (quit)    if you want to quit the program
    Your choise is: """).strip().lower()
        if choise == 'mile':
            mile = float(input("Enter the distance in miles: ").strip())
            print(f"The distance in kilometers: {mile * 1.699344}")
        elif choise == 'fehr': 
            fehr = float(input("Enter the degree in fahreheit: ").strip())
            print(f"The degree in celsuis: {(fehr - 32) * (5/9)}")
        elif choise == 'kgram': 
            kgram = float(input("Enter the weight in kilograms: ").strip())
            print(f"The weight in pounds: {kgram * 2.20462}")
        elif choise == 'cm': 
            cm = float(input("Enter the height in cente meters: ").strip())
            print(f"The height in inches: {cm / 2.54}")
        elif choise == 'quit': break
        else: print("Sorry, invlid input. Try again!")
unit_converter()
print('*' * 70)
####################################################################################################


# Application_8
# Dice Rolling Simulator
print('-' * 10, 'Dice Rolling Simulator', '-' * 10)
num_rolls = int(input("Enter the number of rolls: ").strip())
sides = int(input("Enter the number of sides: ").strip())
import random
# this functions returns a list of results
def roll_dice(num_rolls, sides):    
    result_list = []
    for i in range(num_rolls):
        roll = random.randint(1, sides)
        result_list.append(roll)
    return result_list
# This function anlyze the results 
def analysis(result_list):
    result_list = list(result_list)
    for i in range(1, 7):
        print(f"Frequency of ({i}) is: {float(100 * result_list.count(i) / len(result_list))}%")

analysis(roll_dice(num_rolls, sides))
print('*' * 70)
####################################################################################################


# Application_9
# Budget Tracker
print('-' * 10, 'Budget Tracker', '-' * 10)
word = input("Enter Your Word: ").strip()
def print_histogram(word):
    word = list(word)
    count = 0
    for letter in word:
        if word.count(letter) > 1 and count != word.index(letter): continue
        else: print(f"=> {letter}: {'*' * word.count(letter)}")
        count += 1
print_histogram(word)
print('*' * 70)
####################################################################################################


# Assignment_1
# Calculator: Add, Subtract, Multiply, Divide
print('-' * 10, 'Calculator: Add, Subtract, Multiply, Divide', '-' * 10)
special = ('!', '@', '#', '$', '%', '^', '&', '*')
Note = f'''{'#' * 65}
The supported operations is (add, sub, mult, div). 
You can write the first character of the operation if you want
{'#' * 65}'''
print(Note)
def is_valid_operand(operand):
    if not operand.isalpha() and not operand in special: return True
    else: return False

while True:
    operand_1 = input("Enter The First Operand: ").strip()
    operand_2 = input("Enter The Second Operand: ").strip()
    operation = input("Enter The Operation: ").strip().lower()
    if is_valid_operand(operand_1) and is_valid_operand(operand_2): break
    else: print("Invalid operands. Try again!")

def calculate(op1, op2, operation = 'add'):
    if      operation == 'add' or operation[0] == 'a': print(f"Chosen Operation: addition"); return float(op1) + float(op2)
    elif    operation == 'sub' or operation[0] == 's': print(f"Chosen Operation: subtraction"); return float(op1) - float(op2)
    elif    operation == 'mult'or operation[0] == 'm': print(f"Chosen Operation: multiplication"); return float(op1) * float(op2)
    elif    operation == 'div' or operation[0] == 'd': print(f"Chosen Operation: division"); return float(op1) / float(op2)
print(calculate(operand_1, operand_2, operation))
print('*' * 70)
####################################################################################################


# Assignment_2
# Addition with Unknown Number of Parameters
print('-' * 10, 'Addition with Unknown Number of Parameters', '-' * 10)
def addition(*params):
    tot = 0
    for param in params:
        if param == 5: tot -= param
        elif param == 10: tot = tot
        else: tot += param
    return tot
print(addition(10, 20, 30, 10, 15))             # 65
print(addition(10, 20, 30, 10, 15, 5, 100))     # 160
print('*' * 70)
####################################################################################################


# Assignment_3
# Skills Message
print('-' * 10, 'Skills Message', '-' * 10)
my_skills = 'HTML', 'CSS', 'JS', 'Verilog', 'C++', 'Python', 'SystemVerilog'
name = 'Kareem'
def show_skills(name, *skills):
    if len(skills) == 0: print(f"Hello {name} you've no skills to be shown")
    else: 
        print(f"Hello {name} your skills are: ")
        for skill in skills: print(f"- {skill}")
show_skills(name, *my_skills)
print('*' * 70)
####################################################################################################


# Assignment_4
# Skills Message
print('-' * 10, 'Skills Message', '-' * 10)
name, age, country = 'Kareem', 20, 'Egypt'
def say_hello(name='Unknown', age='Unknown', country='Unknown'):
    print(f"Hello {name} your age is {age} and you live in {country}")
say_hello(name, age, country)   # Hello Kareem your age is 20 and you live in Egypt
say_hello(name, age)            # Hello Kareem your age is 20 and you live in Unknown
say_hello(name)                 # Hello Kareem your age is Unknown and you live in Unknown
say_hello()                     # Hello Unknown your age is Unknown and you live in Unknown
print('*' * 70)
####################################################################################################


# Assignment_5
# Dictionary Unpacking
print('-' * 10, 'Dictionary Unpacking', '-' * 10)
def get_score(**subjects):
    for subject, score in subjects.items():
        print(f'"{subject} => {score}"')
get_score(Math=90, Science=80, Language=70)
get_score(Logic=90, Electronics=100)
print('*' * 70)
####################################################################################################


# Assignment_6
# People Scores
print('-' * 10, 'People Scores', '-' * 10)
def get_people_scores(*names, **subjects):
    for name in names:
        if len(subjects) == 0: print(f'"Hello {name} You Have No Scores To Be Shown')
        else:
            print(f'"Hello {name} Your Score Table: "')
            for subject, score in subjects.items():
                print(f'"{subject} => {score}"')
# Test 1
print('# Test 1')
get_people_scores("Kareem", Math=90, Science=80, Language=70)
# Test 2
print('# Test 2')
get_people_scores("Mahmoud", Logic=70, Problems=60)
# Test 3
print('# Test 3')
get_people_scores(Logic=70, Problems=60)
# Test 4
print('# Test 4')
get_people_scores("Ahmed")
# Test 5
print('# Test 5')
get_people_scores("kareem", "Ahmed", Logic=70, Problems=60)
print('*' * 70)
####################################################################################################


# Assignment_7
# Dictionary Unpacking
print('-' * 10, 'Dictionary Unpacking', '-' * 10)
scores_list = {
    'Math': 90, 
    'Science': 80, 
    'Language': 70
}
def get_the_scores(*name, **subjects):
    if len(name) != 0 and len(subjects) == 0: print(f"Hello {name[0]} You Have No Scores To Be Shown")
    elif len(name) != 0 and len(subjects) != 0: print(f"Hello {name[0]} Your Score Table: ")
    for subject, score in subjects.items():
        print(f"{subject} => {score}")

# Test 1
print('# Test 1')
get_the_scores("Kareem", **scores_list)
# Test 2
print('# Test 2')
get_the_scores("Kareem")
# Test 3
print('# Test 3')
get_the_scores(**scores_list)
print('*' * 70)
####################################################################################################
