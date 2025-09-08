
# Application_1
# Guess the number
print('-' * 10, "Guess the number game", '-' * 10)

tot_chances = 5
secret_num = 42
for chance in range(tot_chances):
    num = int(input("Guess the number: ").strip())
    if num == secret_num: print("You're right!!"); break
    else: print(f"Incorrect. Try again! ({tot_chances-chance-1}) chances left")
print('#' * 80)
######################################################################################################################################################

# Application_2
# Shopping Cart Calculator
print('-' * 10, "Shopping Cart Calculator", '-' * 10)
prices = [2.50, 5.99, 3.75, 12.99, 1.50]
discout_percentage = 10
discount = 0
tot = 0
for price in prices: tot += price
if tot > 20: discount = float(tot * float(discout_percentage/100))
print(f"The total charge before discount: {tot}")
print(f"{discout_percentage}% discount: {discount}")
print(f"The total charge after discount: {tot - discount}")
print('#' * 80)
######################################################################################################################################################

# Application_3
# Vowel Counter & String Reverser
print('-' * 10, "Vowel Counter & String Reverser", '-' * 10)
sentence = input("Enter your sentence: ").strip()
vowel = 'a', 'o', 'u', 'i', 'e'
count = 0
reversed_sentence = ''
for letter in sentence:
    if letter in vowel: count += 1
for letter in sentence:
    reversed_sentence = letter + reversed_sentence
print(f"The number of Vowel letters is: {count}")
print(f"The reversed sentence is: {reversed_sentence}")
print('#' * 80)
######################################################################################################################################################

# Application_4
# Multiplication Table
print('-' * 10, "Multiplication Table", '-' * 10)
num = int(input("Enter a Number: ").strip())
for i in range(10):
    print(f"{num} * {i+1} = {num * (i+1)}")
print('#' * 80)
######################################################################################################################################################

# Application_5
# Anagram Checker
print('-' * 10, "Anagram Checker", '-' * 10)
first = list(input("Enter the first word/sentence: ").strip())
second = list(input("Enter the second word/sentence: ").strip())
is_anagram = True
if len(first) == len(second):
    for letter in first: 
        if not letter in second:
            is_anagram = False
            break
else: is_anagram = False
new1 = ''
new2 = ''
for letter in first: new1 += letter
for letter in second: new2 += letter
if is_anagram   : print(f"The first word/sentence ({new1}) IS an anagram of the second word/sentence ({new2})")
else            : print(f"The first word/sentence ({new1}) IS NOTTTT an anagram of the second word/sentence ({new2})")
print('#' * 80)
######################################################################################################################################################

# Assignment_1
# 5 dividors
print('-' * 10, "5 dividors", '-' * 10)
nums = [15, 81, 5, 17, 20, 21, 13]
nums5 = []
for num in nums:
    if num % 5 == 0: nums5.append(num)
nums5.sort(reverse=True)
print("All Numbers'v been printed")
print('#' * 80)
######################################################################################################################################################

# Assignment_2
# Zero Fill
print('-' * 10, "Zero Fill", '-' * 10)
for x in range(20):
    num = str(x+1)
    print(f"{num.zfill(2)}")
print('#' * 80)
######################################################################################################################################################

# Assignment_3
# One Level Dictionary
print('-' * 10, "One Level Dictionary", '-' * 10)
ranks = {
    'Math': 'A', 
    'Science': 'B', 
    'Drawing': 'A', 
    'Sports': 'C'
}
tot_points = 0
for sub in ranks:
    if ranks[sub] == 'A': pts = 100
    elif ranks[sub] == 'B': pts = 80
    elif ranks[sub] == 'C': pts = 40
    tot_points += pts
    print(f"My Rank in {sub} Is {ranks[sub]} And This Equals {pts} Points")
print('#' * 80)
######################################################################################################################################################

# Assignment_4
# Nested Dictionaries
print('-' * 10, "Nested Dictionaries", '-' * 10)
students = {
    'Kareem': {
        'Math': 'A', 
        'Science': 'D', 
        'Drawing': 'B', 
        'Sports': 'C', 
        'Thinking': 'A'
    },
    'Ashraf': {
        'Math': 'B', 
        'Science': 'B', 
        'Drawing': 'B', 
        'Sports': 'D', 
        'Thinking': 'A'
    },
    'Mostafa': {
        'Math': 'D', 
        'Science': 'A', 
        'Drawing': 'A', 
        'Sports': 'B', 
        'Thinking': 'B'
    }
}
A_pts = 100; B_pts = 80; C_pts = 40; D_pts = 20
# First Way
print('*' * 10, "First Way", '*' * 10)
for student in students:
    print(30 * '-')
    print(f"-- Student Name => {student}")
    print(30 * '-')
    tot = 0
    for sub in students[student]:
        if students[student][sub] == 'A': sub_pts = A_pts
        if students[student][sub] == 'B': sub_pts = B_pts
        if students[student][sub] == 'C': sub_pts = C_pts
        if students[student][sub] == 'D': sub_pts = D_pts
        tot += sub_pts
        print(f"- {sub} => {sub_pts} Points")
    print(f"Total Points For {student} Is {tot}")
# Second Way
print('*' * 10, "Second Way", '*' * 10)
items_students = students.items()
for student, subs in items_students:
    print(30 * '-')
    print(f"-- Student Name => {student}")
    print(30 * '-')
    tot = 0
    for sub in subs:
        if subs[sub] == 'A': sub_pts = A_pts
        if subs[sub] == 'C': sub_pts = C_pts
        if subs[sub] == 'B': sub_pts = B_pts
        if subs[sub] == 'D': sub_pts = D_pts
        tot += sub_pts
        print(f"- {sub} => {sub_pts} Points")
    print(f"Total Points For {student} Is {tot}")
print('#' * 80)
######################################################################################################################################################

