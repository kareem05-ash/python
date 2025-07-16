# --------------------------------------------------------------------------------------------------
# -------Numbers-------
# Integer => ex. [0, 2, 34, -100, 343]
# Float => ex. [2.23, -23.33, 0.324]
# Complex => ex. [3+4j, 5.3+34j, -3+5j, 23-2j]
# --------------------------------------------------------------------------------------------------


## Integer :: 
print(type(233))
print(type(-233))
print(type(0))
print(type(-1000))

## Float ::
print(type(0.32))
print(type(-0.32))
print(type(10.32))
print(type(143.55))
print(type(-10000.0))

## Complex :: 
print(type(-3+34j))
print(type(3-34j))
print(type(14j))
print(type(34+0j))
print(type(-3-3j))

## converting number types 

### Integer => Float or Complex (allowed)
num = 234
print(float(num)) # It'll print 234.0
print(complex(num)) # It'll print 234+0j

### Float => Integer or Complex (allowed)
num = 345.00
print(int(num)) # It'll print 345
print(complex(num)) # It'll print 345+0j

### Complex => Integer or Float (DISAllowed)
num = 22+8j
# print(int(num)) # type error
# print(float(num)) # type error
print(str(num)) # It'll print 22+8j. Keep in your mind that this is string not complex
