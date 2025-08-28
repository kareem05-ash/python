# -----------------------------------------------------------------------------------------------------------
# -----String Formating-----
# -------------------------
# Old Method :: 
#       %s => string
#       %d => number == int
#       %f => float
#       print("myname is %s I'm %d years old" %(name, age))
# New Method ::
#       {s} => string
#       {d} => number
#       {f} => float
#       print("myname is {:s} I'm {:d} yars old".format(name, age))
#       print(f"nyname is {name} I'm {age} years old") => easier way
# -----------------------------------------------------------------------------------------------------------

# Old Method : 
name = "kareem"
level = "junior"
age = 20
## print("My name is " + name + "and I'm " + level + "\nMy age is : " + age) # Error : Can't concatinate string to int
print("My name is %s and I'm %s\nMy age is %d"%(name, level, age))  # My name is kareem and I'm junior
                                                                    # MY age is 20
print("My name is %s and I'm %s\nMy age is %f"%(name, level, age))  # My name is kareem and I'm junior
                                                                    # MY age is 20.000000
print("My name is %s and I'm %s\nMy age is %.2f"%(name, level, age))# My name is kareem and I'm junior
                                                                    # MY age is 20.00

## Truncate string : 
longstring = "kareem ashraf mostafa aboelala iprahim aboelala"
print("MY shortend string : %.10s" % longstring) # it prints : just 10 cahracters from 'longstring' : kareem ash 


# New Method : 
name = "kareem"
level = "junior"
age = 20
## print("My name is " + name + "and I'm " + level + "\nMy age is : " + age) # Error : Can't concatinate string to int
print("My name is {:s} and I'm {:s}\nMy age is {:d}".format(name, level, age))  # My name is kareem and I'm junior
                                                                    # MY age is 20
print("My name is {:s} and I'm {:s}\nMy age is {:f}".format(name, level, age))  # My name is kareem and I'm junior
                                                                    # MY age is 20.000000
print("My name is {:s} and I'm {:s}\nMy age is {:.2f}".format(name, level, age))# My name is kareem and I'm junior
                                                                    # MY age is 20.00

## Truncate string : 
longstring = "kareem ashraf mostafa aboelala iprahim aboelala"
print("MY shortend string : {:.10s}".format(longstring)) # it prints : just 10 cahracters from 'longstring' : kareem ash 

print(f"myname is {name} I'm {age} years old and I'm a {level}")