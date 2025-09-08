# ------------------------------------------------------------------------------------------------------------------------------
# ---------- Salary ----------
# ------------------------------------------------------------------------------------------------------------------------------.

first = float(input("Enter the first payment: "))
month = float(input("Enter the payment per month: "))
percent = float(input("Enter the addition percent per year: "))
tot = first * 1000
for year in range(1, 60): 
    tot += 12 * month
    print(f"Year({year}): {month:,.3f}")
    month = month + month * percent/100.
print(f"Total money payed over 59 years is: {tot:,.3f}")
print(f"The average payed per one year is: {tot/59:,.3f}")