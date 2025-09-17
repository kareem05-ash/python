######################################################################################################################################################
# -------------------- Date & Time In Python --------------------
# ---------------------------------------------------------------
# NOTE - First, we need to import datetime module: 
#       from datetime import datetime as dt
# ************************* Currnet Date ************************* 
# [1] dt.now().date()       => returns the current date with timestamp: yyyy-mm-dd
# [2] dt.now().date().year  => returns the current year: yyyy
# [3] dt.now().yead         => returns the current year: yyyy
# [4] dt.now().date().month => returns the current month: mm
# [5] dt.now().month        => returns the current month: mm
# [6] dt.now().date().day   => returns the current day: dd
# [7] dt.now().day          => returns the current day: dd
# ************************* Currnet Time ************************* 
# [1] dt.now().time()               => returns the current time with timestamp: hh:mm:ss:micros
# [2] dt.now().time().hour          => returns the current hour: hh
# [3] dt.now().hour                 => returns the current hour: hh
# [4] dt.now().time().minute        => returns the current minute: mm
# [5] dt.now().minute               => returns the current minute: mm
# [6] dt.now().time().second        => returns the current second: ss
# [7] dt.now().second               => returns the current second: ss
# [8] dt.now().time().microsecond   => returns the current microsecond: micros
# [9] dt.now().microsecond          => returns the current microsecond: micros
# ************************* Current Date & Time *************************
# [1] dt.now()      => returns the current date & time with timestamp: yyyy-mm-dd hh:mm:ss:micros
# ************************* Limits Of Date & Time *************************
# [1] dt.now().min  => returns the minimum date & time: 0001-01-01 00:00:00                                                                                                            # 
# [1] dt.now().max  => returns the maximum date & time: 9999-12-31 59:59:59:999999
# ************************* Specific Date & Time *************************
# myBirthDay  = dt(2005, 5, 5)
# currentDate = dt.now()
# (currentDate - myBirthDay)    => returns {num of days} days, hh:mm:ss:micros
# (currentDate - myBirthDay).days   => returns {num of days} "as float number"
# ************************* Configure Date-Stamp *************************
# NOTE - To format your date, you should use 'strformat' method as following
#       e.g., dt.now().strformat("%d / %m / %Y") => 17 / 09 / 2025
# NOTE - This website is a guideline for this topic: [https://strftime.org]
# Sone Examples on strftime: 
#   [1] %a  => This is for day name shorted. e.g., Sun
#   [2] %A  => This is for full day name. e.g., Sunday
#   [3] %d  => This is for day number of month as a zero-padded decimel number. e.g., 05
#   [4] %-d => This is for day number of month as decimel number. e.g., 5
#   [5] %b  => This is for month name shorted. e.g., Oct
#   [6] %B  => This is for full month name. e.g., October
#   [7] %m  => This is for month number as a zero-padded decimel number. e.g., 08 (for Aug)
#   [8] %-m => This is for month number as a decimel number. e.g., 8 (for Aug)
#   [9] %y  => This is for Year without century (shorted). e.g., 05 (for 2005)
#   [10] %Y => This is for Year with century. e.g., 2005
#   [11] %H => This is for hour in 24 system as a zero-padded decimel number. e.g., 05 (for 5 AM)
#   [12] %-H=> This is for hour in 24 system as a decimel number. e.g., 5 (for 5 AM)
#   [13] %I => This is for hour in 12 system as a zero-padded decimel number. e.g., 09
#   [14] %-I=> This is for hour in 12 system as a decimel number. e.g., 9                                                                          # 
######################################################################################################################################################
import datetime
from datetime import datetime as dt
print(dir(datetime))    # prints the methods of 'datetime' module
print()
print(dir(dt))          # prints the methods of 'datetime' method

print('#' * 80)

# Current Date
print(dt.now().date())          # e.g., 2025-09-18
print(dt.now().year)            # e.g., 2025
print(dt.now().month)           # e.g., 9
print(dt.now().day)             # e.g., 17

print('#' * 80)

# Current Time
print(dt.now().time())          # e.g., 02:57:55:234220
print(dt.now().hour)            # e.g., 2
print(dt.now().minute)          # e.g., 57
print(dt.now().second)          # e.g., 55
print(dt.now().microsecond)     # e.g., 234220

print('#' * 80)

# Current Date & Time
print(dt.now())             # e.g., 2025-09-18 02:57:55:234220

print('#' * 80)

# Max & Min Date_Time
print(dt.min)
print(dt.max)

print('#' * 80)

# Specific Date & Time
myBirthDay = dt(2005, 5, 5)
currentDate= dt.now()
print(myBirthDay)
print(currentDate)
print(f"I've lived for {(currentDate - myBirthDay).days:,} Days")
print(f"I've lived for {(currentDate - myBirthDay).days / 30:,.0f} Months")
print(f"I've lived for {(currentDate - myBirthDay).days / 365:,.0f} Years")

print('#' * 80)

# Configure Date-Stamp
my_birthday = dt(2005, 5, 5)
print(f"My year born: {my_birthday.strftime('%Y')}")
print(f"My month born: {my_birthday.strftime('%B')}")
print(f"My day born: {my_birthday.strftime('%A')}")

print(f"My Birthday Date: {my_birthday.strftime("%d/%m/%Y")}")

print(f"I Love {my_birthday.strftime('%B')} Because I've been Born In It")
print(f"I Love {my_birthday.strftime('%A')} Because I've been Born On It")
print(f"I Love {my_birthday.strftime('%Y')} Year Because I've been Born At It")