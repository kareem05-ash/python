# Decorators Assignments and Applications
# ------------------ Assignments ------------------
# Assignment_1 
print('*' * 20, 'Assignment_1', '*' * 20)

def reverse_string(mystring):
    for c in mystring: yield c

for c in reverse_string("Kareem"): print(c)
# Assignment_2
print('*' * 20, 'Assignment_2', '*' * 20)

def decorate(func):
    def sub_func():
        print("Sugar added from decorator")
        func()
        print("#" * 20)
    return sub_func
@decorate
def make_tea(): print("Tea's been created")
@decorate
def make_coffe(): print("Coffe's been created")

make_tea()
make_coffe()
# ------------------ Application ------------------
# Application_1: Performance Timer Decorator
print('*' * 20, '# Application_1: Performance Timer Decorator', '*' * 20)

def speed_test(func):
    def sub_func(*args): 
        from time import time
        start = time()
        func(*args)
        end = time()
        print(f"This function takes {end - start} seconds")
    return sub_func

@speed_test
def tst_func(): 
    for num in range(20_000): print(num)

tst_func()

# Application_2: Authentication & Authorization Decorator
print('*' * 20, '# Application_2: Authentication & Authorization Decorator', '*' * 20)
 
admins = ['Kareem', 'Ashraf', 'Mostafa', 'Aboelala', 'Ipraheem']
def authorization(func):
    def sub_func(name, *args):
        if name in admins: 
            print(f"Hello, {name}! You're an admin")
            func(name, *args)
        else: print(f"Sorry, {name}! You're NOT an admin")
    return sub_func

@authorization
def add_admins(name, *new_admins):
    # print(f"Hello, {name}")
    for admin in new_admins: admins.append(admin)
    print("All New Admins Have Been Added Successfully")


add_admins("Ahmed", "Ismail", "Hassan")
add_admins("Kareem", "Ahmed", "Mohamed")
print(f"Admin list after adding new adimins: {admins}")

# Application_3: Rate Limiting Decorator
print('*' * 20, '# Application_3: Rate Limiting Decorator', '*' * 20)
mypassword = "this_is@mypass123"
start = 0 
count = 0
def time_limit(func, max_calls=5, time_window=60):
    def sub_func(*args):
        from time import time
        global start, count
        if count == 0: start = time()
        count += 1
        if time() - start >= time_window: print(f"Sorry, time's done. Total number of execution is {count}")
        else: 
            if count > max_calls: print(f"Sorry, you've consumed all chances in the current time window")
            elif count == max_calls: print(f"Warning: this is the last trial"); func(*args)
            else: func(*args)
    return sub_func

@time_limit
def enter_pass(*args):
    password = input('Enter The Password: ').strip()
    if password == mypassword: print(f"Your're In")
    else: print("In-valid Password. Try again!")

for _ in range(8): enter_pass()
