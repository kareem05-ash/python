'''This module is for Assignments on zip(), PIL, docement vs comment, and pylint'''

# Assignment_1
print('*' * 20, 'Assignment_1', '*' * 20)

my_list = ['K', 'R', 'E', 1, 2, 3]
my_tuple = ('A', 'E', 'M')
my_data = []
for data in zip(my_list, my_tuple):
    if data ==  (my_list[0], my_tuple[0]):
        MY_STRING = my_list[0] + my_tuple[0].lower()
    else:
        MY_STRING += (data[0] + data[1]).lower()
print(MY_STRING)

# Assignment_2
print('*' * 20, 'Assignment_2', '*' * 20)

my_list1 = ['K', 'A', 'R', 'E', 'E', 'M', 1, 2]
my_tuple1 = ('K', 'R', 'E', 1, 2, 'E', 'E', 'M')
my_tuple2 = ('A', 'E', 'M', 1, 2, 'E', 'E', 'M')
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple1, my_tuple2):
    if item1 == my_list1[0]:
        MY_STRING = my_list1[0]
    elif item1 == my_list1[my_list1.index(my_list1[-1]) - 1]:
        break
    else:
        MY_STRING += item1.lower()

print(MY_STRING)

# Assignment_3
print('*' * 20, 'Assignment_3', '*' * 20)

def say_hello_to(name):
    '''
    This function says hello to someone
    paramter(name) => person name
    function to say Hello to anyone
    '''
    return f"Hello, {name}"

print(say_hello_to("Kareem"))
print(say_hello_to.__doc__)

# Assignment_4
print('*' * 20, 'Assignment_4', '*' * 20)

my_friends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_people) -> list:
    '''
    This function says hello to names in a list
    Paramter(some_people) => names list
    '''
    for someone in some_people:
        print(f"Hello {someone}")

say_hello(my_friends)
