# ------------------------------------------------------------------------------------------------------
# --------List Methods--------
# ----------------------------
# list_name.append(item) => it inserts the item at the end of your list
# list_name.extend(list) => it inserts the list at the end of your list
# list_name.remove(item) => it removes the item from your list only once from the start
# list_name.sort(reverse = (True or False)) => it sorts your list which is formed from numbers only
#       if(reverse = False) the sortion will be from the smaller
#       elif(revese = True) the sortion will be from the greater
#       if(reverse isn't included == list_name.sort()) the sortion will be from the smaller by default
# list_name.reverse() => it reverses the order of items in your list.
#       Note : your list here, can be formed from different data types
# list_name.clear() => it clears your list. it returns [] == empty list.
# list_name.copy() => it returns a copy of your list.
# list_name.count(item) => it returns the number of repeatition of the item in your list
# list_name.index(item) => it returns the index of the item in your list
# list_name.insert(index, item) => it inserts the item just before the index (index)
# list_name.pop(index) => it returns the item with index (index) and remove it from your list.
# ------------------------------------------------------------------------------------------------------

# NOTE :
# we can't apply the list methode in print() method.
# we can only apply list method first in seperate line, then we can display the list : print(my_list)
## EX.
### we can't do this : 
###     print(mylist.append(item))
### we can only do this :
###     mylist.append(item)
###     print(mylist)

## list_name.append(item) : 
my_list = [1, 2, 3, 'four', 'five', True, 23.0, (3+23j)]
print(my_list) ### prints the whole list : [1, 2, 3, 'four', 'five', True, 23.0, (3+23j)]
my_list.append("kareem")
print(my_list) ### prints the whole list : [1, 2, 3, 'four', 'five', True, 23.0, (3+23j), 'kareem']
first_list = [1, 2, 3, 4 ,5]
second_list = ['one', 'two', 'three', 'four', 'five']
first_list.append(second_list)
print(first_list) ### prints : [1, 2, 3, 4, 5, ['one', 'two', 'three', 'four', 'five']]
                           ### here, the second_list is considered as a single item in the first_list
### NOTE : we can't do this : 
####            print(mylist.append(item))
####     : we can only do this :
####            mylist.append(item)
####            print(mylist)
print(first_list.index(5)) # 4
print(first_list[5][2]) # 'three'
print(type(first_list[5])) # <class 'list'>

## list_name.extend(ilst) : 
my_list = ['kareem', 'ashraf', 'mostafa']
her_list = ['k', 'a', 'm']
### NOTE : we can't do this : 
####            print(mylist.extend(item))
####     : we can only do this :
####            mylist.extend(item)
####            print(mylist)
my_list.extend(her_list)
print(my_list) # now, my_list is extended to a list with six items : ['kareem', 'ashraf', 'mostafa', 'k', 'a', 'm']
print(my_list.index(my_list[-1]) + 1) # it prints the number of items : 6
print(my_list[4]) # 'a'

## list_name.remove(item) : 
my_list = ['kareem', 'ashraf', 'mostafa', 'ashraf', 'aboelala', 'ashraf']
my_list.remove('ashraf') # it removes the first appearence of 'ashraf'.
print(my_list) # ['kareem', 'mostafa', 'ashraf', 'aboelala', 'ashraf'] 

## list_name.sort() : 
nums = [32, 534, 3, 35, -2, 3, 0]
nums.sort() # sort them from the smallest one | it's the same as : nums.sort(reverse=False)
print(nums) # [-2, 0, 3, 3, 32, 35, 534]
nums = [32, 534, 3, 35, -2, 3, 0]
nums.sort(reverse=True) # sort them from the greatest one 
print(nums) # [534, 35, 32, 3, 3, 0, -2]
mixed = [34, 2, 12, 4, 'three', 'four']
# mixed.sort() # this will release a TypeError

## list_name.reverse : 
mixed = [34, 2, 12, 4, 'three', 'four']
print(mixed) # [34, 2, 12, 4, 'three', 'four']
mixed.reverse()
print(mixed) # ['four', 'three', 4, 12, 2, 34]

## list_name.clear() :
mixed = [34, 2, 12, 4, 'three', 'four']
mixed.clear() # it clears your list
print(mixed) # it prints : []

## list_name.copy() : 
mixed = [34, 2, 12, 4, 'three', 'four']
copied_list = mixed.copy()
print(mixed) # [34, 2, 12, 4, 'three', 'four']
print(copied_list) # [34, 2, 12, 4, 'three', 'four']
mixed.append(3)
print(mixed) # [34, 2, 12, 4, 'three', 'four', 5]
print(copied_list) # [34, 2, 12, 4, 'three', 'four']
### NOTE : 
#### .copy() just take a copy from your list into another lication.
#### the copied_list doesn't change if you change your list.

## list_name.count(item) : 
my_list = ['kareem', 'ashraf', 'mostafa', 'ashraf', 'aboelala', 'ashraf']
print(my_list.count('ashraf')) # 3

## list_name.index(item) :  
my_list = ['kareem', 'ashraf', 'mostafa', 'ashraf', 'aboelala', 'ashraf']
print(my_list.index('ashraf')) # prints : 1. which is the index of first appearence of 'ashraf' in the list.
print(my_list[2: ].index('ashraf')) # prints : 1. 'ashraf' appears for the first time at the index(1) 
#                                       in the sub-list : ['mostafa', 'ashraf', 'aboelala', 'ashraf']

## list_name.insert(item, index) : 
her_list = [1, 2, 3, 4, 5]
her_list.insert(0, 'kareem') # it inserts "kareem" at index 0 (at the start of the list)
print(her_list) # prints : ['kareem', 1, 2, 3, 4, 5] 
her_list.insert(1, 'ashraf')
print(her_list) # prints : ['kareem', 'ashraf', 1, 2, 3, 4, 5]
her_list.insert(10, 'kemo') # even the list doesn't have 9 items (the greatest index was 6), 'kemo' was inserted at the end of the list(index 7)
print(her_list) 
print(her_list.index(her_list[-1]) + 1) # prints the no. of items in the list : 8
print(her_list[7]) # prints : 'kemo'

## list_name.pop(index) :  
her_list = [1, 2, 3, 4, 5]
print(her_list.pop(1)) # it returns her_list[1] : 2. And deletes it from the list.
print(her_list) # after pop() : [1, 3, 4, 5]
my_list = ['kareem', 'ashraf', 'mostafa', 'kareem']
print(f"The repeated item : {my_list.pop(-1)}")
print(f"after pop() operation : {my_list}") # prints : after pop() operation : ['kareem', 'ashraf', 'mostafa']