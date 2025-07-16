# ----------------------------------------------------------------------------------------------------
# ---String Methods---
# --------------------
# len(string_name) => it returns integer number representing the # characters in the string
# string_name.strip() => it deletes spaces form right and left
# string_name.rstrip() => it deletes spaces form right
# string_name.lstrip() => it deletes spaces form left
#       we can specify the deleted characters by adding the character to be deleted in the paranthesis
# string_name.title() => it fits your string to be a title by capitalizing the first character of each word
#       and capitilizing any character after the numbers
# string_name.capitalize() => it capitalizes the first character of the first word in your string
# string_name.zfill(width to be fit for) => print('12'.zfill(3)) ->> prints : 012 
# string_name.upper() => makes all the characters in the string uppercase
# string_name.lower() => makes all the characters in the string lowercase
# string_name.split() => divides your string based on spaces(default) and combine them all in a list
# string_name.split('cahracter') => divides your string based on your cahracter and combine them all in a list
# string_name.split('character', N) => divides your string based on your character into N words 
#       and leave the rest of your string in an one element and combine them in a list. So the list contains (N+1) elments
# string_name.rsplit() => It has the same features which .split() has. 
#       The core difference is thet this one split from right not left
# string_name.center(N, 'charater') => N : number of character needed in the returned string
#                                      character : the character or string which wraps your string
#       if 'character' isn't inculded, it'll be wrapped with default spaces
#       if(N - # characters in your string) is odd then the resulted string will be something like that : @@@kareem@@
# string_name.count("string", index1, index2) => it returns the number of multiples of "string" from index1 to index2
#       if(index1, index2 aren't included) the search will be on the whole string_name
# string_name.swapcase() => it makes all lowercase characters to uppercase character and vice verse
# string_name.startswith("string or character", index1, index2) => 
#       it returns "True" if your string starts with the inlcuded string or character
#       the search are from index1 to index2 : index2 isn't included
#       if(index1, index2) arn't included, will search on the whole string
# string_name.endswith("string or character", index1, index2) => 
#       it returns "True" if your string ends with the inlcuded string or character
#       the search are from index1 to index2 : index2 isn't included
#       if(index1, index2) arn't included, will search on the whole string
# string_name.index("string or character", index1, index2) => it returns the index of the character or the first character of the string
#       if it's not found the program'll release error. if(index1, index2) isn't included, will search over the whole string
# stirng_name.find("string or character", index1, index2) => it's the same as index(), but if the substring isn't found it will return -1 not releasing an error
# string_name.rjust(N, "character") => it justifies your string to the right then fills the rest by the "character". N : the width of the returned string. EX: ####kareem if (N=10)
# string_name.ljust(N, "character") => it justifies your string to the left then fills the rest by the "character". N : the width of the returned string. EX: kareem#### if (N=10)
# string_name.splitlines() => it combine your strin in a list, making each line as an element in the list
# string_name.expandtabs(tab size) => you can custumize tab-size 
# string_name.istitle() => returns 'True' iff the all words in the string starts with uppercase character and all the cahracters which follow numbers too.
# string_name.isspace() => returns 'True' iff your string is a space
# string_name.islower() => returns 'True' iff all the chcaracters in your string is lowercase
# string_name.isupper() => returns 'True' iff all the chcaracters in your string is uppercase
# string_name.isidentifier() => returns 'True' iff your string can be an identifier name
# string_name.isalpha() => returns 'True' iff your string consists of aphapitical characters (A-Z or a-z) only
# string_name.isalnum() => returns 'True' iff your string consists of aphapitical characters (A-Z or a-z) or numbers only
# string_name.replace("substring_old","substring_new", replacement_count) => it replece your substring_old with substring_new in your whole string whenever found replacement_count times.
#       if replacement_count isn't included, the replacement occurs over all substring_old values
# "seperator".join(list_name or tuple_name) => it returns a string which holds the list or tuple elements. Each element sepearated by "seperator"
# ----------------------------------------------------------------------------------------------------

# len(string_name) : 
name = 'kareem ashraf'
print(len(name)) # it returns the # characters : 13
print(len('kareem ashraf')) # it returns the # characters : 13

# string_name.strip() : 
name1 = '    kareem ashraf    '
print(name1.strip()) # it prints (kareem ashraf) without spaces before or after
name2 = '####kareem asharf##'
print(name2.strip('#')) # it prints (kareem ashraf) without hashes

# string_name.rstrip() : 
name1 = '####kareem ashraf####'
print(name1.rstrip('#')) # it prints (####kareem ashraf) after deleting hashes from right only
name2 = '#@#@#@kareem ashraf#@#@#@'
print(name2.rstrip('#@')) # it prints (#@#@#@kareem ashraf) after deleting '#@' from the right

