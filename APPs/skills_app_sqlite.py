# ---------------------------------
# Skills App SQLite-Based
# ---------------------------------

msg = """
What Do You Want To Do?
  "u" => Show All Existing Users
  "a" => Add New Skill To an Existing User
  "s" => Show All Skills Of a Single User
  "r" => Remove A Skill
  "u" => Update Skill Progress
  "q" => Quit The app
Choose Option: """
global db, cr
methods = ['u', 's', 'a', 'r', 'u', 'q']
import sqlite3

# ------------------------------------------------------------------
# Define All Methods

## Connect To Database Method
def connect(dbfile):
  try:
    global db, cr
    db = sqlite3.connect(dbfile)
    cr = db.cursor()
    print(f"Connected To Database")

  except sqlite3.Error as er:
    print(f"Unexpected Error: {er}")

## Commit & Close Method
def commit_close():
  db.commit()
  db.close()
  print("Database Closed Successfully!")

## Show Users Data Method
def show_users():
  print('\n', "<< Users Data >>".center(50))
  connect('data.db')
  cr.execute("SELECT * FROM users")
  users = cr.fetchall()
  for user in users:
    print(f" # UserID  -> {str(user[0]).zfill(2)}", end=' | ')
    print(f"Name    -> {str(user[1]).ljust(10)}", end= ' | ')
    print(f"Age     -> {user[2]}")
  commit_close()

## Add New Skill Method
def add_skill():
  print('\n', "<< Add Skill >>".center(50))
  connect('data.db')

  # Get Data From The User
  uid = input("Enter UserID: ").strip()
  skill = input("Enter Skill Name: ").strip().capitalize()
  prog = input("Enter Skill Progress: ").strip()
  
  # Add skill
  try:
    uid = int(uid)
    prog = int(prog)
    # Data Validation
    ## User ID Validation
    cr.execute("SELECT 1 FROM users WHERE uid = ?", (uid, ))
    if not cr.fetchone():     # User doesn't exist
      raise ValueError(f"User with ID ({uid} not found)")
    
    ## Non-empty skill name
    if not skill:             # Empty skill name
      raise ValueError(f"Unsupported Empty Skill Name")
    
    ## Sufficient Progress Value
    if prog < 0 or prog > 100:  # Invalid progress value
      raise ValueError(f"Invalid Progress Value ({prog}). Must be in [0, 100] range.")
  
    cr.execute("INSERT INTO skills(name, progress, uid) VALUES(?, ?, ?)", (skill, prog, uid))
    print("Skill's been added successfully!")

  except sqlite3.Error as er:
    print(f"Unexpected Error: {er}")

  except ValueError as ve:
    print(f"ValueError: {ve}")

  except:
    print("Unexpected Error")
  
  finally:
    commit_close()

## Show All Skills Of a Single User Method
def show_skills():
  print("Show Skills")

## Remove an Existing Skill Method
def rm_skill():
  print("Remove an Existing Skill")

## Update Skill Progress Method
def update_progress():
  print("Update Skill Progress")


# ------------------------------------------------------------------
# UI Menu
def UI():
  # Input Operation Selection
  op = input(msg).strip().lower()

  if op in methods:     # Valid Operation

    if op == "u":           # Show Users
      show_users()

    elif op == "a":         # Add Skill
      add_skill()
    
    elif op == "s":         # Show Skills
      show_skills()

    elif op == "r":         # Remoe Skill
      rm_skill()

    elif op == "u":         # Update Skill Progress
      update_progress()

    else:                   # Exist App
      print("Goodbuy!")

  else:                 # Invalid Operation
    print(f"Unsupported Operation {op}")

UI()