# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# This application implements a program which organize grading system of some students

# Program Features
# [1] Add new student with its grades
# [2] Show students list with their grades
# [3] Show heighest and lowest grade with student name
# [4] Show sorted students list by their grades (heighest first)
# [5] Calculate the mean of the grades
# [6] Search for a student grade by its name
# [7] Edit a student grades

# The Supported Subjects 
# It Can Be Extended 
# = Logic
# = Electro
# = Digital
# = Analog
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ---------------- Program Functions ----------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# Dictionary Data
students_data = {}
special = ('!', '@', '#', '$', '%', '^', '&', '*')
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# validate numerical input function
def is_number(var):
    try: var = float(var); return True
    except: return False
def num_input(sub):
    while True:
        var = input(f"Enter {sub} grade: ").strip()
        if is_number(var): break
        else: print("Sorry, invalid grade input. Try again!")
    return float(var)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# add new student function:
def add():
    global students_data
    name = input("Enter student full name: ").strip().lower().title()
    Logic = num_input('Logic')
    Electro = num_input('Electro')
    Digital = num_input('Digital')
    Analog = num_input('Analog')
    students_data[name] = {'Logic': Logic, 'Electro': Electro, 'Digital': Digital, 'Analog': Analog}

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# show all students with their grades
def show():
    pass
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# Main Program Loop
while True:
    choise = input("""Choose Operation
Write (add)         to add a new student
Write (show)        to show all students with their grades sorted alphabitically
Write (show_hl)     to show heighest and lowest students' grades
Write (show_sorted) to show all students lits sorted by their grades (heighest first)
Write (mean)        to calculate and print the mean of the grades of all students
Write (find)        to search for a student's grades by its name
Write (edit)        to edit a student grades
Write (quit)        to quit from the program
Your choise is: """).strip().lower()
    
    if choise in ('add', 'show', 'show_hl', 'show_sorted', 'mean', 'find', 'edit', 'quit'):
        if choise == 'add': add()
        elif choise == 'quit': print("Thank You!"); break
        else: print("Error")
    else: print(f"Invalid choise. Try again!")

print(students_data)

