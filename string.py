# -----------------------------------------
# ---string---
# ------------
#   indexing
#   slicing
# -----------------------------------------

# string : 
name1 = 'kareem ashraf' # it can be written inside single or double quotes
name2 = "kareem ashraf"
        # we can use triple single or double quotes to write a string in multiple lines whitout using '\'
multiple_lines1 = '''kareem 
ashraf
mostafa'''
multiple_lines2 = """kareem
ashraf
mostafa"""
print (name1)
print (name2)
print (multiple_lines1)
print (multiple_lines2)
#   indexing : 
#       we use the square brackets
#       it's zero based list
#       string[index]
index = "kareem ashraf" 
print (index)
print (index[0]) # it prints the first character in in the string : 'k'
print (index[7]) # it prints the (7-1)th character in in the string : 'a'
#   slicing 
#       string[starting_index : ending_index] //note that ending_index isn't included 
#       string[start : end : step] //step here representing the step of the printer (if step = 2, it will ignore character and print character and so on)
#       string[ : end] //it prints from the start till end index (end isn't included)
#       string[start : ] //it pritns from the start index till the end of the string
sli = "Ahmed Mohamed" 
print (sli)
print (sli[2:7]) # it'll print from the index : 2 till the index : 7-1 (med M)
print (sli[ : 8]) # it'll print from the start to the index : 8-1 (Ahmed Mo)
print (sli[2 : ]) # it'll print from the index : 2 to the end (med Mohamed)
print (sli[ : : 1]) # there are no starting or ending index so it'll print the whole string with step : 1 (Ahmed Mohamed)
print (sli[ : : 2]) # ``     ``      ``   ``     ``           ``` `````      ``         ``  with step : 2 (AmdMhmd)


