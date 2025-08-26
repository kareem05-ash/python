# -------------------------------------------------------------------------------------------
# ------ Dictionarie Methods -------
# ----------------------------------
# dict_name.clear()                 : It clears the dictionary 'dict_name'
# my_dict = dict_name.copy()        : It copies all items in dict 'dict_name' into another dict 'my_dict'
# dict_name.update({key, value})    : It inserts the new key with its value to the dict 'dict_name'
# dict_name.keys()                  : It returns all keys of dict 'dict_name'
# dict_name.values()                : It returns all values of dict 'dict_name'
# dict_name.setdefault(key, value)  : It returns the past value and updates the dict 'dict_name' with the key.
#                               NOTE: If the key is allready exists, this method will do nothing
#                               NOTE: If value is missing (dict_name.setdefault(key)), the value will considered (None)
# dict_name.popitem()               : It returns the last item added to the dict and remove it from the dict
# ITEMS = dict_name.items()         : It stores the items of the dict'dict_name' into a list 'ITEMS'.
#                               NOTE: Each item(key, value) will be stored as a tuple in the list 'ITEMS'
# dict_name = dict.fromkeys(A, B)   : A & B are tuples. this method returns a dict with keys in tuple (A). The values of these keys are the same and is a tuple (B)
#                               NOTE: If tuple (B) consists of more than one item, the value of each key in (A) is considered a tuple(B)
# -------------------------------------------------------------------------------------------
print('-' * 70)

# dict_name.clear()         : It clears the dictionary 'dict_name'

dict_name = {
    'name'      : 'kareem'
}
print(dict_name)    # {'name': 'kareem'}
dict_name.clear()
print(dict_name)    # {}
print('=' * 70)

# dict_name.copy(my_dict)           : It copies all items in dict 'dict_name' to another dict 'my_dict'

dict1 = {
    1   : True, 
    2   : 'False'
}
dict2 = dict1.copy()
print(dict1)    # {1: True, 2: 'Fasle'}
print(dict2)    # {1: True, 2: 'Fasle'}
dict1[3] = 'True & False'
print(dict1)    # {1: True, 2: 'Fasle', 3: 'True & False'}
print(dict2)    # {1: True, 2: 'Fasle'}
print('=' * 70)

# dict_name.update({key, value})    : It inserts the new key with its value to the dict 'dict_name'

dict_name = {
    'name'      : 'kareem'
}
print(dict_name)    # {'name': 'kareem'}
dict_name.update({'age': 20})
print(dict_name)    # {'name': 'kareem', 'age': 20}
dict_name.update({'status': 'single'})
print(dict_name)    # {'name': 'kareem', 'age': 20, 'status': 'single'}
# we can use: dict_name[new_key] = value_of_new_key. It's the same as: dict_name.update({new_key: value_of_new_key})
print('=' * 70)

# dict_name.keys()  : It returns all keys of dict 'dict_name'

print(dict_name.keys())             # dict_keys(['name', 'age', 'status'])
print(type(dict_name.keys()))       # <class 'dict_keys'>
print('=' * 70)

# dict_name.values(): It returns all values of dict 'dict_name'

print(dict_name.values())           # dict_values(['kareem', 20, 'single'])
print(type(dict_name.values()))     # <class 'dict_values'>
print('=' * 70)

# dict_name.setdefault(key, value)  : It returns the value and updates the dict 'dict_name' with the key.

my_dict = {
    'name'  : 'kareem'
}
print(my_dict)      # {'name': 'kareem'}
print(my_dict.setdefault('name', 'ashraf')) # kareem
print(my_dict)      # {'name': 'kareem'}
print(my_dict.setdefault('age', 20))    # 20
print(my_dict)      # {'name': 'kareem', 'age': 20}
print(my_dict.setdefault('status')) # None
print(my_dict)      # {'name': 'kareem', 'age': 20, 'status': None}
print('=' * 70)

# dict_name.popitem()               : It returns the last item added to the dict and remove it from the dict
my_dict = {
    'name'  : 'kareem'
}
print(my_dict)      # {'name': 'kareem'}
my_dict.update({'age': 20}) # Now, my_dict = {'name': 'kareem', 'age': 20}
print(my_dict)      # {'name': 'kareem', 'age': 20}
print(my_dict.popitem())    # it prints: {'age': 20} and deletes this item from the dict
print(my_dict)      # Now, it prints: {'name': 'kareem'} 
print('=' * 70)

# ITEMS = dict_name.items()         : It stores the items of the dict'dict_name' into a list 'ITEMS'.
my_dict = {
    'name'  : 'kareem'
}
print(my_dict)      # {'name': 'kareem'}
ITEMS = my_dict.items()     # Now, ITEMS is considered a list and it holds the items of my_dict. Each item in a tuple
print(ITEMS)    # dict_items([('name', 'kareem')])
my_dict['age'] = 20     # we updates my_dict with new item
print(ITEMS)    # dict_items([('name', 'kareem'), ('age', 20)]) => this list will be updated anytime my_dict changes
print(type(ITEMS))      # <class 'dict_items'>
print('=' * 70)

# dict_name = dict.fromkeys(A, B)   : A & B are tuples. this method returns a dict with keys in tuple (A). The values of these keys are taken from tuple (B)
A = ('1st key', '2nd key', '3rd key')
B = ('default value')       # it can be: B = 'default value' too
my_dict = dict.fromkeys(A, B)
print(my_dict)      # {'1st key': 'default value', '2nd key': 'default value', '3rd key': 'default value'}
print('-' * 70)