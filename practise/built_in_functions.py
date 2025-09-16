# This File Shows 8 Applications and 8 Assignments on Built-In-Functions in Python

####################################################################################################
# Application_1: Data Validation For User Registeration
print('*' * 20, '# Application_1: Data Validation For User Registeration', '*' * 20)
username, email, password = '', 'k@sd.sd', ''      # Registeration Fields
special = ('!', '@', '#', '$', '%', '^', '&', '*')
def un_isvalid(username):  return all([len(username)>=3, username.isalnum()])
def em_isvalid(email): return all([email.islower(), '@' in email, '.' in email[email.index('@'):]])
def pass_isvalid(password): 
    cond1 = len(password) >= 8
    cond2 = any(list(map(str.isupper, password)))
    cond3 = any(list(map(str.islower, password)))
    cond4 = any(list(map(lambda c: c in special, password)))
    return all([cond1, cond2, cond3, cond4])
if all([un_isvalid('kareem05'), em_isvalid('valid.em@gmail.com'), pass_isvalid('Kare1212@a')]): print("DONE")
else: print("NOT YET")
####################################################################################################
# Application_2: Statistical Summary Generator
print('*' * 20, '# Application_2: Statistical Summary Generator', '*' * 20)
nums = [1, 23, 5, -2, 32, 55, 230, -23, 34]
SUM = sum(nums)
MIN = min(nums)
MAX = max(nums)
AVG = round(SUM/len(nums), 2)
print(f"The Sum: {SUM}")
print(f"The Minimum number: {MIN}")
print(f"The Maximum number: {MAX}")
print(f"The Average: {AVG}")
####################################################################################################
# Application_3: Text-Base Data Visualizer
print('*' * 20, '# Application_3: Text-Base Data Visualizer', '*' * 20)
skills = {      # skills = {skill: percentage}
    'HTML': 100, 
    'CSS': 10, 
    'JS': 0, 
    'React.js': 0, 
    'Node.js': 0, 
    'Python': 60, 
    'Verilog': 100, 
    'SystemVerilog': 0, 
    'C++': 60
}
def rotate(text, length, placeholder):
    rtext = ''
    if len(text) >= length: return text
    else: 
        for x in range(int((length-len(text))/2) + 1): rtext += placeholder
        rtext += text
        for x in range(length-len(rtext)): rtext += placeholder
        return rtext

def show_statistics(**skills): 
    for skill, rate in skills.items(): 
        print(f"{rotate(skill, 14, '_')} :", end=' ')
        for x in range(rate): print('#', end='')
        print()

show_statistics(**skills)
# print(rotate('kareem', 15, '#'))
####################################################################################################
# Application_4: List Pagination System
print('*' * 20, '# Application_4: List Pagination System', '*' * 20)
data = ['Apple', 'Banana', 'Chery', 'Date', 'Elderberry', 'Fig', 'Grape']
def paginate(cpage, page_items, *items): 
    if len(items)%page_items == 0: tot = len(items)/page_items
    else: tot = len(items)/page_items + 1
    return {
    'Page Items': list(items[slice((cpage-1)*page_items, (cpage-1)*page_items+page_items)]),
    'Current Page Number': cpage, 
    'Total Number Of Pages': int(tot)
}
for item, value in paginate(2, 3, *data).items(): print(f"{item}: {value}")
####################################################################################################
# Application_5: Sequence Comparison Tool
print('*' * 20, '# Application_5: Sequence Comparison Tool', '*' * 20)
mylist, mystr = ['k', 'a', 'r', 'e', 'e', 'm'], 'kareem'

def is_identical(itr1, itr2):
    conds = []
    if len(itr1) != len(itr2): return False
    else: 
        for i in range(len(itr1)):
            if id(itr1[i]) == id(itr2[i]): conds.append(True)
            else: conds.append(False)
        return all(conds)
    
print(is_identical(mystr, mylist))
####################################################################################################
# Application_6: Number Base Converter
print('*' * 20, '# Application_6: Number Base Converter', '*' * 20)
def bin_convert(num):
    if num < 0: print(f"Binary representation of {num} is: -ve {bin(abs(num))}")
    else: print(f"Binary representation of {num} is: {bin(abs(num))}")

