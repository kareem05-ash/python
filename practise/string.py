# -----------------------------------------------------------------------------------------
# ----- This file is considered a practise on string and its methods -----
# [1st] Assignment: exp output => "Hello 'Kareem', How You Doing \ """ Your Age Is "20"" + And Your Country Is: Egypt
# [2nd] Assignment: print the previous output but each section in a single line
# [3rd] Assignment: Indexing & Sclicing: single character
# [4th] Assignment: Indexing & Sclicing: multiple characetrs
# [5th] Assignment: print: Kareem not #@#@Kareem#@#@
# [6th] Assignment: use .zfill() method
# [7th] Assignment: use .rjust() method
# [8th] Assignment: use .swapcase() method
# [8th] Assignment: use .count() method
# [10th] Assignment: use .index() method
# [11th] Assignment: use .replace() method: for one time
# [12th] Assignment: use .replace() method: for all occurences
# [13th] Assignment: define your age as integer not string
# -----------------------------------------------------------------------------------------

# [1st] Assignment: exp output => "Hello 'Kareem', How You Doing \ """ Your Age Is "20"" + And Your Country Is: Egypt
print(30 * '-', '1st Assignment', 30 * '-')
name = "'Kareem'"
age = '"20"'
country = 'Egypt'
print(f'"Hello {name}, How You Doing \\ """ Your Age Is {age} + And Your Country Is: {country}')
# -----------------------------------------------------------------------------------------
# [2nd] Assignment: print the previous output but each section in a single line
print(30 * '-', '2nd Assignment', 30 * '-')
print(f'''"Hello {name}, How You Doing \\
""" Your Age Is {age} +
And Your Country Is: {country}''')
# -----------------------------------------------------------------------------------------
# [3rd] Assignment: Indexing & Sclicing: single character
print(30 * '-', '3rd Assignment', 30 * '-')
name = "Kareem"
print(f'''The Second Letter is: "{name[1]}"
The Third Letter is: "{name[2]}"              
Teh Last Letter is: "{name[-1]}"''')
# -----------------------------------------------------------------------------------------
# [4th] Assignment: Indexing & Sclicing: multiple characetrs
print(30 * '-', '4th Assignment', 30 * '-')
name = 'Kareem'     # 1st line: "are", 2nd line: "Kre", 3rd line: "erK"
print(f'''"{name[1:4]}"
"{name[::2]}"
"{name[4::-2]}"''')
# -----------------------------------------------------------------------------------------
# [5th] Assignment: print: Kareem not #@#@Kareem#@#@
print(30 * '-', '5th Assignment', 30 * '-')
name = "#@#@Kareem#@#@"
print(name.strip("#@"))
# -----------------------------------------------------------------------------------------
# [6th] Assignment: use .zfill() method
print(30 * '-', '6th Assignment', 30 * '-')
num = "2"
print(num.zfill(4))
num = "15"
print(num.zfill(4))
num = "233"
print(num.zfill(4))
num = "1500"
print(num.zfill(4))
# -----------------------------------------------------------------------------------------
# [7th] Assignment: use .rjust() method
print(30 * '-', '7th Assignment', 30 * '-')
name = "Kareem"
fullname = "Kareem_Ashraf"
print(name.rjust(20, '@'))
print(fullname.rjust(20, '@'))
# -----------------------------------------------------------------------------------------
# [8th] Assignment: use .swapcase() method
print(30 * '-', '8th Assignment', 30 * '-')
name = "KareEM AsHRaf"
print(name.swapcase())
# -----------------------------------------------------------------------------------------
# [8th] Assignment: use .count() method
print(30 * '-', '9th Assignment', 30 * '-')
msg = "I Love Python And Although Love Kareem Ashraf"
print(msg.count('Love'))    # 2
# -----------------------------------------------------------------------------------------
# [10th] Assignment: use .index() method
print(30 * '-', '10th Assignment', 30 * '-')
name = "Kareem"
print(name.index('r'))  # 2
# -----------------------------------------------------------------------------------------
# [11th] Assignment: use .replace() method: for one time
print(30 * '-', '11th Assignment', 30 * '-')
msg = "I <3 Python And Although <3 Kareem Ashraf"
print(msg.replace('<3', 'Love', 1)) # I Love Python And Although <3 Kareem Ashraf
# -----------------------------------------------------------------------------------------
# [12th] Assignment: use .replace() method: for all occurences
print(30 * '-', '12th Assignment', 30 * '-')
print(msg.replace('<3', 'Love')) # I Love Python And Although Love Kareem Ashraf
# -----------------------------------------------------------------------------------------
# [13th] Assignment: define your age as integer not string
print(30 * '-', '13th Assignment', 30 * '-')
name = "Kareem"
age = 20
country = "Egypt"
print(f"Your name: {name}, Your age: {age}, Your country: {country}")
# -----------------------------------------------------------------------------------------