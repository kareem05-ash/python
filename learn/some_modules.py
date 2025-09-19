######################################################################################################################################################
# ******************** This File Contains Some Important Modules And Built-In Functions ********************
# **********************************************************************************************************
# -------------------- zip() Built-In Function --------------------
# -----------------------------------------------------------------
# [1] - It returns a zip object which contains all input objects
# [2] - Its length is the same as the smallest length of the input objects
# [3] - It can take any object as an input. e.g., zip(mylist, mytuplt, mydict, mystr)
# -------------------- PIL Built-In Module For Image Manuplation --------------------
# -----------------------------------------------------------------------------------
# [1] - This is a toturial link for pillow module: [https://hugovk-pillow.readthedocs.io/en/stable/handbook/tutorial.html]
# [2] - Frist Of All, we need to install this package by this command: [pip install pillow] to your terminal
# [3] - After Installation, we've to import 'Image' fro 'PIL' module: from PIL import Image
# [4] - There are many methods at this package::
#   (1) - myImage = Image.open("image\\path"): first, we need to open our image
#   (2) - myImage.show(): this method shows the image
#   (3) - myCroppedImage = myImage.crop((left, top, right, bottom)): this method cropes your image. e.g., new = myImage.crop((300, 300, 800, 800))
#   (4) - greyImage = myImage.convert("L"): this method converts your image to black-white mode
#   (5) - There are many methods you can check what you want to use in the previous provided link at Line_9
# -------------------- Doc String & Commenting vs. Documenting --------------------
# --------------------------------------------------------------------------------- 
# [1] - Commenting can be accessed by '#' character. This is for you and to make your code is more readable
# [2] - Documenting is used for the more complex funcitons 
# [3] - Documenting can be accessed by tripple quotes ('''Your Documentation''' or """Your Documentation""")
#       NOTE - We can read the function documentation using help() method or __doc__                                                    # 
######################################################################################################################################################

# # -------------------- zip() Built-In Function --------------------
# print(f"# -------------------- zip() Built-In Function --------------------")
# names = ['Kareem', 'Ashraf', 'Mostafa', 'Aboelala', 'Ipraheem']
# nums = [1, 2, 3]

# compressed_data = zip(nums, names)
# print(compressed_data)          # <zip object at 0x000....>
# print(type(compressed_data))    # <class 'zip'>

# for item in compressed_data: print(type(item), item)
# # Output:: 
# # <class 'tuple'> (1, 'Kareem') 
# # <class 'tuple'> (2, 'Ashraf') 
# # <class 'tuple'> (3, 'Mostafa') 
# # NOTE - The last 2 names havn't been printed as, the length of zip object is only 3 as the length of nums (the smallest object)

# user_data = {
#     'name': 'Kareem Ashraf', 
#     'age': 20, 
#     'coutry': 'Egypt'
# }
# letters5 = ('A', 'B', 'C', 'D', 'F')
# letters3 = ('A', 'B', 'C')
# letters2 = ('A', 'B')

# print(f"This is from letter5")
# for letter, (key, value) in zip(letters5, user_data.items()):
#     print(f"{letter} - User({key}) => {value}")

# print(f"This is from letter3")
# for letter, (key, value) in zip(letters3, user_data.items()):
#     print(f"{letter} - User({key}) => {value}")

# print(f"This is from letter2")      # Here, User(coutry)'s not been printed as the length of lettter2 is just 2
# for letter, (key, value) in zip(letters2, user_data.items()):
#     print(f"{letter} - User({key}) => {value}")

# # -------------------- PIL Built-In Module For Image Manuplation --------------------
# print("# -------------------- PIL Built-In Module For Image Manuplation --------------------")
# from PIL import Image
# # first we need to open our image
# myimage = Image.open("game.jpg")

# # show the image
# myimage.show()

# -------------------- Doc String & Commenting vs. Documenting --------------------
print("# -------------------- Doc String & Commenting vs. Documenting --------------------")

def sayhello(name): 
    ''''
This function says hello to the person who the input name is his name
Parameters: 
    name: <class 'str'>, the person name 
return: 
    msg: hello message to input person name    
    '''
    print(f"Hello, {name}!, Good to see you from Kareem function")

sayhello("Mohamed")     # this is the ordinary use of functions

help(sayhello)              # prints a guide to use this function what contains our documentation
print(dir(sayhello))        # prints the methods can be used for this function
print(sayhello.__doc__)     # prints our documentation only