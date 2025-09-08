# This file is for some small applications on while loops in python
######################################################################################################################################################

# Application_1
# Input Validation
print("Input Validation")
while True:
    age = input("Enter your age: ")
    if age.isdecimal(): age = float(age); break
    elif age.isalpha(): print("Invalid age. Try again!")
    elif age.isalnum(): print("Invalid age. Try again!")
    else: 
        agelist = age.split('.')
        if len(agelist) != 2: print("Invalid age. Try again!")
        else:
            if agelist[0].isdecimal() and agelist[1].isdecimal(): age = float(age); break
print(f"Your age: {age}")
print(type(age))
print('*' * 50)
######################################################################################################################################################

# Application_2
# Gussing-Number Game
print("Gussing-Number Game")
admin_num = 23
guess_num = 0
while True:
    guess_num += 1
    user_num = input("Guess the number between [0 => 100]: ").strip()
    if not user_num.isdecimal(): print("Sorry, invalid input. Guess a valid number!")
    else:
        user_num = int(user_num)
        if not 0 <= user_num <= 100: print("Sorry, out of range input. Guess a valid number!")
        else: 
            if user_num > 2*admin_num: print("Incorrect! Too high")
            elif user_num > admin_num: print("Incorrect! Your're close")
            elif 2*user_num < admin_num: print("Incorrect! Too low")
            elif user_num < admin_num: print("Incorrect! Your're close here")
            elif user_num == admin_num: print("Your'are RIGHT!!!"); break
print(f"You've got the right number({admin_num}) after '{guess_num}' guesses")
print('*' * 50)
######################################################################################################################################################

# Application_3
# Fibonacci Sequence
print("Fibonacci Sequence")
# User Prompt
while True:
    num = input("How many Fibonacci numbers do you want?: ").strip()
    if not num.isdecimal(): print("Invalid input. Try a valid integer number!")
    else: num = int(num); break
# Sequence Loop
iteration = 0
fib_list = [0, 1]
while iteration < num:
    print(fib_list[iteration])
    iteration += 1
    fib_list.append(fib_list[len(fib_list)-1] + fib_list[len(fib_list)-2])

print('*' * 50)
######################################################################################################################################################

# Application_4
# Exponential Grouth Simmulator
print("Exponential Grouth Simmulator")
first_pop = 100
current_pop = 100
admin_limit = 1_000_000
hr = 0

while current_pop < admin_limit:
    print(f"@ hour({hr}): population is ({current_pop:,})")
    hr += 1
    current_pop = 2*current_pop
print(f"It took ({hr}) hours to exceede ({admin_limit:,}) and hit ({current_pop:,})")
print('*' * 50)
######################################################################################################################################################
