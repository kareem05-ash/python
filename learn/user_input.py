# ------------------------------------------------------------------------------------------------------------------------------
# ---------- User Input ----------
# input(): return type is 'str'
# ------------------------------------------------------------------------------------------------------------------------------


fname = input("Enter your first name: ").strip().capitalize()
mname = input("Enter your middle name: ").strip().capitalize()
lname = input("Enter your last name: ").strip().capitalize()

print(f"Hello, {fname} {mname} {lname}")
print(f"Hello, {fname} {mname:.1s} {lname}")