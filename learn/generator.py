######################################################################################################################################################
# -------------------- Generators --------------------
# ----------------------------------------------------
# NOTE 1: It's a function with 'yield' keyword instead of 'return'
# NOTE 2: It supports iterations and returns iterator by calling yield
# NOTE 3: It can have one or more yield
# NOTE 4: We can use next() to resume the iteration from the past yield
# NOTE 5: When it's called, it doesn't start automatically. It just, give you the control                                                          #
######################################################################################################################################################

def mygen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
print(80 * '*')
print(type(mygen))          # <calss 'function'>
print(type(mygen()))        # <calss 'generator'>

var1 = mygen()              # It does nothing. Just, stores an iterator of our generator in var1
var2 = mygen()              # It does nothing. Just, stores an iterator of our generator in var2
var3 = mygen()              # It does nothing. Just, stores an iterator of our generator in var3
var4 = mygen()              # It does nothing. Just, stores an iterator of our generator in var4

print(var1)                 # <generator object mygen at 0x00.....>
print(next(var1))           # 1
print(next(var1))           # 2
print(next(var1))           # 3
print(next(var1))           # 4
print(next(var1))           # 5

print(var2)                 # <generator object mygen at 0x00.....>
print(next(var2))           # 1
print(next(var2))           # 2
print(next(var2))           # 3
print(next(var2))           # 4
print(next(var2))           # 5

print("This is from var2")
for item in var2: print(item)           # It does nothing as, the iterator has done
print("This is from var3")
for item in var3: print(item, end=" ")  # It prints: 1 2 3 4 5

print(next(var4))           # 1
print(next(var4))           # 2
print(next(var4))           # 3

for item in var4: print(item, end=" ")  # It prints: 4 5 | it loops from the last yield (3)