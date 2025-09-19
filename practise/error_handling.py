# Assignments of Error Handling & Debugging

# Assignment_1
print('*' * 20, 'Assignment_1', '*' * 20)

NUM = input("Add Your Number: ")


if len(NUM) != 1:
    raise IndexError("Only One Character Allowed")
if NUM == '0':
    raise ValueError("Number Must Be Larger Than 0")
if NUM.isalpha():
    raise Exception("Only Numbers Allowed")
print(f"The Number Is {NUM}")

# Assignment_2
print('*' * 20, 'Assignment_2', '*' * 20)

letter = input("Enter a letter from A - Z: ").strip()

try:
    if len(letter) != 1:
        raise IndexError
    elif not letter.isupper() or not letter.isalpha():
        raise Exception
except IndexError:
    print("You must write one character only")
except Exception:
    print("The letter isn't in A - Z")
else:
    print(f"You Typed {letter}")

# Assignment_3
print('*' * 20, 'Assignment_3', '*' * 20)

def calculate(num1, num2) -> int:
    return num1 + num2

print(calculate(20, 30))