# -----------------------------------------------------------------------------------------
# ----- This file is considered a practise on numbers and its types -----
# [1st] Assignment: print out all types of numbers
# [2nd] Assignment: print out the img and re part of a complex number. Each in a single line
# [3rd] Assignment: convert an Integer number to a float one and put 10 numbers after '.'
# [4th] Assignment: convert a float number to an integer one and print out its type
# [5th] Assignment: put a valid operator
# -----------------------------------------------------------------------------------------

# [1st] Assignment: print out all types of numbers
print(30 * '-', '[1st] Assignment', 30 * '-')
print(type(2))          # <class 'int'>
print(type(2.0))        # <class 'float'>
print(type(2 + 0j))     # <class 'complex'>
# -----------------------------------------------------------------------------------------
# [2nd] Assignment: print out the img and re part of a complex number. Each in a single line
print(30 * '-', '[2nd] Assignment', 30 * '-')
comp_num = 2 + 3j
print(f"The real part: {comp_num.real}\nThe imaginary part: {comp_num.imag}")
print(type(comp_num.real))      # float
print(type(comp_num.imag))      # float
# -----------------------------------------------------------------------------------------
# [3rd] Assignment: convert an Integer number to a float one and put 10 numbers after '.'
print(30 * '-', '[3rd] Assignment', 30 * '-')
int_num = 20
print(f"{float(int_num): .10f}")
# -----------------------------------------------------------------------------------------
# [4th] Assignment: convert a float number to an integer one and print out its type
print(30 * '-', '[4th] Assignment', 30 * '-')
float_num = 20.322
print(type(float_num))  # <class 'float'>
print(f"{type(int(float_num))}")    # <class 'int'>
# -----------------------------------------------------------------------------------------
# [5th] Assignment: put a valid operator
print(30 * '-', '[5th] Assignment', 30 * '-')
# Qustions
## 100 ? 115 = -15
## 50 ? 30 = 1500
## 21 ? 4 = 1
## 110 ? 11 = 10
## 97 ? 20 = 4
# Soulutions
print(100 - 115)    
print(50 * 30)  
print(21 % 4)   
print(110 // 11)    
print(97 // 20) 
# -----------------------------------------------------------------------------------------
