########################################################################################################################################################################################################
# ---------- File Handling ----------
# -----------------------------------
# file = open("file/path", "Mode")
# 
# Mode Options: 
# ------------
# [1] => "r" stands for 'Read'  : (Default Value) opens the file to read from it and prevent any write operations. It gives an error if the file desn't exist
# [2] => "w" stands for 'Write' : opens the file to overwrite on it. It creates the file if it doesn't exist
# [3] => "a" stands for 'Append': opens the file to append data to it without deleting the existing data. It creates the file if it doesn't exist  
# [4] => "x" stands for 'Create': creates the file. It gives an error if the file exists
# 
# Relative vs Absolute path: 
# -------------------------
# Relative: Path of your file from your relative to your working directory. e.g., working dir: F:\GitHub\Python, Relative path: ".\myfile.json"
# Absolute: Full path of your file from the working disk. e.g., whatever your working directory, Absolute path: "F:\GitHub\python\myfile.json" 
# 
# Some Useful Methods From "os" Module: 
# ------------------------------------
# First of all, we must write this line of code ("import os"), to call the operating system module
# Method_1  => os.gitcwd()  : returns the current working directory
# Method_2  => os.chdir()   : changes the working directory
# Method_3  => os.path.abspath(__file__)    : returns the absolute path to your working file (working file: file you run this command at it)
# Method_4  => os.path.relpath(__file__)    : returns the relative path to your working file relative to current working directory
# Method_5  => os.path.basename(__file__)   : returns the name of the working file. e.g., file_handling.py
# 
# Some NOTEs: 
# ----------
# NOTE  => if you add 'r' before typing your path, any escape sequence character will be prevented to do its jop
#           e.g., os.chdir(r"F:\GitHub\python\files\nfiles\myfile.json) : '\n' will be prevented to break the line as expected and the path will be taken as it's written,
# 
# ----------------------------------------- File Read -----------------------------------------
# ---------------------------------------------------------------------------------------------
# myfile = open("F:\GitHub\python\learn\kareem.txt", "r")   => Open The File
# print(myfile) => prints an object of the file data such as (name, mode, encoding). Type of this object: <class '_io.TextIOWrapper'> 
# print(myfile.name)    => prints the name of your file with its relative path
# print(myfile.mode)    => prints the mode of your file e.g., "r"
# print(myfile.encoding)=> prints the encoding of your file e.g., cp1252
# myfile.read(n)        => returns the first 'n' characters in your file
# myfile.read()         => returns the all data of your file
# myfile.readline(n)    => returns the first 'n' characters in your filee as lines
# myfile.readline()     => returns the first line in your file
# myfile.readlines(n)   => returns the first lines in your file which their total length doesn't exceede 'n' characters as a list of lines
#   NOTE: the items of the list must be a complete line not a part of a line
#   NOTE: e.g., if the first 3 lines total length = 28 and 'n' = 30, then the returned list will be a list of the first 3 lines only
# myfile.readlines()    => returns a list of all lines in your file 
# myfile.close()        => close the file (this is the best practise)             
# NOTE: we can loop on the file and the iterable will be a list of lines   
# 
# ----------------------------------------- File Write -----------------------------------------
# ----------------------------------------------------------------------------------------------
# myfile = open("F:\GitHub\python\learn\kareem.txt", "w")   => Open The File Or Create it if not exist
# myfile.write("Text")  => This function overwrites the on your file. It resets your file first then writes your text
# myfile.writelines(yourlist)   => This overwrtes on your file with the list items as lines 
#
# ----------------------------------------- File Append -----------------------------------------
# -----------------------------------------------------------------------------------------------
# myfile = open("F:\GitHub\python\learn\kareem.txt", "w")   => Open The File Or Create it if not exist
# myfile.write("Text")  => This function writes to your file from the cursor (The basic meaning of appending)
# myfile.writelines(yourlist)   => This writes to your file from the cursor with the list items as lines
# 
# myfile.tell()     => returns the index of the cursor (file pointer)
# myfile.seek(n)    => moves the index of the cursor to the index 'n'
# myfile.truncate(n)=> truncates (erases) file content from index 'n'. NOTE: if 'n' not exist it truncates the file from the cursor index
# os.remove("file/path/relative/or/absolute")   => this command delete the file to this path
# 
# --------------------  Mode vs Mode+ --------------------
# --------------------------------------------------------
# [1] => "r "   : When you only need to read from an existing file
# [2] => "r+"   : When you need to read and modify an existing file
# [3] => "w "   : When you creating a new file or overwriting completely for an existing one
# [4] => "w+"   : When you want to create / overwrite / read-back from it
# [5] => "a "   : When you creating a new file or appending to the end of existing one
# [6] => "a+"   : When you want to create / appen / read-back from it
# [7] => "a "   : When you want to ensure that you've created a new file
# 
########################################################################################################################################################################################################


