######################################################################################################################################################
# ******************** Error Handling & Exceptions ********************
# *********************************************************************
# ---------------------------- Exceptions -----------------------------
# ---------------------------------------------------------------------
# [1] - Exceptions terminates your code. The rest of the code after the exception will not be executed
# [2] - Exceptions have many types e.g., (SyntaxError, TypeError, KeyErrro, etc...)
# [3] - You can check Exceptions list at [https://docs.python.org/3/library/exceptions.html]
# [4] - To raise your own Exception, use 'raise' keyword. e.g., if True: raise Exception("Your exception message")
# [5] - You can raise any specific Exception from the Exceptinos list. e.g., if True: raise SyntaxError("Your exception message")
# ------------------- Try | Except | Else | Finally -------------------
# ---------------------------------------------------------------------
# [1] - try       => Tests your code and hunts errors
# [2] - except    => If errors are tracked, the block of code after except will be executed
# [3] - else      => If there are no errors, the block of code after lese will be executed
# [4] - finally   => Its block of code will be executed whatevet happended
# --------------------------- Type Hinting ----------------------------
# ---------------------------------------------------------------------
# NOTE - It's used just for small scale documentation in your code
# NOTE - It doesn't restrict anything to your code
# NOTE - We can think of it as an advice
# NOTE - Usually, it's used for parameters type in defining functions
# e.g., def sayhello(name) -> str: print(f"Hello, {name})
#       The previous function takes (name) as a parameter. It's suggensted to be a string.
#       What if name isn't a string, let say it's an interger, the function will be executed normally and the output will be: e.g., Hello, 10                                                                             # 
######################################################################################################################################################

# ---------------------------- Exceptions -----------------------------
num = int(input("Enter the number: ").strip())
if num < 0:
    raise ValueError(f"Value of num({num}) is less than zero")
else:
    print(f"Value of num({num}) is great!")

# ------------------- Try | Except | Else | Finally -------------------

try:
    print(int("Kareem"))
    print(10 / 0)   # this will release an error (ZeroDivisionError)
    print("this message is from try block. It'll NOT be printed")
except ZeroDivisionError:
    print("This is ZeroDivisionError")
except ValueError:
    print("There is ValueError. Be carefull!")
except: # any other error
    print("There is some error")
else:
    print("this message is from else block")
finally:
    print("this message is from finally block; To be printed whatever happened")


file = None
trials = 5

while trials > 0:
    try:
        print(f"{trials} trials left")
        print("Enter your file path as (F:\\GitHub\\python\\practise\\mydir\\kareem.txt)")
        file_path = input("file_path: ").strip()
        file = open(file_path, "r")
        print(file.read())
        break
    except FileExistsError:
        print("No such file or directory. Try again!")
    except:
        print("Some error happened. Try again!")
        trials -= 1
    finally:
        if file is not None:
            file.close()
else:
    print("Oh! You've used all trials")

# --------------------------- Debugging ----------------------------
mylist = [1, 2, 3, 4, 5]
for num in mylist:
    print(num)

print("We're done")


# --------------------------- Type Hinting ----------------------------
def myadd(num1, num2) -> int:
    print(num1 + num2)

myadd(12, 23)   # 35
myadd(12.5, 23) # 35.5 | Even it's not prefered, it works
