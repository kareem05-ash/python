######################################################################################################################################################
# ---------- This File Shows Built-in Functions In Python ----------
# ------------------------------------------------------------------
# [1] all(iterable)             => returns True if all the elements in the iterable are True value. Else returns False
# [2] any(iterable)             => returns True if at least one of the elements of the iterable are True value. Else returns False
# [3] bin(x)                    => returns the Binary value of any integer x
# [4] id(variable)              => returns the id of the variable. NOTE: this id is unique
# [5] sum(iterable, start)      => returns the sum of all elements in your iterabe + start. NOTE: start is optional. start's default value is 0
# [6] round(num, n_digits)      => returns the num rounded to n_digits after the dot
# [7] range(start, end, step)   => returns a range of numbers from start to end exclusively. NOTE: start is optional, its defalut value: 0. step is optional, its default value
# [8] print(your input)         => returns the value of your input
#       NOTE: It can take many arguments ot be printed. e.g., print('karee', 'ashraf', 'mostafa'). O/P: kareem ashraf mostafa
#       NOTE: sep='value': this attribute seperate your arguments by this value. e.g., print('kareem', 'ashraf', sep='|'). O/P: kareeem|ashraf
#           NOTE: It's totaly optional. Its default value is space
#       NOTE: end='value': this attribute configre the last character to be printed with your input.
#           NOTE: It's totaly optional. Its default value is '\n' new line
#           e.g., print('1st line', end='#')
#                 print('2nd line', end='#')  
#                 O/P: 1st line#2nd line# 
# [9] abs(num)                  => returns the absolute value of your num
# [10] pow(base, exp, mod)      => returns the modules of base to the power of exp. NOTE: mod is optional 
#       e.g., print(pow(2, 5, 10)): 2**5 % 10 = 32 % 10 = 2
# [11] min(iterable or items)   => returns the minimum number of your iterable or the minimum number of the input items
# [12] max(iterable or items)   => returns the maximum number of your iterable or the maximum number of the input items 
# [13] slice(start, end, step)  => slices your iterable from start to end exclusively by step 'step'
# [14] map(function, iterable)  => maps all items in the iterable for the your function
#       NOTE: function can be pre-defined function or lambda function
# [15] filter(function, iterable)   => does the same as map() does but it filters your iterable items to a condition you define
#       NOTE: filter() works if the returned data from you function is True
#       NOTE: Your pre-defined function or lambda function must return True value if the condition met to engine your filter
# [16] reduce(function, iterable)   => NOTE 1: The pre-defined function or lambda function must take 2 arguments
#                                   => NOTE 2: The returned value from the first 2 items in your iterable is taken with the 3rd items as the arguments in the following function calling and so on
#                                   => NOTE 3: reduce() must be imported from 'functools' module
# [17] enumerate(iterable, start=0) => generates a counter to your itrable items. configurable start with default value = 0
# [18] help(method)                 => gives a guideline for the inserted method
# [19] reversed(iterable)           => returns your itrable reversed. e.g., [2, 5, 23] --> [23, 5, 2]                                                                                                 #
######################################################################################################################################################


# [1] all(iterable)
print('# [1] all(iterable)')
mylist = [1, 2, 'kareem', True] # This is my iterable
print(all(mylist))  # True
mylist = [1, 2, 'kareem', True, ()] # This is my iterable
print(all(mylist))  # False
print('*' * 70)


# [2] any(iterable)
print('# [2] any(iterable)')
mylist = [1, 2, 'kareem', True, False, []]  # This is my iterable
print(any(mylist))  # True
mylist = [0, [], '', False, ()] # This is my iterable
print(any(mylist))  # False
print('*' * 70)


# [3] bin(x)
print('# [3] bin(x)')
print(bin(15))      # 0b1111
# print(bin(15.3))    # Error: bin() takes integers only
print(bin(20))      # 0b10100
print('*' * 70)


# [4] id(variable)
print('# [4] id(variable)')
name, age, country = 'kareem', 20, 'egypt'
print(id(name))     # e.g., 2222219905646640
print(id('kareem')) # The same as name's id: 2222219905646640
print(id(age))      # e.g., 2222219905643234233
print(id(20))       # The same as age's id: 2222219905643234233
print(id(country))  # e.g., 2222219905323993
print(id('egypt'))  # The same as country's id: 2222219905323993
print('*' * 70)


# [5] sum(iterable, start)
print('# [5] sum(iterable, start)')
sallaries = [20, 39, 30, 11]
print(sum(sallaries))       # 100
print(sum(sallaries, 30))   # 130
print(sum([2, 3, 5, False], 32))    # 42. NOTE: value of False is considered 0
print(sum([2, 3, 5, True], 32))     # 43. NOTE: value of True is considered 1
# print(sum([23, 30, 'kareem']))      # This will release an error
# print(sum([23, 3, 4,[]]))           # This will release an error
print('*' * 70)


# [6] round(num, n_digits)
print('# [6] round(num, n_digits)')
print(round(22.55))         # 23
print(round(22.5))          # 22
print(round(100.449, 2))    # 100.45
print(round(100.449, 3))    # 100.459
print(round(22.501, 6))     # 22.501
print(round(22.501, 3))     # 22.501
print('*' * 70)


