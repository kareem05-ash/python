######################################################################################################################################################
# ******************** Regular Expresions ********************
# ************************************************************
# NOTE - Regular Expresion is a sequence of characters that defines a seerch pattern
# NOTE - It's used for string validation e.g., (Credit Card, Ip Address, E-Mail Address, etc...) validation
# NOTE - User Manula: [https://www.debuggex.com/cheatsheet/regex/python]
# NOTE - Test & Practise on RegEx: [https://regex.com]
# NOTE - Test & Practise on RegEx: [https://pythex.org]
# ____________________________________________________________
# ----- Here is some regular expressions for character clases -----
# [\d] -> One Digit
# [\D] -> One non-digit
# [\s] -> One whitespace
# [\S] -> One non-whitespace
# [\w] -> One word character NOTE - alpha & digits are included but special characters & dot'.' are not
# [\W] -> One non-word character
# ____________________________________________________________
# ----- Quantifiers ------
# e.g., \w{4}   -> matches for exactly 4 word characters
# e.g., \d{1,3} -> matches for digits in range from 1 to 3 (selects any 1, or 2, or 3 digits)
# e.g., \D{,5}  -> matches for non-digits in range from 0, or 1 to 5
# e.g., \d*     -> matches for digits in range from 0 to infinity
# e.g., \d+     -> matches for 1 or more digits (in range from 1 to infinity)
# e.g., \w?     -> matches for 0 or 1 word character
# ____________________________________________________________
# [0-9]         -> matches for any number from 0 to 9
# [^0-9]        -> matches for anything except the numbers from 0 to 9
# [A-Z]         -> matches for any uppercase alphabitical letter
# [^A-Z]        -> matches for anything except the uppercase letters
# [a-z]         -> matches for any lowercase alphabitical letter
# [^a-z]        -> matches for anything except the lowercase letters
# [0-9A-S]      -> matches for any digit from 0 to 9 and any uppercase ltter from A to S
# [A-z]         -> matches for any alphabitical letter (upper or lower) case
# NOTE -> inserting '^' at the first of the regular expression, ensuring that the expression starts from a new line
# NOTE -> inserting '$' at the end   of the regular expression, ensuring that the expression is at the end of the line
# ____________________________________________________________
# ------ E-Mail Seaarching ------
# ^[A-z0-9\.]+@[A-z0-9]+\.(com|info|net|org)$       -> matches com, info, org, or net email addresses only
# ^[A-z0-9\.]+@[A-z0-9]+\.[A-z0-9]+$                -> matches any email address   
# ____________________________________________________________
# ------ URL Searching ------
# ^(https?://)(www.)?((\w+)\.(com|ash|org|net|me))$
# ____________________________________________________________
# ____________________________________________________________
# ----------------------------- (re) module for regular expressions -----------------------------
# method(1) search(your_reg_exp, your_string)           
#           -> searches for a match for your regular expression and returns the first match only
# method(2) findall(your_reg_exp, your_string)          
#           -> searches for all matches for your regular expression and returns a list of matches.
# method(3) split(your_reg_exp, your_string, maxsplit=n) 
#           -> splits your string in a list by your regular expression with maximum number of splits equals max_split
# mehtod(4) sub(your_reg_exp, replace, your_string, count=n)  
#           -> replaces each match for your regular expression by the replace with maximum number of replacement equals replace_count 
#   NOTE -> In case of no match, the returned list will be empty
# 
# NOTE -> re.search.group(n): returns group number 'n' in the search result
# NOTE -> re.search.groups(): returns a tuple of groups in the search result
#                                                                                                                                                   #
######################################################################################################################################################


# import re

# test_string = "https://kareem.ash"
# reg_exp = r"(https?)://(\w+)\.(\w+)"
# srch_res = re.search(reg_exp, test_string)

# print(srch_res.group())
# print('*' * 30)
# print(srch_res.groups())
# print(type(srch_res.groups()))
# print('*' * 30)
# for x in srch_res.groups():
#     print(x)

# from re import search as s
# from re import findall as f

# # name = 'KAreem Ashraf'
# # my_re = r'[A-Z]+'       # searches for a group of uppercase letters
# # srch_rslt = s(my_re, name)

# # # print(srch_rslt)
# # # print(srch_rslt.group())
# # print(srch_rslt.span())
# # # print(dir(srch_rslt))

# # for match in srch_rslt.group():
# #     print(match)



# # user_email = input("Enter Your E-mail: ").strip()
# regular_exp = r"^[A-z0-9\.]+@[A-z0-9]+\.[A-z0-9]+$"

# user_email_list = []

# # is_valid = f(regular_exp, user_email)
# # if is_valid:
# #     print(f"Your email address ({user_email}) is valid")
# # else:
# #     print(f"Your email address ({user_email}) is NOT valid")

# for _ in range(2):
#     user_email_list.extend(f(regular_exp, input("Enter Your E-mail: ").strip()))


# print(user_email_list)



# import re

# print(re.split(r"-", "Kareem-Ashraf-Mostafa-Aboelal"))
# print(re.split(r"-", "Kareem-Ashraf-Mostafa-Aboelal", maxsplit=2))
# print(re.sub(r"-", " ", "Kareem-Ashraf-Mostafa-Aboelal"))
# print(re.sub(r"-", " ", "Kareem-Ashraf-Mostafa-Aboelal", count=2))

# import re
# testString = """http
# https
# abcd
# abcd"""

# reg_exp1 = r"https?"
# reg_exp2 = r"(https)|(http)"
# reg_exp3 = r""
# reg_exp4 = r""
# reg_exp5 = r""

# print(re.findall(reg_exp1, testString))


# import re
# test_string = """http://www.elzero.org:8888/link.php
# https://elzero.org:8888/link.php
# http://www.elzero.com/link.py
# https://elzero.com/link.py
# http://www.elzero.net
# https://elzero.net"""

# reg_exp = r"(.+\.)(net)"

# srch_list = re.findall(reg_exp, test_string, re.MULTILINE)

# # print(srch_list)
# for url in srch_list:
#     print(url)