bin_convert(233)
bin_convert(-233)
####################################################################################################
# Application_7: Palindrome & Word Reverser
print('*' * 20, '# Application_7: Palindrome & Word Reverser', '*' * 20)
def is_palindrome(itr): 
    conds = []
    rvrsd = ''.join(reversed(itr))
    for i in range(len(itr)):
        if itr[i] == rvrsd[i]: conds.append(True)
        else: conds.append(False)
    return all(conds)
def show(word):
    print(f"The Word            : {word}")
    print(f"The Reversed Word   : {''.join(reversed(word))}")
    print(f"This Word Is{' ' if is_palindrome(word) else ' NOT'} a Palindrome")
    print(is_palindrome(word))
for x in ['level', 'civic', 'deified', 'kayak', 'madam', 'racar']: show(x); print(20 * '-')
####################################################################################################
# Application_8: Spatial Proximity Calculator
print('*' * 20, '# Application_8: Spatial Proximity Calculator', '*' * 20)
def find_closest(target, *coordinates):
    dists = []
    for coordinate in coordinates: dists.append(pow(coordinate[0]-target[0], 2) + pow(coordinate[1]-target[1], 2))
    return coordinates[dists.index(min(dists))]
print(find_closest((2, 2), (3, 5), (23, 43)))
####################################################################################################
####################################################################################################
# Assignment_1
print('*' * 20, 'Assignment_1', '*' * 20)
values = (0, 1, 2)
if any(values): my_var = 0
my_list = [True, 1, 1, ['A', 'B'], 10.5, my_var]
if all(mylist[:4]) or all(mylist[:6]) or all(mylist[:]): print('Good')
else: print('Bad')
# Output: Good
####################################################################################################
# Assignment_2
print('*' * 20, 'Assignment_2', '*' * 20)
v = 40
my_range = list(range(v))
print(sum(my_range, v) + pow(v, v, v))
####################################################################################################
# Assignment_3
print('*' * 20, 'Assignment_3', '*' * 20)
n = 21
l = list(range(n))
if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9): print('Good')
# Output: Good
####################################################################################################
# Assignment_4
print('*' * 20, 'Assignment_4', '*' * 20)
def my_all(conds): 
    for cond in conds:
        if not cond: return False
    return True
def my_any(conds): 
    for cond in conds: 
        if cond: return True
    return False
def my_min(nums): 
    minimum = nums[0]
    for num in nums[1:]: 
        if num < minimum: minimum = num
    return minimum
def my_max(nums): 
    maximum = nums[0]
    for num in nums[1:]: 
        if num > maximum: maximum = num
    return maximum
# my_all()
print(my_all([1, 2, 3]))    # True
print(my_all([1, 2, 3, []]))# False
# my_any()
print(my_any([0, 1, [], False]))    # True
print(my_any([(), 0, False]))       # False
# my_min()
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100
# my_max()
print(my_max([10, 100, -20, -100, 50, 700]))    # 700
print(my_max((10, 100, -20, -100, 50, 700)))    # 700
####################################################################################################
# Assignment_5
print('*' * 20, 'Assignment_5', '*' * 20)
def rm_chars(text): return text[1:-1]
missy = ['AEmanS', 'AAhmedS', 'DSamehF', 'LOsamaL']
clean = list(map(rm_chars, missy))
for name in clean: print(name)
####################################################################################################
# Assignment_6
print('*' * 20, 'Assignment_6', '*' * 20)
def get_names(name):
    name = str(name)
    if name.endswith('m'):  return True
names = tuple(filter(get_names, ['Waseem', 'Amal', 'Essam', 'Gamal', 'Othman']))
for name in names: print(name)
####################################################################################################
# Assignment_7
print('*' * 20, 'Assignment_7', '*' * 20)
from functools import reduce
nums = [2, 4, 6, 2]
def multiply(num1, num2): return num1 * num2
print(reduce(multiply, nums))
print(reduce(lambda n1, n2: n1*n2, nums))
####################################################################################################
# Assignment_8
print('*' * 20, 'Assignment_8', '*' * 20)
skills = ('HTML', 'CSS', 10, 'PHP', 'Python', 20, 'JavaScript')
# First Mehtod
for n, x in enumerate(reversed(skills), 50): 
    x = str(x)
    if not x.isdecimal(): print(f"{n} = {x}")
# Second Method
n = 50
for skill in reversed(skills): 
    skill = str(skill)
    if not skill.isdecimal(): print(f"{n} - {skill}")
    n += 1