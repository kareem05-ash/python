######################################################################################################################################################
# ******************** Iterable vs. Iterator ********************
# ***************************************************************
# --------------------        Iterable       --------------------
# [1] It's an object contains a data which can be iterated
# [2] e.g., list, tuple, str, set, dict
# --------------------        Iterator       --------------------
# [1] It's an object used to iterate over our iterable
# [2] We can generate an iterator from any iterable by using iter(MyIterable) method
# [3] For loops generates an iterator automatic from your iterable to iterate over the iterable                                                                                                                                                  #
######################################################################################################################################################

mylist = [1, 2, 3, 4, 5]
print(type(mylist))         # <class 'list'>
print(type(iter(mylist)))   # <class 'list_iterator'>
print(mylist)               # [1, 2, 3, 4, 5]
print(iter(mylist))         # <list_iterator object at 0x0000021C122705E0>
for num in mylist: print(num, end=' ')          # 1 2 3 4 5
print()
for num in iter(mylist): print(num, end=' ')    # 1 2 3 4 5 
print()

my_iter = iter(mylist)

print(next(my_iter))    # 1
print(next(my_iter))    # 2
print(next(my_iter))    # 3
print(next(my_iter))    # 4
print(next(my_iter))    # 5
# print(next(my_iter))    # Error because there's no more items in the iterable