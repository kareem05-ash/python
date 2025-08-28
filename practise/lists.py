# -----------------------------------------------------------------------------------------
# ----- This file is considered a practise on list and its methods -----
# [1st] Assignment: create your list & print needed items in two different ways
# [2nd] Assignment: print items with odd index into a line and with even index into another line
# [3rd] Assignment: Sclicing
# [4th] Assignment: edit the last two items with a default value
# [5th] Assignment: add item at the first position and at the last position
# [6th] Assignment: delete the first item then delete the last item. print out the list after each proccess
# [7th] Assignment: add more items to your list with 2 new lists
# [8th] Assignment: sort items alphabiticaly accending into a line and decending into another line
# [9th] Assignment: print the number of items in your list
# [10th] Assignment: create a super list includes a sub lits at its end. print the first and last item in the sub list
# -----------------------------------------------------------------------------------------

# [1st] Assignment: create your list & print needed items in two different ways
print(30 * '-', '[1st] Assignment', 30 * '-')
mylist = ['kareem', 'ashraf', 'mostafa', 'aboelala', 'ipraheem']
print(mylist[0])
print(mylist[::len(mylist)])    # Note, this returns a list not string
print(mylist[-1])
print(mylist[4])
# -----------------------------------------------------------------------------------------
# [2nd] Assignment: print items with odd index into a line and with even index into another line
print(30 * '-', '[2nd] Assignment', 30 * '-')
print(mylist[1::2]) # odd indexing
print(mylist[::2])  # even indixing
# -----------------------------------------------------------------------------------------
# [3rd] Assignment: Sclicing
print(30 * '-', '[3rd] Assignment', 30 * '-')
print(mylist[1:-1])
print(mylist[-1:-3:-1])
# -----------------------------------------------------------------------------------------
# [4th] Assignment: edit the last two items with a default value
print(30 * '-', '[4th] Assignment', 30 * '-')
print(mylist)
mylist[-1] = "default name"
mylist[-2] = "default name"
print(mylist)
# -----------------------------------------------------------------------------------------
# [5th] Assignment: add item at the first position and at the last position
print(30 * '-', '[5th] Assignment', 30 * '-')
print(mylist)
mylist.insert(0, "Name at the begin")
mylist.append("Name at the end")
print(mylist)
# -----------------------------------------------------------------------------------------
# [6th] Assignment: delete the first item then delete the last item. print out the list after each proccess
print(30 * '-', '[6th] Assignment', 30 * '-')
print(mylist)
mylist.pop(0)
print(mylist)
mylist.pop(-1)
print(mylist)
# -----------------------------------------------------------------------------------------
# [7th] Assignment: add more items to your list with 2 new lists
print(30 * '-', '[7th] Assignment', 30 * '-')
first = ['kareem', 'ashraf', 'mostafa']
second = ['ahmed', 'mohamed', 'ali']
third = ['zzzz', 'zzz', 'zz']
first.extend(second)
first.extend(third)
print(first)
# -----------------------------------------------------------------------------------------
# [8th] Assignment: sort items alphabiticaly accending into a line and decending into another line
print(30 * '-', '[8th] Assignment', 30 * '-')
print(mylist)
accending = sorted(mylist)
deccending = sorted(mylist, reverse=True)
print(accending)
print(deccending)
# -----------------------------------------------------------------------------------------
# [9th] Assignment: print the number of items in your list
print(30 * '-', '[9th] Assignment', 30 * '-')
print(len(mylist))  # this prints the number of items in mylist8
# -----------------------------------------------------------------------------------------
# [10th] Assignment: create a super list includes a sub lits at its end. print the first and last item in the sub list
print(30 * '-', '[10th] Assignment', 30 * '-')
superlist = ['python', 'html', 'css', 'js', ['django', 'flask', 'web']]
print(superlist[-1][0])     # dfango
print(superlist[-1][-1])    # web
# -----------------------------------------------------------------------------------------
