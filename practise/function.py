# # Some Small Applications on User Defined Functions in Python

# # Application_1
# # prime Number Generator
# print('-' * 10, 'prime Number Generator', '-' * 10)
# def is_prime(num):
#     for i in range(2, num): 
#         if num%i == 0: return False
#     return True
# def generate_primes(limit):
#     for num in range(2, limit+1):
#         if is_prime(num): print(num)
# generate_primes(int(input("Enter The Limit: ").strip()))
# # print(is_prime(13))
# print('*' * 70)
# ####################################################################################################

# # Application_2
# # Password Strength Validator
# print('-' * 10, 'Password Strength Validator', '-' * 10)
# # Password Limits
# # - At least 8 characters long
# # - At least one uppercase letter
# # - At least one lowercase letter
# # - At least one digit
# # - At least one special character (e.g., !@#$%^&*)

# def is_strong(password):
#     password = str(password)
#     if len(password) < 8: return False          # - At least 8 characters long VALIDATION
#     else:
#         if password.isupper(): return False     # - At least one lowercase letter VALIDATION
#         if password.islower(): return False     # - At least one uppercase letter VALIDATION
#         for character in password:              # - At least one digit VALIDATION
#             if character.isdecimal(): break
#         else: return False
#         for character in password:              # - At least one special character (e.g., !@#$%^&*) VALIDATION
#             if character in ('!', '@', '#', '$', '%', '^', '&', '*'): break
#         else: return False
#     return True

# while True:
#     password = input("""# Password Limits
# # - At least 8 characters long
# # - At least one uppercase letter
# # - At least one lowercase letter
# # - At least one digit
# # - At least one special character (e.g., !@#$%^&*)
#     Enter Your New Password: """).strip()
#     if is_strong(password): print(f"Your password {password} is strong. Confirm it!"); break
#     else: print(f"Your password {password} is NOT strong enough. Try a stronger one!")
# print('*' * 70)
# ####################################################################################################

# # Application_3
# # Digital Cash Register
# print('-' * 10, 'Digital Cash Register', '-' * 10)
# total = float(input("Enter the total cost: ").strip())
# paid  = float(input("Enter the paid money: ").strip())
# quarter, dime, nickel, penny = 20, 10, 5, 1

# def change_calc(total, paid):   
#     if total > paid: print(f"Sorry! You paid {paid}. We need {total - paid} more.")
#     else:
#         rest = paid - total
#         quarters, dimes, nickels, pennies = 0, 0, 0, 0
#         while rest >= 1:
#             if rest >= 20: rest -= 20; quarters += 1
#             elif rest >= 10: rest -= 10; dimes += 1
#             elif rest >= 5: rest -= 5; nickels += 1
#             elif rest >= 1: rest -= 1; pennies += 1
#         else: return {
#             '20s': quarters, 
#             '10s': dimes, 
#             '5s': nickels, 
#             '1s': pennies
#         }

# print(change_calc(total, paid))
# print('*' * 70)
# ####################################################################################################


# # Application_4
# # Sentence Formatter
# print('-' * 10, 'Sentence Formatter', '-' * 10)
# sentence = input("Enter the messy sentence: ")
# def format_sentence(sentence): 
#     sentence = str(sentence).strip().lower().capitalize()
#     return sentence + '.'
# print(f"The formated sentence: {format_sentence(sentence)}")
# print('*' * 70)
# ####################################################################################################


# # Application_5
# # Multiplication Table Generator
# print('-' * 10, 'Multiplication Table Generator', '-' * 10)
# num = int(input("Enter Your Number: ").strip())
# def mult_table(num):
#     for x in range(1, num+1):
#         print(f"# {str(x).zfill(3)} * {str(x).zfill(3)} = {x * x:,}")
# mult_table(num)
# print('*' * 70)
# ####################################################################################################


# Application_6
# List Duplicate Remover
print('-' * 10, 'List Duplicate Remover', '-' * 10)
mylist = [1, 2, 2, 1, 3, 3, 2, 4, 5, 4, 6, 6, 7, 8, 8, 4, 8, 9]
def remove_duplicates(mylist):
    mylist = list(mylist)
    
print('*' * 70)
####################################################################################################

