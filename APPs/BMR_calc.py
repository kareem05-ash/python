# This program calculates BMR ratio for male and female
# This program calculates the least callories a day for bulking

# The expression: BMR = 10 * weight(kg) + 6.25 * height(cm) - 5 * age(years) + s
# s = +5 for men
# s = -161 for women

print('*' * 20, 'BMR Calculator', '*' * 20)
while True:
    gender = input("Are you male or female (m, f)?: ").strip().lower()
    weight = input("Enter Your Weight In (kg): ").strip()
    height = input("Enter Your Height In (cm): ").strip()
    age    = input("Enter Your Age In (yearr): ").strip()
    days   = input("Enter Number Of Workout Days: ").strip()
    try:
        weight = float(weight)
        height = float(height)
        age    = float(age)
        days   = int(days)
        if gender not in ('m', 'f'):
            raise ValueError(f"Selected Gender ({gender}) isn't valid")
    except ValueError:
        print('Unsupported Gender')
    except:
        print('Invalid data input (weight/height/age/days)')
    else:
        break

if gender == 'm':
    BMR = 10 * weight + 6.25 * height - 5 * age + 5         # men
else:
    BMR = 10 * weight + 6.25 * height - 5 * age - 161       # women

print(f"Your BMR is: {BMR}")

print(f"Least Callories a day for Bulking is: {BMR * (1 + days/10) + 500}")