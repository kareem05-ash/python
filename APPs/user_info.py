# ------------------------------------------------------------------------------------------------------------------------------

# ---------- Email Slice ----------
# User Prompt
name = input("Enter your name: ").strip().title()
email = input("Enter your email: ").strip().lower()
age = int(input("What\'s your age?: "))
username = str(email[ : email.index('@')])
website = str(email[email.index('@')+1 : ])
# Display
print(f"Hello, {name}! \nYour email is: {email}\nUserName: {username}\nWebSite: {website}")

# ---------- Age Details ----------
months = age * 12
weeks = months * 4
days = age * 365
hrs = days * 24
mins = hrs * 60
secs = mins * 60
print(f"Your age in: ")
print(f"Years is {age:,}")
print(f"Months is {months:,}")
print(f"Weeks is {weeks:,}")
print(f"Days is {days:,}")
print(f"Hours is {hrs:,}")
print(f"Minutes is {mins:,}")
print(f"Seconds is {secs:,}")