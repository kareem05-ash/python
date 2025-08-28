# ------------------------------------------------------
# --Variables--
# -------------
# [variable name] [assigning operator] [value]
# variable names can starts with a-z or A-Z or Underscore
# variable names can't start with special characters
#       like {@, -, +, =, *, %, etc.....}
# variable names can include Underscore and numbers 1-9
# variable names can't include special characters
# Case Sensitive : name isn't like Name
# --Notes--
# ---------
# Source Code : Original code which you write it in your PC
# Translation : Converting Original code into Machine Language
# Interpretation : Translate code on the fly during executoin
# Run-Time : Period App take to excute line commands
# --Reserved Words--
# ------------------
# help ("keywords") : it prints the reserved keywords
# ------------------------------------------------------

name1 = "Kareem Ashraf"
name2 = "Ahmed Mohamed"
# 3name this isn't valid for variable name
# @name this isn't valid for variable name
print (name1)
print (name2)
help("keywords") # prints all reserved keywords
help("class") # show more data about the written keyword

# this is valid, but redundunt
a = 1
b = 2
c = 3
print(a)
print(b)
print(c)
# this is the shorted way
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)