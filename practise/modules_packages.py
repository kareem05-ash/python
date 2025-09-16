# This File Contains 4 Assignemnts On Modules & Pakcages In Python

####################################################################################################
# Assignment_1
print('*' * 20, '# Assignment_1', '*' * 20)
import random
from random import randint
even, odd = 1, 2
while even%2 != 0: even = randint(2, 10)
while odd%2  == 0: odd  = randint(1, 9)
print(f"Random Number Between 10 And 50 => {randint(10, 50)}")
print(f"Random Even Number Between 2 And 10 = {even}")
print(f"Random Odd Number Between 1 And 9 = {odd}")
print("\nrandom module methods: ")
print(dir(random))
####################################################################################################
# Assignment_2
print('*' * 20, '# Assignment_2', '*' * 20)
import sys
sys.path.append(r"F:\GitHub\python\modules")
import my_mod as m
m.say_hello('Kareem')
m.say_welcome('Kareem')