# string_name.lstrip() : 
name1 = '####kareem ashraf####'
print(name1.lstrip('#')) # it prints (kareem ashraf####) after deleting hashes from left only
name2 = '#@#@#@kareem ashraf#@#@#@'
print(name2.lstrip('#@')) # it prints (kareem ashraf#@#@#@) after deleting '#@' from left only

# string_name.title() : 
header = 'degital design and verification in 3d model'
print(header.title()) # expected output : Digital Design And Verification In 3D Model

# string_name.capitalize() : 
header = 'degital design and verification in 3d model'
print(header.capitalize()) # expected output : Digital design and verification in 3d model

a, b, c = '1', '12', '123'
print('before zfill()' , a, b, c) # prints : before zfill() 1 12 123
print('after zfill()' , a.zfill(4), b.zfill(4), c.zfill(4)) # prints : after zfill() 0001 0012 0123
print('1234'.zfill(3)) # prints 1234

# string_name.upper() : 
name = 'kareem ashraf'
print(name.upper()) # it prints : KAREEM ASHRAF

# string_name.lower() : 
name = 'KAREM AShraF'
print(name.lower()) # it prints : kareem ashraf

# string_name.split('character', N) : 
my_string = "kareem ashraf mostafa aboelala iprahim aboelala"
print(my_string.split()) # the list should be : ["kareem", "ashraf", "mostafa", "aboelala", "iprahim", "aboelala"]
my_string2 = "kareem-ashraf-mostafa-aboelala-iprahim-aboelala"
print(my_string2.split()) # the list should be : ["kareem-ashraf-mostafa-aboelala-iprahim-aboelala"], because the are no spaces
print(my_string2.split('-')) # the list should be : ["kareem", "ashraf", "mostafa", "aboelala", "iprahim", "aboelala"]
print(my_string2.split('-', 3)) # the list shoould be : ["kareem", "ashraf", "mostafa", "aboelala-iprahim-aboelala"]

# string_name.rsplit('character', N) : 
my_string = "kareem ashraf mostafa aboelala iprahim aboelala"
print(my_string.rsplit()) # the list should be : ["kareem", "ashraf", "mostafa", "aboelala", "iprahim", "aboelala"]
my_string2 = "kareem-ashraf-mostafa-aboelala-iprahim-aboelala"
print(my_string2.rsplit()) # the list should be : ["kareem-ashraf-mostafa-aboelala-iprahim-aboelala"], because the are no spaces
print(my_string2.rsplit('-')) # the list should be : ["kareem", "ashraf", "mostafa", "aboelala", "iprahim", "aboelala"]
print(my_string2.rsplit('-', 3)) # the list shoould be : ["kareem-ashraf-mostafa", "aboelala", "iprahim", "aboelala"]
        # Now, we can say that the diffiernce between (split(), rsplit()) apeares only it we use the maxsplit feature(N)

# string_name.center(N, 'character') :
name = "kareem"
print(name.center(10)) # name'll be wrapped with spaces : (  kareem  ). Two spaces before and after name
print(name.center(10, '@')) # name'll be wrapped with '@'s : (@@kareem@@)
print(name.center(11, '@')) # name'll be wrapped with '@'s : (@@@kareem@@). The odd-case forces the rest goes before name, not after it.

# string_name.count("string", index1, index2) : .
name = "kareem ashraf mostafa aboelala imprahim aboelala"
print(name.count("aboelala")) # it searches for "aboelala" in the whole string(name) and returns 2(# multiples)
print(name.count("aboelala", 0, 30)) # it searches for "aboelala" from name[0] to name[30] and returns 1, 
                                        # because the next"aboelala" isn't between naem[0:30]

# string_name.swapcase() : 
string1 = "kAREEM aSHRAF mOSTAFA"
string2 = "Kareem Ashraf Mostafa"
print(string1.swapcase()) # it'll print : Kareem Ashraf Mostafa
print(string2.swapcase()) # it'll print : kAREEM aSHRAF mOSTAFA

# string_name.startswith("string or character", index1, index2) : 
name = "kareem"
print(name.startswith('k')) # it'll print : True. Note that K != k (case sensitive)
print(name.startswith('kar')) # it'll print : True.
print(name.startswith('k', 1, 6)) # it'll print : False, becase 'k' isn't included between name[1:6].

# string_name.endswith("string or character", index1, index2) : 
name = "kareem"
print(name.endswith('m')) # it'll print : True. Note that M != m (case sensitive)
print(name.endswith('eem')) # it'll print : True.
print(name.endswith('m', 0, 5)) # it'll print : False, becase 'm' isn't included between name[0:5].
                                # knowing that the ending index isn't inclueded

