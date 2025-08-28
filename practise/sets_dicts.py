# -----------------------------------------------------------------------------------------
# ----- This file is considered a practise on tuple and its methods -----
# [1st] Assignment: create a non-unique list. set another unique-list cnsists of the unique numbers in non-unique list
# [2nd] Assignment: create 2 different sets and concatenate them into cat_set in 3 different ways. print cat_set each way
# [3rd] Assignment: create 2 different sets and clear one of them in a single line then assign the cleared one with the first 2 items in the other one and try to delete the third item in the second list from the first one (which it doesn't exist) without errors
# [4th] Assignment: create a super set and sub set. ensures that all items in the sub set are in the super set
# [5th] Assignment: create a dict with three programing languages as keys each with its progress. print them, each language in a line. add another language then print it out
# -----------------------------------------------------------------------------------------

# [1st] Assignment: create a non-unique list. set another unique-list cnsists of the unique numbers in non-unique list
print(30 * '-', '[1st] Assignment', 30 * '-')
mylist = [1, 2, 3, 3, 4, 5, 1]
print(mylist)
mylist_unique = mylist[:3] + mylist[4:-1]
print(mylist_unique)
mylist_unique.pop(-1)
print(mylist_unique)
# -----------------------------------------------------------------------------------------
# [2nd] Assignment: create 2 different sets and concatenate them into cat_set in 3 different ways. print cat_set each way
print(30 * '-', '[2nd] Assignment', 30 * '-')
first = {1, 2, 3}
second = {'a', 'b', 'c'}
cat = first.union(second)
print(cat)
cat = first | second
print(cat)
first.update(second)
print(first)
# -----------------------------------------------------------------------------------------
# [3rd] Assignment: create 2 different sets and clear one of them in a single line then assign the cleared one with the first 2 items in the other one and try to delete the third item in the second list from the first one (which it doesn't exist) without errors
print(30 * '-', '[3rd] Assignment', 30 * '-')
first = {1, 2, 3}
second = {'a', 'b', 'c'}
print(first)
first.clear()
print(first)
second.remove('c')
first = second
print(first)
# -----------------------------------------------------------------------------------------
# [4th] Assignment: create a super set and sub set. ensures that all items in the sub set are in the super set
print(30 * '-', '[4th] Assignment', 30 * '-')
sub = {1, 2, 3}
supe = {1, 2, 3, 4, 5, 6}
print(sub.issubset(supe))
# -----------------------------------------------------------------------------------------
# [5th] Assignment: create a dict with three programing languages as keys each with its progress. print them, each language in a line. add another language then print it out
print(30 * '-', '[5th] Assignment', 30 * '-')
mydict = {
    'Verilog'   : 90, 
    'C++'       : 80, 
    'Python'    : 40
}
print(f"Python Progress Is: {mydict['Verilog']}%")
print(f"Python Progress Is: {mydict['C++']}%")
print(f"Python Progress Is: {mydict['Python']}%")
mydict['HTML'] = 0
print(f"Python Progress Is: {mydict['HTML']}%")
mydict.update({'CSS': 0})
print(f"Python Progress Is: {mydict['CSS']}%")
# -----------------------------------------------------------------------------------------
