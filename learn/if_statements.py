# ------------------------------------------------------------------------------------------------------------------------------
# ---------- IF Statements ----------
# ------------------------------------------------------------------------------------------------------------------------------.

# Nomal if, else
print(10 * '-', "Nomal if, else", 10 * '-')
cond = False
if cond:    print("Hello!")
else:       print("Goodbuy!")

# if, elif, else
print(10 * '-', "if, elif, else", 10 * '-')
cond1 = False
cond2 = True
if cond1:   print("Hello, Kareem!")
elif cond2: print("Hello, Ashraf!")
else:       print("Goodbuy!")

# Tertinary if condition
print(10 * '-', "Tertinary if condition", 10 * '-')
name = 'kareem'.capitalize()
print("Hello, Kareem!" if name == 'kareem'.capitalize() else "Hello, Ashraf!")

# Nested if statements
print(10 * '-', "Nested if statements", 10 * '-')
name = "kareEm".capitalize()
age = 20
country = "egypt".capitalize()
if name == 'Kareem':    
    if age >= 18:   print("You are old enough to watch this movie. Happy watching!") 
    else        :   print("You are not old enough to watch this movie. Sorry!")
elif country == "Egypt" : print(f"Your name is {name} not Kareem. Your country is {country}")