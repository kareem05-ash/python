# ------------------------------------------------------------------------------------------------------------------------------
# ---------- Boolean and its Operator ----------
# ---------------  True Values   ---------------
# True, any number except(0), any non-empty data type. 
#       e.g., | True, 12, 4.9, 3+4j, "kareem", [2, 32, 3], [False], {1:3, False:32}, {2, 3, 4}, (False, True, 23, 4) .......and so on|
# ---------------  False Values  ---------------
# False, 0, 0.0, 0+0j, None, and empty data.
#       e.g., | False, 0, 0.0. 0+0j, {}, [], () |
# ----------   Comparison Operator   -----------
# ==: print(x == y), If 'x' is the same as 'y', it prints True. Else, it prints False NOTE: 100 === 100.0 === 100 + 0j
# ==: print(x != y), If 'x' isn't the same as 'y', it prints True. Else, it prints False
# < : print(x < y), If 'x' is less than 'y', it prints True. Else, it prints False
# > : print(x > y), If 'x' is greater than 'y', it prints True. Else, it prints False
# <=: print(x <= y), If 'x' is less than or equal 's', it prints True. Else, it prints False
# >=: print(x >= y), If 'x' is greater than or equal 's', it prints True. Else, it prints False
# ----------     Logical Operator    -----------
# and: ensures all conditions are valid. if only one of conditions aren't valid, the returned bool value will be (False) 
# or : ensures at least one of conditions are valid. if only one of conditions are valid, the returned boll value will be (True)
# not: reverses the logic. if the condition is True, it will reverse it to False and vice verse.
# ----------   Assignment Operator   -----------
# =     : Assignment
# +=    : increment the self variable
# -=    : decrement the self variable
# *=    : mulriply the self variable
# /=    : divide the self variable by a divisor
# **=   : increase the self variable to a power
# %=    : taking modulus of the self variable
# //=   : divide(int) the self variable by a divisor
# ------------------------------------------------------------------------------------------------------------------------------


print("---------------  True Values   ---------------")
print(bool(0+3J)) 
print(bool([False]))
print(bool({1:3, False:23}))
print(bool((False, True, 23, [32])))

print("---------------  False Values  ---------------")
print(bool(0))
print(bool(0.0))
print(bool(0+0j))
print(bool(None))
print(bool([]))
print(bool(()))
print(bool({}))

print("----------   Comparison Operator   -----------")
name = "kareem"
age = 20
country = "egypt"
print(name == "kareem")     # True
print(100 == 100.0)         # True
print(100 != 100 + 2j)      # False
print(age > 18)             # True
print(age < 18)             # False
print(country != "egypt")   # False
print(age >= 20)            # True
print(age <= 20)            # True

print("----------     Logical Operator    -----------")
print(100 <= 120 and " ".isspace() and 'kareem' != 'ashraf')        # True, all conditions are valid
print(100 <= 120 and " ".isspace() and 'kareem' == 'ashraf')        # False, only one of the conditions aren't valid
print(100 <= 120 and "".isspace() and 'kareem' == 'ashraf')         # False, only one of the conditions are valid
print(100 <= 120 or " ".isspace() or 'kareem' != 'ashraf')          # True, all conditions are valid
print(100 <= 120 or " ".isspace() or 'kareem' == 'ashraf')          # True, only one of the conditions aren't valid
print(100 <= 120 or "".isspace() or 'kareem' == 'ashraf')           # True, only one of the conditions are valid
print(100 == 120 or "".isspace() or 'kareem' == 'ashraf')           # False, none is valid

print("----------   Assignment Operator   -----------")
x = 20
x //= 10
print(x)
x = 11
x %= 2              # x = 1
print(x)
print(type(x))      # <class 'int'>
x = 3
x **= 3             # x = 27
print(x)
print(type(x))      # <class 'int'>
