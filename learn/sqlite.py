######################################################################################################################################################
# --------------
# SQLite
# --------------
# 1. Import Database Module     -> import sqlite3
# 2. Create Database & Connect  -> db = sqlite3.connect('file_name.db')
# 3. Create Table               -> db.execute("CREATE TABLE IF NOT EXISTS 'table_name' (col1 DATA_TYPE, col2 DATA_TYPE, and so on)")
# 4. Close Database             -> db.close()       
# NOTE: It's not prefered to use db connection to access Database. You should use The Cursor instead
# 5. Setting Up The Cursor      -> cr = db.cursor()
# NOTE: Once 'cr' variable is defined as the db.cursor(), you can access your Database like (cr.execute("YOUR QUERY")   
# 6. Inserting Data             -> cr.execute("INSERT INTO 'table_name'(uid, name, age) VALUES(1, 'Kareem', 21)")     
# 7. Fetching Data              -> We can fetch data using 3 methods (fetchone, fetchall, fetchmany)
# NOTE: We need first to write fetching query   "SELECT field FROM table_name"
#   = cr.execute("SELECT name FROM users")      => This fetches names column from users table
#   = cr.execute("SELECT uid FROM users")       => This fetches user ids column from users table
#   = cr.execute("SELECT uid, age FROM users")  => This fetches user ids & users age columns from users table
#   = cr.execute("SELECT * FROM users")         => This fetches all columns from users table
# NOTE: After writing the query, we can fetch data as we want
#   - cr.fetchone()       => returns one row as a tuple
#   - cr.fetchall()       => returns all rows as a list of tuples
#   - cr.fetchmany(n)     => returns 'n' rows as a list of tuples   
# 8. Adding Column To An Existing Table   -> cr.execute("ALTER TABLE users ADD COLUMN age INTEGER DEFAULT 0")
#   - This will add another column to users table (age column) setting all existing rows with 0 age
#   NOTE: We can remove (DEFAULT 0) hence, existing rows will take Null age   
# 9. Updating existing data   -> cr.execute("UPDATE users SET age = ? WHERE uid = ?", (20, 1))
#   - This updates user with (uid = 1) age = 20     
# 10. Deleting Existing Data  -> cr.execute("DELETE FROM table_name WHERE coln = ?" (coln_val, ))   
#   - cr.execute("DELETE FROM users WHERE uid = 3")   // This deletes user with uid = 3 from users table
#   - cr.execute("DELETE FROM users")                 // This deletes all data in users table                                                                             # 
######################################################################################################################################################
# Import DataBase Module
import sqlite3

# # Create DataBase & Connect using 'db' variable
# db = sqlite3.connect("data.db")    # Connection with database file

# # Setting Up The Cursor
# cr = db.cursor()

# # Create Tables Using Cursor Connection
# cr.execute("CREATE TABLE IF NOT EXISTS 'users' (uid INTEGER, name TEXT)")
# cr.execute("CREATE TABLE IF NOT EXISTS 'skills' (name TEXT, progress INTEGER, uid INTEGER)")

# # # Inserting Data Into Your Database
# # users = ['Kareem', 'Ahmed', 'Mohamed', 'Naser', 'Hagag', 'Ibrahim', 'Mr']
# # for key, user in enumerate(users):
# #   cr.execute(f"INSERT INTO 'users'(uid, name) VALUES({key + 1}, '{user}')")

# # Updating Users Data
# cr.execute("Update users SET age = ? WHERE uid = ?", (20, 1))

# # # Fetching Data
# # cr.execute("SELECT * FROM users")
# # print(type(cr.fetchone()))

# # # Add New Column To An Existing Table
# # cr.execute("ALTER TABLE users ADD COLUMN age INTEGER")

# # # Seeing Database Info
# # cr.execute("PRAGMA table_info(users)")
# # print(cr.fetchall())

# # Commit Changes
# db.commit()

# # Close DataBase
# db.close()


# Get Data Function
def get_data():
  try:
    # Connect to database
    db = sqlite3.connect("data.db")
    cr = db.cursor()
    print("\nConnected to Database successfully")

    # Fetching Data
    cr.execute("SELECT * FROM users")
    print("Fetching users all data DONE!")

    # Printing Users Data
    print()
    for row in cr.fetchall():
      print(f"UserID -> {row[0]}", end=" | ")
      print(f"Name   -> {str(row[1]).ljust(10)}", end=" | ")
      print(f"Age    -> {row[2]}")

  except sqlite3.Error as er:
    print(f"Unexpected Error: {er}")
  finally:
    db.close()

# Remove Data Function
def rm(table, uid) -> None:
  try:
    # Connect To Database
    db = sqlite3.connect("data.db")
    cr = db.cursor()

    # Delete Data
    cr.execute(f"DELETE FROM {table} WHERE uid = ?", (uid,))

    # Commit Changes
    db.commit()
    print(f"\nRow with UserID = {uid} in {table} has been deleted successfully")

  except sqlite3.Error as er:
    print(f"Unexpected Error: {er}")

  finally:
    db.close()

get_data()

rm('users', 7)

get_data()