# ------------------------------------------------------------------------------------------------------
# --------Set--------
# -------------------
# EX. my_set = {2, 4, 'kareem', True}
# Set items arn't ordered or indexed. It can't be accessed by its index because they're not ordered.
# We can't slice our set beause their items arn't ordered.
# Set has IMMUTABLE data types just like tuples. Lists and Dicts have MUTABLE data types.
# Set items are Unique. A single item can't be repeated. If one is repeated, the interpreter'll neglect it.
# ------------------------------------------------------------------------------------------------------

## Ordering and Indexing : 
my_set = {1, 23, 100.0, 9+1j}
print(my_set) # It may print : {23, 1, (9+1j), 100.0}
print(my_set) # It may print : {100.0, 1, 23, (9+1j)}
print(my_set) # It may print : {1, 100.0, (9+1j), 23}
# print(my_set[0]) # It'll release an Error : 'set' object isn't subscriptable.
### NOTE : 
#### A set can only hold immutable elemnts like tuples, int, str, ....
#### A set can't hold mutable elements like lists or dictionaries.

my_set = {1, 23, 100.0, 9+1j}
# print(my_set[:]) # It'll release an Error : 'set' object isn't subscriptable.

## Unique Items : 
my_set = {'kareem', 'ashraf', 'kareem', True} # The repeatition will be neglicted automaticly.
print(my_set) # Maybe print : {True, 'kareem', 'ashraf}
