# -------------------------------------------------------------------------------------------
# ------Set Methods-------
# ------------------------
# set_name.clear() => it clears the set.
# set_name.union(set1, set2, ....) => it returns set1 & set2 in one set.
# set_name.add(item) => it adds the item (item) ot your set. NOTE : .add() takes only one argument.
# set_name.copy() => it returns a copy from your set into another variable.
# set_name.remove(item) => it removes the item (item) from your set.
#          NOTE if item isn't in your set, it'll release error.
# set_name.discard(item) => it removes the item (item) from your set.
#          NOTE if item isn't in your set, it'll do nothing with no errors.
# set_name.pop() => it returns and removes a random element from your set.
# set_name.update(set or list) => it updates your set with the included set or list.
#          NOTE the repeatition will discardid automaticly.
# set_name.difference(set) => it returns the items in your set 'set_name' & not in set 'set'
#          NOTE a.difference(b) is the same as a - b
# set_name.difference_update(set) => it's the same as diifference(set) but, it updates your set 'set_name' with the reurned values
# set_name.intersection(set) => it returns the common items between your set 'set_name' and set 'set'
#          NOTE a.intersection is the same as a & b
# set_name.intersection_update(set) => it's the same as intersection(set) but, it updates your set 'set_name' with the returned values
# set_name.symmetric_difference(set) => it returns the items arn't common between your set 'set_name' and set 'set'
#          NOTE a.system_difference(b) is the same as a ^ b
# set_name.symmetric_difference_update(set) => it's the same as symmetric_difference(set) but, it updates your set 'set_name' with the returned values
# set_name.issuperset(set) => returns 'Ture' if all values of 'set' are in 'set_name' == 'set_name' is a superset for 'set', returns 'False' if not.
# set_name.issubset(set) => returns 'True' if all vaules of 'set_name' are in 'set' == set_name' is a subset from 'set', return 'False' if not.
# set_name.isdisjoint(set) => returns 'True' if there is no such element is common between 'set_name' ans 'set'
# -------------------------------------------------------------------------------------------

## set_name.clear() : clears the set from its elements
print("set_name.clear() : clears the set from its elements")
my_set = {1, 2, 3, 4, 5}
print(my_set) # {1, 2, 3, 4, 5}
my_set.clear()
print(my_set) # set()

## set_name.union(set or list) : unions the set_name with the specified set or list
print("set_name.union(set or list) : unions the set_name with the specified set or list")
my_set = {1, 2, 3, 4, 5, True, False, 3+3j}
print(my_set) # it may print {True, False, 1, 2, 3, 4, 5, 3+3j}
print(my_set | {'a', 'b'}) # it may print {True, False, 1, 2, 3, 4, 5, 3+3j, 'a', 'b'}
print(my_set.union(['a', 'b'])) # it may print {True, False, 1, 2, 3, 4, 5, 3+3j, 'a', 'b'}
set1 = {1, 2, 3, 4, 5}
set2 = {'kareem', 'ashraf', True, (3+2j)}
print(set1.union(set2)) # it may print : {1, 2, 3, 4, 5, (3+2j), 'ashraf', 'kareem'}

## set_name.add(item) : add item to the set (set_name) 
### NOTE : .add() takes only one argument
print("set_name.add(item) : add item to the set (set_name)")
set1 = {1, 2, 3, 4, 5}
print(set1) # it may print : {1, 2, 3, 4, 5}
set1.add(6)
print(set1) # it may print : {1, 2, 3, 4, 5, 6}
# set1.add(6, 7) : TypeError
# set1.add([7, 8, 9]) : TypeError

## set_name.copy() : it makes a copy from set_name
print("set_name.copy() : it makes a copy from set_name")
set1 = {1, 2, 3, 4, 5}
set2 = set1.copy()
print(set1) # {1, 2, 3, 4, 5}
print(set2) # {1, 2, 3, 4, 5}
set1.add('kareem')
print(set1) # {1, 2, 3, 4, 5, 'kareem'}
print(set2) # {1, 2, 3, 4, 5}

## set_name.remove(item) : if item is in the set 'set_name', it will delete this item from this set
###                         if item isn't in the set 'set_name', it will release an error
print("set_name.remove(item) : if item is in the set 'set_name', it will delete this item from this set")
set1 = {1, 2, 3, 4, 5}
set1.remove(3) # removes '3' from the set
print(set1) # it prints : {1, 2, 4, 5}
# set1.remove(12) # KeyError : 12 isn't in the set

## set_name.discard(item) : the same as .remove(), but if item isn't in the set, it'll do nothing
print("set_name.discard(item) : the same as .remove(), but if item isn't in the set, it'll do nothing")
set1 = {1, 2, 3, 4, 5}
set1.discard(3) # removes '3' from the set
print(set1) # it prints : {1, 2, 4, 5}
set1.discard(12) # ti'll do nothing because '12' isn't in the set
print(set1) # it may prints : {1, 2, 4, 5}

## set_name.pop() : it returns and removes a random element from the set
print("set_name.pop() : it returns and removes a random element from the set")
set1 = {True, 1, 2, 3, 4, 5}
print(set1.pop()) # it will print a random element from the set then remove it from the set : typically teh first element

## set_name.update(set or list) : it's the same as .union(set). The main difference is that it can take a list as an argument
print("set_name.update(set or list) : it's the same as .union(set). The main difference is that it can take a list as an argument")
my_set = {1, 2, 3, 4, 5}
print(my_set) # it may print : {1, 2, 3, 4, 5}
my_set.update([6, 7, 8, 9])
print(my_set) # it may print : {1, 2, 3, 4, 5, 6, 7, 8, 9}

## set_name.difference(set) : returns the items in your set 'set_name' which isn't in set 'set'
print("set_name.difference(set) : returns the items in your set 'set_name' which isn't in set 'set'")
my_set = {'kareem', 3, 'x', True}
her_set = {'kareem', True, False, 23}
print(my_set.difference(her_set)) # it may print : {3, 'x'}
print(my_set) # {'kareem', 3, 'x', True}
print(her_set) # {'kareem', True, False, 23}
her_set = {'kareem', 3, 'x', True}
print(my_set - her_set) # the same as : my_set.difference(her_set)
print(my_set) # {'kareem', 3, 'x', True}
print(her_set) # {'kareem', 3, 'x', True}

## set_name.difference_update(set) : returns the items in your set 'set_name' which isn't in set 'set'. Then updates your set 'set_name'
print("set_name.difference_update(set) : returns the items in your set 'set_name' which isn't in set 'set'. Then updates your set 'set_name'")
my_set = {'kareem', 3, 'x', True}
her_set = {'kareem', True, False, 23}
print(my_set) # {'kareem', 3, 'x', True}
print(her_set) # {'kareem', True, False, 23}
my_set.difference_update(her_set) 
print(my_set) # {3, 'x'}
print(her_set) # {'kareem', True, False, 23}

## set_name.intersection(set) : 
my_set = {'kareem', 3, 'x', True}
her_set = {'kareem', True, False, 23}
my_set.intersection(her_set)
print(my_set) # {3, 'x'}
print(her_set) # {'kareem', True, False, 23}


## set_name.intersection_update(set) :  



## set_name.symmetric_difference(set) : 



## set_name.symmetric_difference_update(set) : 



## set_name.issuperset(set) : 



## set_name.issubset(set) : 



## set_name.isdisjoint(set) : 



