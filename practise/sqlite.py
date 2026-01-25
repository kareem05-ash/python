# import sqlite3
# db = sqlite3.connect('data.db')
# cr = db.cursor()

# # Creating users table
# cr.execute("CREATE TABLE IF NOT EXISTS users(uid INTEGER, name TEXT, dob TEXT, email TEXT)")

# # Add New User
# def add_user(uid:int):
#   """Add new user for users table"""
#   name = input("User Name: ").strip().title()
#   email = input("User Email: ").strip().lower()
#   dob = input("Date of Birth: ").strip()
#   cr.execute("SELECT uid FROM users")
#   if (uid, ) not in cr.fetchall():
#     cr.execute("INSERT INTO users VALUES(?, ?, ?, ?)", (uid, name, dob, email))
#   else:
#     print(f"User with ID ({uid}) already has data")

# def rm(uid:int):
#   """Remove user data with uid"""
#   try:
#     cr.execute("DELETE * FROM users WHERE uid = ?", (uid, ))
#     db.commit()
#     print(f"User with ID({uid}) DELETED")
#   except sqlite3.Error as er:
#     print(f"Unexpected Error: {er}")
#   except:
#     print("Error")

# # for u in range(5):
# #   print("-" * 10, f"User ({u + 1}) Data", "-" * 10)
# #   add_user(u + 1)
# #   print()
# # db.commit()

# # cr.execute("SELECT * FROM users ORDER BY uid DESC LIMIT 1")
# # print(cr.fetchall())

# cr.execute("SELECT uid FROM users")
# uid = input("User(to be deleted) ID: ").strip()
# try:
#   uid = int(uid)
# except:
#   print(f"({uid}) not a valid User ID")

# if (uid,) not in cr.fetchall():   # User Doesn't Exist
#   print("User Doesn't Exist")
# else:       # User Exists
#   rm(uid)
#   cr.execute("SELECT * FROM users")
#   users = cr.fetchall()
#   for user in users:
#     if user[0] != uid:
#       print(f"ID => {user[0]}, Name => {user[1]}, Data Of Birth => {user[2]}, Email => {user[3]}")

# db.close()