# [7] range(start, end, step)
print('# [7] range(start, end, step)')
print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(0, 5)))        # [0, 1, 2, 3, 4]
print(tuple(range(1, 6)))       # (1, 2, 3, 4, 5)
print(list(range(0, 10, 2)))    # [0, 2, 4, 6, 8]
print(list(range(5, 0, -1)))    # [5, 4, 3, 2, 1]
print(list(range(10, 0, -2)))   # [10, 8, 6, 4, 2]
print('*' * 70)


# [8] print(your input)
print('# [8] print(your input)')
print('Kareem', 'Ashraf', 'Mostafa')                # Kareem Ashraf Mostafa
print('Kareem Ashraf Mostafa')                      # Kareem Ashraf Mostafa
print('Kareem', 'Ashraf', 'Mostafa', sep='@')       # Kareem@Ashraf@Mostafa
print('Kareem', 'Ashraf', 'Mostafa', sep='%')       # Kareem%Ashraf%Mostafa
print('This is my first line', end='END')
print('This is my second line')                     # This is my first lineENDThis is my second line
print('This is my first line', end=' END ')
print('This is my second line')                     # This is my first line END This is my second line
print('This is my first line', end='\t')
print('This is my second line')                     # This is my first line   This is my second line
print('*' * 70)


# [9] abs(num)
print('# [9] abs(num)')
print(abs(20))      # 20
print(abs(-20))     # 20
print(abs(15.55))   # 15.55
print(abs(-12.55))  # 12.55
print('*' * 70)


# [10] pow(base, exp, mod)
print('# [10] pow(base, exp, mod)')
print(pow(2, 5, 10))    # 2**5 % 10 = 32 % 10 = 2
print(pow(3, 3))        # 27
print(pow(4, 3, 5))     # 4**3 % 5 = 64 % 5 = 4
print('*' * 70)


# [11] min(iterable or items)
print('# [11] min(iterable or items)')
nums = (1, 234, 5 , 22, -50)
print(min(nums))        # -50
print(min(22, 34, -2, -39))     # -39
names = ('Kareem', 'A', 'O', 'S')
print(min(names))       # A
names = ('Kareem', 'O', 'S')
print(min(names))       # Kareem
print('*' * 70)


# [12] max(iterable or items)
print('# [12] max(iterable or items)')
nums = (1, 234, 5 , 22, -50)
print(max(nums))        # 234
print(max(22, 34, -2, -39))     # 34
names = ('Kareem', 'A', 'O', 'S')
print(max(names))       # S
names = ('Kareem', 'O', 'S', 'Z')
print(max(names))       # Z
print('*' * 70)


# [13] slice(start, end, step) 
print('# [13] slice(start, end, step)')
mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mylist[slice(5)])         # [0, 1, 2, 3, 4]
print(mylist[slice(0, 5)])      # [0, 1, 2, 3, 4]
print(mylist[slice(0, 5, 2)])   # [0, 2, 4]
print(mylist[slice(9, 0, -2)])  # [9, 7, 5, 3, 1]
print(mylist[slice(19, 0, -2)]) # [9, 7, 5, 3, 1]
print('*' * 70)


# [14] map(function, iterable)
print('# [14] map(function, iterable)')
        # Pre-Defined Function
def format_name(name): 
    return f'- {name.strip().title()} -'
print(map(format_name, ['kAReem   ', '  AHMed ', 'MoHAmED   ']))        # <map object at 0x0000001CBA--- some address
print('# Pre-Defined Function')
for name in map(format_name, ['kAReem   ', '  AHMed ', 'MoHAmED   ']): print(name)
        # Lambda Function 
print('# Lambda Function')
for fname in map(lambda name: f'- {name.strip().title()} -', ['kAReem   ', '  AHMed ', 'MoHAmED   ']): print(fname)
print('*' * 70)



# [15] filter(function, iterable)
print('# [15] filter(function, iterable)')
admins = ['Kareem', 'Ashraf', 'Mostafa']
NAMES = ['Kareem', 'Ahmed', 'Ashraf', 'Mohamed', 'Sayed']
        # Pre-Defined Function
print('# Pre-Defined Function')
def myfunc(name): return name in admins
for person in filter(myfunc, NAMES): print(f"## {person} ##")
        # Lambda Function 
print('# Lambda Function')
for person in filter(lambda name: name in admins, NAMES): print(f"** {person} **")
print('*' * 70)



# [16] reduce(function, iterable)
print('# [16] reduce(function, iterable)')
import functools
nums = [1, 23, 5, 23, 5]
        # Pre-Defined Function
print('# Pre-Defined Function')
def get_sum(num1, num2): return num1 + num2
print(sum(nums))        # 57
print(functools.reduce(get_sum, nums))  # 57
        # Lambda Function 
print('# Lambda Function')
print(functools.reduce(lambda n1, n2: n1 + n2, nums))   # 57
print('*' * 70)



# [17] enumerate(iterable, start=0)
print('# [17] enumerate(iterable, start=0)')
skills = ('HTML', 'CSS', 'JS', 'React.js', 'Node.js', 'SQL', 'MangoDB')
# Ordinary Method
print('# Ordinary Method')
count = 0
for skill in skills: 
    print(f'{count}: {skill}')
    count += 1
# Enumerated Method
print('# Enumerated Method')
for num, skill in enumerate(skills): print(f'{num}: {skill}')
# Ordinary Method
print('# Ordinary Method')
count = 10
for skill in skills: 
    print(f'{count}: {skill}')
    count += 1
# Enumerated Method
print('# Enumerated Method')
for num, skill in enumerate(skills, 10): print(f'{num}: {skill}')
print('*' * 70)
