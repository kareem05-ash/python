######################################################################################################################################################
# -------------------- Decorators --------------------
# ----------------------------------------------------
# NOTE 1 - Decorators take functions as parameters and execute this function with a specified decoration
# _______________________________________________________________
# -------------------- Syntax ------------------------
# def mydecorator(myfunc):
#   def subfunc():
#       print("Before") 
#       myfunc()
#       print("After")
#   return subfunc
# Option1
#   def myfunc(): print(Hello, World!)
#   mydecorator(myfunc)
# Option2
#   @mydecorator
#   def myfunc(): print(Hello, World!)
#   mydecorator(myfunc)
# Output:: 
#   = Before
#   = Hello, World!
#   = After
# _______________________________________________________________
# NOTE 2 - We can apply more than one decorator on single function
# -------------------- Syntax ------------------------
# @first_decorator
# @second_decorator
# def myfunc(): 
#   Body
# NOTE 3 - If the first and second decorators just print messages before and after myfunc() execution, this is the order of execution
#       1. print before message from the first decorator
#       2. print before message from the second decorator 
#       3. execute myfunc()
#       4. print after message from the second decorator
#       5. pritn after message from the first decorator 
# NOTE 4 - If the order of @first_decorator and @second_decorator lines is reversed, the order of execution will be reversed too
# _______________________________________________________________
# NOTE 5 -                                                                                              # 
######################################################################################################################################################



def Mydecorator(func):
    def sub_func(name):
        print("This is before our function")
        func(name)
        print("This is after our function")
    return sub_func

@Mydecorator
def sayhello(name): print(f"Hello, {name}! Good to see you again")

sayhello('Kareem')


print('*' * 70)


def first_dec(func): 
    def sub_func(NAME):
        print("This message is from the first decorator")
        func(NAME)
        print("Goodbuy from the first decorator")
    return sub_func
def second_dec(func): 
    def sub_func(name):
        print("2nd Decorator")
        func(name)
        print("Goodbuy from 2nd Decorator")
    return sub_func

@second_dec
@first_dec
def myfunc(name): print(f"Hello {name}! Good to see you")

myfunc("Kareem Ashraf")

print('*' * 70)
from time import time 
def speed_test(func):
    def sub_func():
        start = time()  
        func()
        end = time()
        print(f"This function takes {end - start} seconds")
    return sub_func
@speed_test
def myfunc():
    for num in range(20_000): print(num)

myfunc()