# --------------------------------------------------------------------------------
# ---------Lists----------
# ------------------------
# ex. my_list = ["kareem", 2, 5, True, False, 3+5j, 23.00].
# Lists are zero-base indexed.
# List items are mutable => we can edit, delete, add items.
# List can hold different data types.
# --------------------------------------------------------------------------------

my_list = ["kareem", 2, 5, True, False, 3+5j, 23.00]
print(my_list) # prints the whole list : ['kareem', 2, 5, True, False, (3+5j), 23.0]
print(my_list[1:5]) # prints : [2, 5, True, False]. Note that ending index isn't included.
print(my_list[ :6]) # prints from start to my_list[5] : ['kareem', 2, 5, True, False, (3+5j)]
print(my_list[-1]) # prints the last item : 23.0
print(my_list[ : : 2]) # prints the whole list with step (2) : ['kareem', 5, False, 23.0]
print(my_list[1:6:2]) # prints from index 1 to 5 with step (2) : [2, Trues, (3+5j)]
print(my_list[-3]) # prints the third item from the end : False.
print(my_list[ : -1 : 1]) # prints from start to the second item from the end with step (1)
                          # ['kareem', 2, 5, True, False, (3+5j)].

her_list = ['one', 'two', 'three', 'four', 'five']
her_list[ :3] = [] # this deletes the items specified
print(her_list) # prints the list after deletion : ['four', 'five']
print(her_list[ : ]) # prints : ['four', 'five']
her_list[2:5] = [1, 2, 3]
print(her_list) # prints : ['four', 'five', 1, 2, 3]
her_list = [1, 2, 3]
print(her_list) # prints : [1, 2, 3]
her_list[3:] = ['kareem', 'ashraf', 'mostafa', 'aboelala']
print(her_list[3: ]) # prints : ['kareem', 'ashraf', 'mostafa', 'aboelala']
print(her_list) # pritns : [1, 2, 3, 'kareem', 'ashraf', 'mostafa', 'aboelala']

print(type(her_list)) # <class 'list'>
print(type(her_list[0])) # <class 'int'>
print(type(her_list[-1])) # <class 'str'>
