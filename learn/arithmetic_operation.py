# ---------------------------------------------------------------------------------------------------
# --------Arithmetic Operations----------
# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Modulus (%)
# Exponent (**)
# Floor Division (//)
# ---------------------------------------------------------------------------------------------------

## Addition (+) : common addition operation 
print("## Addition (+) : ")
print(2 + 3) # 5
print(-2 + 3) # 1
print(23 + -33) # -10
print(23.4 + 23) # 26.4
print(type(23.4 + 23)) # <class 'float'>
print(type(23 + -33)) # <class 'int'>

## Subtraction (-) : common subtractoin operation 
print("## Subtraction (-) : ")
print(2 - 3) # -1
print(-2 - 3) # -5
print(23 - -33) # 56
print(23.4 - 23) # 0.4
print(type(23.4 - 23)) # <class 'float'>
print(type(23 - -33)) # <class 'int'>

## Multiplication (*) : common multiplication operation 
print("## Multiplication (*) : ")
print(2*4) # 8
print(23*10) # 230
print(-2 * 34) # -68
print(3 + 3 *23) # 72
print((3 + 3) *23) # 138
print(3*2.4) # 7.2
print(type(3*2.4)) # <class 'float'>
print(type(-2 * 34)) # <class 'int'>

## Division (/) : common division operation type(float)
print("## Division (/) : ")
print(12/6) # 2.0
print(12/5) # 2.4
print(-24/2) # -12.0
print(100/-10) # -10.0
print(type(234/23)) # <class 'float'>

## Modulus (%) : returns division remainder (R) 
print("## Modulus (%) : ")
print(12%3) # 0
print(24%5) # 4
print(12.3%6) # 0.300000000000007
print(type(24%5)) # <class 'int'>
print(type(12.3%6)) # <class 'float'>

## Exponent (**) : common exponent operation (2**3 === 2^3)
print("## Exponent (*) : ")
print(2**5) # 32 (2^5)
print(3**3) # 27
print(5**4) # 625
print(type(3**5)) # <class 'int'>

## Floor Division (//) : just like common division operation but it floors the quationt
print(120//20) # 6
print(12.4//4) # 3.0
print(110//20) # 5
print(type(120//20)) # <class 'int'>
print(type(12.4//4)) # <class 'float'>
print(type(110//20)) # <class 'int'>