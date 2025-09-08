# ------------------------------------------------------------------------------------------------------------------------------
# ---------- While Loop ----------
#              Syntax                     
# while condition:
#   line of code                                              #
#   line of code
#   ....
#   incrementer / condition changer
# else
#   if the condition isn't valid, this line of code will be executed
# The rest of your code                                            #
# ------------------------------------------------------------------------------------------------------------------------------.

x = 0
# It prints: numbers from (0) to (100) with step (10) then break
while True:
    print(x)
    x += 10
    if x == 100: break