# string_name.index("string or character", index1, index2) : 
string = "kareem ashraf mostafa"
print(string.index('r')) # it'll print : 2 which is the index for 'r' in "kareem".
print(string.index('r', 4, 12)) # it'll print : 10 which is the index for 'r' in "ashraf"
print(string.index('kareem')) # it'll print : 0, because it's the starting index of the string "kareem"
# print(string.index('A')) # ERROR : substring not found
# print(string.index('k', 3, 20)) # ERROR : substring not found, even it's found in the whole string but not foung in the limit indecies

# stirng_name.find("string or character", index1, index2) : 
string = "kareem ashraf mostafa"
print(string.find('r')) # it'll print : 2 which is the index for 'r' in "kareem".
print(string.find('r', 4, 12)) # it'll print : 10 which is the index for 'r' in "ashraf"
print(string.find('kareem')) # it'll print : 0, because it's the starting index of the string "kareem"
print(string.find('A')) # it will print -1
print(string.find('k', 3, 20)) # it will pring -1

# string_name.rjust(N, "character") : 
name = "kareem"
print(name.rjust(10, '@')) # it prints : @@@@kareem
# print(name.rjust(10, '@#')) # ERROR : it must be a single character
print(name.rjust(10)) # if the character isn't included, it'll placed by spaces: (    kareem)

# string_name.ljust(N, "character") : 
name = "kareem"
print(name.ljust(10, '@')) # it prints : kareem@@@@
# print(name.rjust(10, '@#')) # ERROR : it must be a single character
print(name.ljust(10)) # if the character isn't included, it'll placed by spaces: (kareem    )

# string_name.splitlines() : 
string = """first line
second line
third line
fourth line"""
print(string.splitlines()) # it prints : ['first line', 'second line', 'third line', 'fourth line']
print(type(string.splitlines())) # it prints : <class 'list'>

# string_name.expandtabs(tab size) : 
name = "kareem\tashraf\tmostafa\taboelala\tiprahim\taboelala"
print(name)
print(name.expandtabs(6))

# string_name.istitle() : 
string1 = "Kareem Ashraf Mostafa 3D"
string2 = "kareem ashraf mostafa 3d"
print(string1.istitle()) # it prints True (Boolean)
print(string2.istitle()) # it prints False (Boolean)
print(type(string2.istitle())) # it prints <class 'bool'>

# string_name.isspace() : 
string1 = " "
string2 = "   "
string3 = ""
print(string1.isspace()) # it prints True becase it consists of one space character
print(string2.isspace()) # it prints True becase it consists of multiple space characters
print(string3.isspace()) # it prints False because it's empty
print(type(string1.isspace())) # it prints <class 'bool'>

# string_name.islower() : 
name1 = "KAreem"
name2 = "kareem"
print(name1.islower()) # it'll print : False
print(name2.islower()) # it'll print : True

# string_name.isupper() : 
name1 = "KAreem"
name2 = "KAREEM"
print(name1.isupper()) # it'll print : False
print(name2.isupper()) # it'll print : True

# string_name.isidentifier() : 
id1 = "kareem_ashraf"
id2 = "kareemAshraf"
id3 = "kareem-ashraf"
print(id1.isidentifier()) # it'll print 'True'
print(id2.isidentifier()) # it'll print 'True'
print(id3.isidentifier()) # it'll print 'False' because '-' can't be included in an identifier name

# string_name.isalpha() : 
x = "aaaaaaaaaaaadddddddddddddfffff"
y = "aaaaaaa23adfegggggggggg33"
print(x.isalpha()) # it'll print 'True' 
print(y.isalpha()) # it'll print 'False' becase the string y consists of alphapitical characters and numbers too

# string_name.isalnum() : 
x = "aaaaaaaaaaaadddddddddddddfffff"
y = "aaaaaaa23adfegggggggggg33"
z = "asdfddddd223###@##dddddd"
print(x.isalnum()) # it'll print 'True' 
print(y.isalnum()) # it'll print 'True' 
print(z.isalnum()) # it'll print 'False' becase the string y consists of alphapitical characters and numbers and special characters like (#, @) too this isn't allowed

# string_name.replace("substring_old", "substring_new", replacement_count) : 
string = "kareem ashraf kareem mostafa kareem kareem"
print(string.replace("kareem", "KAREEM")) # it'll print : KAREEM ashraf KAREEM mostafa KAREEM KAREEM
                                          # replace all old values because replacement_count isn't included
print(string.replace("kareem", "KAREEM", 2)) # it'll print : KAREEM ashraf KAREEM mostafa kareem kareem

# "seperator".join(list_name or tuple_name) : 
my_list = ['kareem', 'ashraf', 'mostafa']
my_tuple = ('kareem', 'ashraf', 'mostafa')
print(" ".join(my_list)) # it'll print : kareem ashraf mostafa
print("-".join(my_tuple)) # it'll print : kareem-ashraf-mostafa