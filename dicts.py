# -------------------------------------------------------------------------------------------
# ------ Dictionaries -------
# ---------------------------
# [1] Dict items are enclosed in curly braces {}
# [2] Dict items are considered keys. Each key has value
# [3] Dict keys need to be immuatable => (Number, String, Tuple) NOTE: List aren't allowed
# [4] Dict values can be anything
# [5] Dict keys need to be unique. If it's not unique, the last key is the considered
# [6] Dict  isn't ordered. We access it by its key names
# -------------------------------------------------------------------------------------------

# [1] Dict items are enclosed in curly braces {}

dict1 = {
    'name'  : 'Kareem Ashraf', 
    'age'   : 20, 
    'edu'   : 'EECE @ Cairo University', 
    'status': 'single' 
}
print(dict1)

# [2] Dict items are considered keys. Each key has value
# The following dict has 4 different keys ('name', 'age', 'edu', 'status')
# Each key has value. (e.g., 'name' has value: 'Kareem Ashraf')

dict1 = {
    'name'  : 'Kareem Ashraf', 
    'age'   : 20, 
    'edu'   : 'EECE @ Cairo University', 
    'status': 'single' 
}

# [3] Dict keys need to be immuatable => (Number, String, Tuple) NOTE: List aren't allowed

# This is not allowed

# dict2 = {
#     1                       : True, 
#     2                       : 'kareem', 
#     'three'                 : '20 yo ', 
#     4                       : ['one', 'two', 'three'], 
#     ['mh list', 'items']    : 'kareem'
# }
7# This is allowed

dict3 = {
    1         : True, 
    2         : 'kareem', 
    'three'   : '20 yo ', 
    4         : ['one', 'two', 'three']
}
print(dict3)

# [4] Dict values can be anything (lists are allowed)

dict4 = {
    1         : True, 
    2         : 'kareem', 
    'three'   : '20 yo ', 
    4         : ['one', 'two', 'three']
}
print(dict4)

# [5] Dict keys need to be unique. If it's not unique, the last key is the considered

dict5 = {
    1   : 'kareem', 
    2   : 20,       # this value will not considered the value of key(2)
    3   : True, 
    2   : 30        # this value to be considered the value of key(2)
}
print(dict5)    # {1: 'kareem', 2: 30, 3: True}

# [6] Dict  isn't ordered. We access it by its key names

super_dict = {
    1       : {
        'name'  : 'kareem', 
        'age'   : 20, 
        'status': 'single'
    }, 
    'two'   : {
        'name'  : 'ashraf', 
        'age'   : 57, 
        'status': 'married'
    }, 
    3       : {
        'name'  : 'mostafa', 
        'age'   : 110, 
        'status': 'dead'
    }, 
    4       : ['he', 'she', 'they', 'we', True]
}

print(super_dict)                   # this prints the whole dictionary
print(super_dict[3])                # this prints the value of key(3) which is an inner dictionary: {'name'  : 'mostafa', 'age'   : 110, 'status': 'dead'} 
print(super_dict[4])                # this prints the value of key(4) which is a list: ['he', 'she', 'they', 'we', True]
print(super_dict[4][3])             # this prints the value of index(3) in the list of key(4) which is: we
print(super_dict[1]['name'])        # this prints the value of key('name') in the dict of key(1) which is: kareem
print(super_dict['two']['status'])  # this prints the value of key('status') in the dict of key('two') which is: married