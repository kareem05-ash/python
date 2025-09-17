from datetime import datetime as dt

# Assignment_1
print('*' * 20, 'Assignment_1', '*' * 20)
birthday = dt(2005, 5, 5)
today = dt.now() 
print(f"Days From {birthday.date()} To {today.date()} Is => {(today - birthday).days}")

# Assignment_1
print('*' * 20, 'Assignment_1', '*' * 20)
# Today Is 17 / 09 / 2025
today = dt.now()
print(today.date())                     # 2025-09-17
print(today.strftime("%b %d, %Y"))      # Sep 17, 2025
print(today.strftime("%d - %b - %Y"))   # 17 - Sep - 2025
print(today.strftime("%d / %b / %y"))   # 17 / Sep / 25
print(today.strftime("%d / %B / %Y"))   # 17 / September / 2025
print(today.strftime("%a, %d %B %Y"))   # Wed, 17 September 2025
