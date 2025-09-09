######################################################################################################################################################
# ------------------------------- User Define Functions -------------------------------
# -------------------------------------------------------------------------------------
# -------------------- Syntax --------------------
# ----- Function Definition -----
# def function_name(Parameter1, Parameter2):
#     Body
# ----- Function Calling -----    
# function_name(Argument1, Argument2)
# 
# Packing & Unpacking =>>>>> Unpacking: Argument == Unpacking: *Argument
# e.g., nums = [1, 2, 3, 4, 5]
# print(nums)   # O/P: [1, 2, 3, 4, 5]
# print(*nums)  # O/P: 1 2 3 4 5                   
# 
# Default Parameters
# def function_name(parameter1='default_value1', parameter2='default_value2, parameter3='default_value3):
#     Body
# NOTE: We can't give defalut value for a parameter and the following one hasn't defulat value
#      All The Following Combinations Are Valid: 
#          - par1=no, par2=no, par3=no                                                                                                                           #
#          - par1=no, par2=no, par3=yes                                                                                                                           #
#          - par1=no, par2=yes, par3=yes                                                                                                                           #
#          - par1=yes, par2=yes, par3=yes
#      All The Fllowing Combinations Are NOT VAlid:
#          - par1=yes, par2=no, par3=no                                                                                                                           #
#          - par1=yes, par2=yes, par3=no                                                                                                                           #
#          - par1=yes, par2=no, par3=yes                                                                                                                           #
#          - par1=no, par2=yes, par3=no     
# Key Word Argument
# def function_name(**parameter):
#     Body
# Now, type of parameter is dict
# 
# Unknown Function 'lambda'   
# Syntax:: some_varilable = lambda arg1, arg2: Body
# - It has no name
# - It's written inline not in block of code
# - It's used for simple functions 
# - Its type is function also                                                                                                                #
######################################################################################################################################################

# Packing & Unpacking
names = ['kareem', 'ashraf', 'mostafa', 'aboelala']
print(names)        # ['kareem', 'ashraf', 'mostafa', 'aboelala']
print(*names)       # kareem ashraf mostafa aboelala

def print_skills(name, *skills): 
    print(f"Hello, {name.capitalize()}! Your skills: ")
    n = 0
    for skill in skills: 
        n += 1
        print(f"- Skill_{n}: {skill}")

print_skills('kareem', 'C++', 'Python', 'Verilog', 'HTML', 'CSS', 'SystemVerilog')

# Default Paramters
def myfunc(name, age = 'unknown', country = 'unknown'):
    print(f"Hello {name.strip().capitalize()}! Your age is {age} and your country is {country.strip().capitalize()}")
myfunc(' kareem       ', 20, '   egypt')
myfunc('kareem', 20)
myfunc('kareem')

# Packing & Unpacking with Key Word Argument
def myfunc1(*skills):
    print(type(skills))     # <class 'tuple'>
    for skill in skills:
        print(skill)
def myfunc2(**skills):
    print(type(skills))     # <class 'dict'>
    for skill, value in skills.items():
        print(f"Skill ({skill}) => {value}")
myskills = {
    'HTML': '90%', 
    'CSS': '30%', 
    'JS': '0%'
}
myfunc1('HTML', 'CSS', 'JS')
myfunc2(HTML='90%', CSS='30%', JS='0%')     
myfunc2(**myskills)     # the same output just like the above line of code
# myfunc2(myskills)       # This will release an error

# Function Recursion

messy_word = 'WWWoooorrllllllldd'

def clean_word(word):
    if len(word) <= 1: return word
    else:
        if word[0] == word[1]: return clean_word(word[1:])
        else: return word[0] + clean_word(word[1:])

print(clean_word(messy_word))



# Lambda Functions
hello = lambda name, age: print(f"Hello {name}, your age: {age}")
hello('Kareem', 20)