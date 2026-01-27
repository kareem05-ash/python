import sqlite3 as sq
# -----------------------------------------
# Assignment 1: Students CRUD
print("-" * 10, " Assignment 1: Students CRUD " , "-" * 10)
db = sq.connect("sales.db")
cr = db.cursor()
# cr.execute("CREATE TABLE IF NOT EXISTS students(sid INTEGER, name TEXT, age INTEGER, major TEXT)")

# def add_std(sid, name, age, major):
#   """Insert New Student"""
#   try:
#     cr.execute("INSERT INTO students VALUES(?, ?, ?, ?)", (sid, name, age, major))
#     print(f"New user added with ID({sid})")
#   except sq.Error as er:
#     print(f"Unexpected Error: ({er})")

# def update_major(sid:int, new_major:str):
#   try:
#     cr.execute("UPDATE students SET major = ? WHERE sid = ?", (new_major, sid))
#     print("Studet Data Updated Successfully!")
#   except sq.Error as er:
#     print(f"Unexpected Error ({er})"),

# def rm_std(sid:int):
#   """Removes Student From Students Table"""
#   try:
#     cr.execute("SELECT 1 FROM students WHERE sid = ?", (sid,))
#     if not cr.fetchone():   # Fetched None
#       raise ValueError(f"No such student with ID({sid})")
#     else:
#       cr.execute("DELETE FROM students WHERE sid = ?", (sid,))
#       print(f"Student with ID({sid}) deleted succesfully!")
#   except (sq.Error, ValueError) as er:
#     print(er)
#   except Exception as ex:
#     print(f"Unexpected Error: ({ex})")

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
# print("-" * 10, " Assignment 2: Enrollments " , "-" * 10)
# cr.execute("CREATE TABLE IF NOT EXISTS stds(sid INTEGER, name TEXT)")
# cr.execute("CREATE TABLE IF NOT EXISTS courses(cid INTEGER, name TEXT)")
# cr.execute("CREATE TABLE IF NOT EXISTS enrollments(sid INTEGER, cid INTEGER)")
# cr.execute("INSERT INTO enrollments(sid, cid) VALUES(1, 2)")
# cr.execute("INSERT INTO enrollments(sid, cid) VALUES(2, 3)")
# cr.execute("INSERT INTO enrollments(sid, cid) VALUES(3, 3)")
# # Retrieve all students for Signals & Systems course
# cr.execute("SELECT * FROM courses")
# for c in cr.fetchall():
#   print(f"CourseID => {c[0]} | Name => {c[1]}")

# try:
#   cid = int(input("CourseID: ").strip())
#   cr.execute("SELECT sid FROM enrollments WHERE cid = ?", (cid,))
#   print(f"<<Students In The Course>>")
#   for sid in cr.fetchall():
#     cr.execute("select name from stds where sid = ?", (sid[0],))
#     print(f"StudentID => {sid[0]} | Name => {cr.fetchone()[0]}")
# except Exception as e:
#   print(e)


# # Retrieve all course for Kareem Ashraf only
# cr.execute("select * from stds")
# for std in cr.fetchall():
#   print(f"StudentID => {std[0]} | Name => {std[1]}")

# try:
#   sid = int(input("StudentID: ").strip())
#   print(f"<< Courses For The Student >>")
#   cr.execute("select cid from enrollments where sid = ?", (sid,))
#   for cid in cr.fetchall():
#     cr.execute("select name from courses where cid = ?", (cid[0],))
#     print(f"CourseID => {cid[0]} | Name => {cr.fetchone()[0]}")
# except Exception as e:
#   print(e)

# -----------------------------------------
# Assignment 3
# cr.execute("create table if not exists sales(pid integer, pname text, qty integer, price float, sale_date text)")
ps = 'apple', 'tomato', 'rice', 'cheese', 'bread', 'juice', 'meat', 'milk'
# for pid, pname in enumerate(ps):
#   cr.execute("insert into sales(pid, pname, qty, price) values(?, ?, ?, ?)", (pid+1, pname, 2*pid, 1.49*(pid+1)))
# for count, p in enumerate(ps):
#   print(f"{count+1}. {p}")
# print()
# p = input("Product Name: ").strip().lower()
# cr.execute("select price from sales where pname = ?", (p,))
# tot_rev = 0
# for (price,) in cr.fetchall():
#   tot_rev += price
# print('-'*10, ' Report ', '-'*10)
# print(f"Total Revenu from {p.title()} => {tot_rev}")
cr.execute("select pname, qty from sales")
apple, tomato, rice, cheese, bread, juice, meat, milk = 0, 0, 0, 0, 0, 0, 0, 0
for pname, qty in cr.fetchall():
  if    pname == 'apple'  : apple += qty
  elif  pname == 'tomato' : tomato += qty
  elif  pname == 'rice'   : rice += qty
  elif  pname == 'cheese' : cheese += qty
  elif  pname == 'bread'  : bread += qty
  elif  pname == 'juice'  : juice += qty
  elif  pname == 'meat'   : meat += qty
  elif  pname == 'milk'   : milk += qty

lst = [apple, tomato, rice, cheese, bread, juice, meat, milk]
max = apple
for l in lst[1:]:
  if l > max:
    max = l
    indx = lst.index(l)

if    indx == 0: print(f"Besst Seller Product => Apple | Quantity => {max}")
elif  indx == 1: print(f"Besst Seller Product => Tomato | Quantity => {max}")
elif  indx == 2: print(f"Besst Seller Product => Rice | Quantity => {max}")
elif  indx == 3: print(f"Besst Seller Product => Cheese | Quantity => {max}")
elif  indx == 4: print(f"Besst Seller Product => Bread | Quantity => {max}")
elif  indx == 5: print(f"Besst Seller Product => Juice | Quantity => {max}")
elif  indx == 6: print(f"Besst Seller Product => Meat | Quantity => {max}")
elif  indx == 7: print(f"Besst Seller Product => Milk | Quantity => {max}")




# -----------------------------------------
# Assignment 4

# -----------------------------------------
# Assignment 5



db.commit()
db.close()