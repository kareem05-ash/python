import sqlite3 as sq
# -----------------------------------------
# Assignment 1: Students CRUD
print("-" * 10, " Assignment 1: Students CRUD " , "-" * 10)
db = sq.connect("students.db")
cr = db.cursor()
# cr.execute("CREATE TABLE IF NOT EXISTS students(sid INTEGER, name TEXT, age INTEGER, major TEXT)")

def add_std(sid, name, age, major):
  """Insert New Student"""
  try:
    cr.execute("INSERT INTO students VALUES(?, ?, ?, ?)", (sid, name, age, major))
    print(f"New user added with ID({sid})")
  except sq.Error as er:
    print(f"Unexpected Error: ({er})")

def update_major(sid:int, new_major:str):
  try:
    cr.execute("UPDATE students SET major = ? WHERE sid = ?", (new_major, sid))
    print("Studet Data Updated Successfully!")
  except sq.Error as er:
    print(f"Unexpected Error ({er})"),

def rm_std(sid:int):
  """Removes Student From Students Table"""
  try:
    cr.execute("SELECT 1 FROM students WHERE sid = ?", (sid,))
    if not cr.fetchone():   # Fetched None
      raise ValueError(f"No such student with ID({sid})")
    else:
      cr.execute("DELETE FROM students WHERE sid = ?", (sid,))
      print(f"Student with ID({sid}) deleted succesfully!")
  except (sq.Error, ValueError) as er:
    print(er)
  except Exception as ex:
    print(f"Unexpected Error: ({ex})")

# for sid in range(1, 6):
#   print("-" * 10, f" Student {sid} Data ", "-" * 10)
#   name  = input("Student Name   : ").strip().title()
#   age   = int(input("Student Age    : ").strip())
#   major = input("Student Major  : ").strip().title()
#   add_std(sid, name, age, major)  

# cr.execute("SELECT * FROM students WHERE age > 20")
# for std in cr.fetchall():
#   print(f"StudentID => {std[0]} | Name => {std[1]} | Age => {std[2]} | Major => {std[3]}")

# sid = input("Student ID: ").strip()
# rm_std(int(sid))


# -----------------------------------------
# Assignment 2: Enrollments
print("-" * 10, " Assignment 2: Enrollments " , "-" * 10)
cr.execute("CREATE TABLE IF NOT EXISTS stds(sid INTEGER, name TEXT)")
cr.execute("CREATE TABLE IF NOT EXISTS courses(cid INTEGER, name TEXT)")
cr.execute("CREATE TABLE IF NOT EXISTS enrollments(sid INTEGER, cid INTEGER)")

# -----------------------------------------
# Assignment 3

# -----------------------------------------
# Assignment 4

# -----------------------------------------
# Assignment 5



db.commit()
db.close()