# import os

# print(os.getcwd())                  # f:\GitHub\python

# print(os.path.dirname(__file__))    # f:\GitHub\python\learn
# print(os.path.abspath(__file__))    # f:\GitHub\python\learn\file_handling.py
# print(os.path.relpath(__file__))    # learn\file_handling.py


# # File Read


# file = open(r"learn\function.py", "r")

# myfile = open("learn\kareem.txt", "r")
# print('*' * 50)
# print(myfile)           # <_io.TextIOWrapper name='learn\\kareem.txt' mode='r' encoding='cp1252'>
# print(type(myfile))     # <class '_io.TextIOWrapper'>
# print(myfile.name)      # learn\kareem.txt | relative path relative to the current working directory
# print(myfile.mode)      # r | Read
# print(myfile.encoding)  # e.g, cp1252

# myfile.close()
# myfile = open("learn\kareem.txt", "r")
# print(myfile.read(10))  # reads just 10 bytes from the first of the file
# print(myfile.read())    # reads the rest of the file

# myfile.close()
# myfile = open("learn\kareem.txt", "r")
# print(myfile.readline())    # reads the first line 
# print(myfile.readline())    # reads the second line
# print(myfile.readline())    # reads the third line
# print(myfile.readline(5))   # reads the first 5 characters (bytes) from the fourth line
# print(myfile.readline())    # reads the rest of the fourth line

# myfile.close()
# myfile = open("learn\kareem.txt", "r")
# print(myfile.readlines(30))         # prints a list of lines which total length of the printed lines in the list doesn't exceede 30 characters
# print(myfile.readlines())           # prints a list with all the rest lines in your file
# print(type(myfile.readlines()))     # <class 'list'>

# myfile.close()
# myfile = open("learn\kareem.txt", "r")
# for line in myfile:     # prints all lines of your file until the line starts with '05'
#     print(line)
#     if line.startswith('05'): break

# myfile.close()



# # File Write 

# myfile = open("learn/writefile.txt", "w")       # Opens 'writefile.txt', Creates it if it doesn't exist
# # print(os.path.abspath('learn/writefile.txt'))
# myfile.write("01 => Kareem Ashraf Mostafa\n")
# myfile.write("02 => Junior student engineer at Electronics & Electrical Communication Department, Cairo University\n")
# myfile.write("03 => E-Mail: kareem.ash05@gmail.com\n")
# myfile.write("05 => GitHub: https://github.com/kareem05-ash\n")
# myfile.write("06 => Linkedin: https://www/linkiedin/in/kareemashraf05\n")
# myfile.write("07 => Phone: +201002321067 / +201154398353\n")
# for x in range(8, 21):
#     myfile.write(f"{str(x).zfill(2)} => The Repeated Line\n")

# herfile = open("learn/she.txt", "w")
# herlist = ['first line\n', 'second line\n', 'third line\n']
# # for line in herlist: herfile.write(line)
# herfile.writelines(herlist)     # This line does the same function of the previous one. Looping on the list and write each item in the list as a line in your file


# # File Append

# myfile = open("learn/append_file.txt", "a")
# myfile.write("My First Append File\n")
# myfile.write("my first append file\n".upper())

# mylist = ['first\n', 'second\n', 'third\n']
# myfile.writelines(mylist)




# write_data_file = open("learn/data.txt", "w")       # Creates a file to store data in it
# write_data_list = ['1st\n', '2nd\n', '3rd\n']
# write_data_file.writelines(write_data_list)
# # write_data_file.close()

# read_data_file = open("learn/data.txt", "r")        # Opens the file to read from it
# print(read_data_file.read())
# read_data_file.close()

# print(write_data_file.tell())   # 15 because each line contains 3 characters but the new line is considered as 2 characters so total = 3*3 + 2*3 = 15
# # write_data_file.seek(5)
# write_data_file.truncate(2)     # delete all data from pointer 2 (we have just 2 characters in our file)
# write_data_file.close()

# print('File has been reseted')
# read_data_file = open("learn/data.txt", "r")
# print(read_data_file.read())



# import os
# file = open("learn/tobedeleted.txt", "x")   # creates a file
# file.close()                                # closes the file
# os.remove("learn/tobedeleted.txt")          # removes the file