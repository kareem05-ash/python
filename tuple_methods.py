# -------------------------------------------------------------------------------------------------------------
# ------Tuple------
# -----------------
# EX. my_tuple = (1, 2, 3, 4, 5, 'kareem', True)
# You can remove the parentheses : ex. my_typle = 1, 2, 3, 4, 5, 'kareem', False
# Tuples are zero-base indexed. Its items can be accessed by their indecies.
# Tuple items are IMMUTABLE. We can't add, delete or assign.
# Tuple items arn't unique. An item can be repeated in the same tuple.
# Tuples can have different data types.
# Operators used in lists and strings are available in tuples.
# ------Tuple Methods------
# -------------------------
# tuple_name.count(item) => it counts and return the number of repeatition of the sepecified item(item).
# tuple_name.index(item) => it returns the index of the specified item (item).
# -------------------------------------------------------------------------------------------------------------

## Syntax : 
first_tuple = (1, 2, 3, 4 ,5)
second_tuple = 1, 2, 3, 4, 5
print(first_tuple) # prints the whole tuple : (1, 2, 3, 4 ,5)
print(second_tuple) # prints the whole tuple : (1, 2, 3, 4 ,5)
print(type(first_tuple)) # <class 'tuple'>
print(type(second_tuple)) # <class 'tuple'> 

## Indexing : 
my_tuple = 'kareem', 'ashraf', 1, 2, 3, 4, 5, True, False, (4+3j)
print(my_tuple) # prints the whole tuple : ('kareem', 'ashraf', 1, 2, 3, 4, 5, True, False, (4+3j))
print(my_tuple[0]) # first item : 'kareem'
print(my_tuple[-1]) # last item : (4+3j)
print(my_tuple[ :3]) # prints the first 3 items : ('kareem', 'ashraf', 1)
print(my_tuple[::2]) # prints the whole tuple with step (2) : ('kareem', 1, 3, 5, False)

## Immutable proof : 
my_tuple = 'kareem', 'ashraf', 1, 2, 3, 4, 5, True, False, (4+3j)
### my_tuple[0] = 'ashraf' # this will release a TypeError : 'tuple' doesn't support item assignment.

## Tuple with One Element : 
my_tuple = ("kareem")
first_tuple = "kareem" 
print(type(my_tuple)) # it prints <class 'str'> not <class 'tuple'>
print(type(first_tuple)) # it prints <class 'str'> not <class 'tuple'>
my_tuple = ("kareem", )
first_tuple = "kareem",  
print(type(my_tuple)) # it prints <class 'tuple'>
print(type(first_tuple)) # it prints <class 'tuple'>
print(len(first_tuple)) # it prints the number of elements in the tuple : 1
print(len(my_tuple)) # it prints the number of elements in the tuple : 1

## Tuple Concatination : 
first_tuple = 'kareem', 'ashraf', True, 3-4j
second_tuple = 1, 2, 3, 4, 5
cat_tuple = first_tuple + second_tuple
print(cat_tuple) # it prints the reseult : ('kareem', 'ashraf', True, (3-4j), 1, 2, 3, 4, 5)
# cat_tuple2 = first_tuple + 1, 2, 3, 4, 5 # it'll release an Error : can't concatinate tuple to int.
cat_tuple2 = first_tuple + (1, 2, 3, 4, 5)
print(cat_tuple2) # it prints the reseult : ('kareem', 'ashraf', True, (3-4j), 1, 2, 3, 4, 5)

## Repeat (*) {tuple, list, string} : it repeats the {tuple, list, string} with specefied number.
my_tuple = 'a', 'b'
my_list = ['A', 'B']
my_string = 'AB'
print(my_tuple * 10) # ('a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'........, 'a', 'b') 10 times.
print(my_list * 10) # ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'........., 'A', 'B'] 10 times.
print(my_string * 10) # ABABABABABABABABABAB                                                          10 times.

## tuple_name.count(item) : 
my_tuple = 'kareem', 'ashraf', 'kareem' 
print(my_tuple.count('kareem')) # it prints : (2). Which means that 'kareem' has been repeated 2 times in your tuple.
print(my_tuple.count(True)) # it prints : (0). Which means that True isn't in your tuple.

## tuple_name.index(item) : 
my_tuple = 'kareem', 'ashraf', 1, 2, 3, 4, 5, True, False, (4+3j)
print(my_tuple.index('kareem')) # prints : (0). Which means that 'kareem' is the first elements in your tuple.
print(my_tuple.index(my_tuple[-1])) # prints : (9). This is the index of the last element in your tuple.
print(my_tuple.index(my_tuple[-1]) + 1) # prints : (10). Which represents the no. of elements in your tuple.
print(len(my_tuple)) # same as the previous line. prints : (10). Which represents the no. of elements in your tuple.

## Tuple Destruction : 
tuple1 = 1, 2, 3, 4
# a, b, c = tuple1 # it'll release an Error : expected 3, got 4
a, b, c, _= tuple1
print(a) # 1
print(b) # 2
print(c) # 3