# -------------------------------------------------------------------------------------------------
# --Escape Sequences Characters--
# -------------------------------
# \b => back space : it removes the previous character
# \newline => it ignores the newline
# \\ => escape back-slash : if u want to print '\' in your text
# \' => escape single quote : it's not important for newer versions
# \" => escape double quote : it's stil important
# \n => feed with newline : just like cout<<endl; in C++
# \t => feed with tap : leaves indent after it
# \r => carriage return 
# \xhex => cahracter hex value : it returns the cahracter which has "hex" as its hex equivalent

# Concatination => using '+' operator
# -------------------------------------------------------------------------------------------------

# \b : 
print ("Kareemm\b Ashraf") # it prints "kareem Ashraf" not "Kareemm Ashraf"

# \newline
print("karee\
 Ashraf\
 Mostafa")

# \\ : 
print ("kareem\\Ashraf")

# \" : 
print ("Kareem \"Ashraf\" ")

# \n : 
print ('Kareem\nAshraf')

# \t : 
print ("kareem\tAshraf")

# \r : 
print ("123456\rabcd") # it replace the first four characters with the characters after "\r"
print ("asdfdgda\rkareem") # it prints : kareemgda ////asdfd are ignored

# \xhex : 
print ("\xCF") # now it prints 'I', because the equivalent ASCCI code for 'I' in hex is //CF//
print ("\x7c") # now it prints '|', because the equivalent ASCCI code for '|' in hex is //7C//. af == AF (it's not case sensitive here noly)

# concatination : 
firstname = "kareem"
secondname = "ashraf"
print (firstname + secondname) # it prints : kareemashraf
print (firstname + " " + secondname) # it prints what we need with space : kareem ashraf