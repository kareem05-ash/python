# ------------------------------------------------------------------------------------------------------------------------------
# ---------- Type Conversion ----------
# -------------------------------------
# int()     : 'int', 'float' data type can be converted to 'int' data type
# float()   : 'int', 'float' data type can be converted to 'float' data type
# complex() : 'int', 'float', 'complex' data type can be converted to 'complex' data type
# str()     : any data type can be converted to 'str' data type
# list()    : 'str', 'list', 'set', 'tuple', dict' can be conberted to 'list' data type NOTE: the converted list from a dict is formed of the keys of the dict
# tuple()   : 'str', 'list', 'set', 'tuple', dict' can be conberted to 'tuple' data type NOTE: the converted tuple from a dict is formed of the keys of the dict
# set()     : 'str', 'list', 'set', 'tuple', dict' can be conberted to 'set' data type NOTE: the converted set from a dict is formed of the keys of the dict
# dict()    : 'list', 'tuple', 'dict' can be converted to 'dict' data type 
#           NOTE: the 'list' to be converted to a 'dict' has to be formed of nested lists. Super list formed of 2-items sub-lists. Each sub-list has [key, value]
#           NOTE: the 'tuple' to be .......................................................... the same
# ------------------------------------------------------------------------------------------------------------------------------

print("---------- convert to int data type ----------")
print(int(10.0))            # 10
print(int(10))              # 10
# print(int(10 + 0j))        # Error
# print(int(10 + 2j))        # Error
# print(int('kareem'))       # Error

print("---------- convert to float data type ----------")
print(float(10.0))          # 10.0
print(float(10))            # 10.0
# print(float(10 + 0j))      # Error
# print(float(10 + 2j))      # Error
# print(float('kareem'))     # Error

print("---------- convert to complex data type ----------")
print(complex(10.0))        # (10+0j)
print(complex(10))          # (10+0j)
print(complex(10 + 0j))     # (10+0j)
print(complex(10 + 2j))     # (10+2j)
# print(complex('kareem'))  # Error

print("---------- convert to str data type ----------")
print(str(10.0))            # 10.0
print(str(10))              # 10
print(str(10 + 0j))         # (10+0j)
print(str(10 + 2j))         # (10+2j)
print(str('kareem'))        # kareem
print(str(True))            # True
print(str(False))           # Flase
print(str([1, 2, 3]))       # [1, 2, 3]
print(str({2, 3, 4}))       # {2, 3, 4}
print(str({1:2, 2:4}))      # {1:2, 2:4}
print(str((1, 2, 3)))       # (1, 2, 3)

print("---------- convert to list data type ----------")
# print(list(10.0))           # Error
# print(list(10))             # Error
# print(list(10 + 0j))        # Error
# print(list(10 + 2j))        # Error
# print(list(True))           # Error
# print(list(False))          # Error
print(list('kareem'))       # ['k', 'a', 'r', 'e', 'e', 'm']
print(list([1, 2, 3]))      # [1, 2, 3]
print(list({2, 3, 4}))      # [2, 3, 4]
print(list({1:2, 2:4}))     # [1, 2]
print(list((1, 2, 3)))      # [1, 2, 3]

print("---------- convert to tuple data type ----------")
# print(tuple(10.0))          # Error
# print(tuple(10))            # Error
# print(tuple(10 + 0j))       # Error
# print(tuple(10 + 2j))       # Error
# print(tuple(True))          # Error
# print(tuple(False))         # Error
print(tuple('kareem'))      # ('k', 'a', 'r', 'e', 'e', 'm')
print(tuple([1, 2, 3]))     # (1, 2, 3)
print(tuple({2, 3, 4}))     # (2, 3, 4)
print(tuple({1:2, 2:4}))    # (1, 2)
print(tuple((1, 2, 3)))     # (1, 2, 3)
print("---------- convert to set data type ----------")
# print(set(10.0))            # Error
# print(set(10))              # Error
# print(set(10 + 0j))         # Error
# print(set(10 + 2j))         # Error
# print(set(True))            # Error
# print(set(False))           # Error
print(set('kareem'))        # {'k', 'a', 'r', 'e', 'e', 'm'}
print(set([1, 2, 3]))       # {1, 2, 3}
print(set({2, 3, 4}))       # {2, 3, 4}
print(set({1:2, 2:4}))      # {1, 2}
print(set((1, 2, 3)))       # {1, 2, 3}

print("---------- convert to set data type ----------")
# print(dict(10.0))                                       # Error
# print(dict(10))                                         # Error
# print(dict(10 + 0j))                                    # Error
# print(dict(10 + 2j))                                    # Error
# print(dict(True))                                       # Error
# print(dict(False))                                      # Error
# print(dict('kareem'))                                   # Error
# print(dict({{'key1', 'val1'}, {'key2', 'val2'}}))       # Error
print(dict([['key1', 'val1'], ['key2', 'val2']]))       # {'key1': 'val1', 'key2': 'val2'}
print(dict((('key1', 'val1'), ('key2', 'val2'))))       # {'key1': 'val1', 'key2': 'val2'}
print(dict({1:2, 2:4}))                                 # {1:2, 2:4}