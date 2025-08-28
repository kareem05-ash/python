# -----------------------------------------------------------------------------------------
# ----- This file is considered a practise on tuple and its methods -----
# [1st] Assignment: create your tuple with your name only without using () and print it out and its type
# [2nd] Assignment: create your tuple with 3 items change the first item and print it, its type, and # items out each in a single line
# [3rd] Assignment: create 2 tuples first, holds numbers from 1 to 3. second, holds A, B, C. Then concatenate them into a single tuple. Finally, print it, and # items out
# [4th] Assignment: destruct a tuple formed from 4 items into 3 variables. print out the variables
# -----------------------------------------------------------------------------------------

# [1st] Assignment: create your tuple with your name only without using () and print it out and its type
print(30 * '-', '[1st] Assignment', 30 * '-')
mytuple = 'kareem', 
print(mytuple)          # ('kareem',)
print(type(mytuple))    # <class 'tuple'>
# -----------------------------------------------------------------------------------------
# [2nd] Assignment: create your tuple with 3 items change the first item and print it, its type, and # items out each in a single line
print(30 * '-', '[2nd] Assignment', 30 * '-')
mytuple = 'kareem', 'ashraf', 'mostafa'
mytuple = "KAREEM", mytuple[1], mytuple[2]
print(mytuple)
print(type(mytuple))
# -----------------------------------------------------------------------------------------
# [3rd] Assignment: create 2 tuples first, holds numbers from 1 to 3. second, holds A, B, C. Then concatenate them into a single tuple. Finally, print it, and # items out
print(30 * '-', '[3rd] Assignment', 30 * '-')
first = 1, 2, 3
second = 'A', 'B', 'C'
cat_tuple = first + second
print(cat_tuple)        # (1, 2, 3, 'A', 'B', 'C')
print(type(cat_tuple))  # <class 'tuple'>
print(len(cat_tuple))   # 6
# -----------------------------------------------------------------------------------------
# [4th] Assignment: destruct a tuple formed from 4 items into 3 variables. print out the variables
print(30 * '-', '[4th] Assignment', 30 * '-')
mytuple = True, 'kareem', 23, [22, 32, False]
a, b, _, c = mytuple
print(a, type(a))       # True <class 'bool'>
print(b, type(b))       # 'kareem' <calss 'str'>
print(c, type(c))       # [22, 32, False] <calss 'list'>
# -----------------------------------------------------------------------------------------
