######################################################################################################################################################
# ******************** Object Oriented Programming (OOP) ********************
# ---------------------------------------------------------------------------
# __________________________________ Class __________________________________
# ___________________________________________________________________________
# NOTE - Class is the blueprint or the constructor of the object. In other word, class is the mom of objects
# NOTE - Class is formed with attributes & methods
#   Attributes  -> Each object from the class has its attributes
#   Methods     -> Available built-in methods (over your class scope) can be used by any object from the class\
# NOTE - Class is defined by keyword 'class' as: class YourClassNmae: 
# NOTE - Class name has to be written in PascalCase (UpperCamelCase) style. e.g., class MyFirstClass:
# NOTE - Instance is an object from the class
# NOTE - __init__ dunder/magic_method (built-in method) is considered the constructor method of the class
# NOTE - __init__ is called each time you create an instance from the class
# NOTE - __init__ main function is to initialize object data
# NOTE - __init__ has to take at least one parameter usually is called "self"
# NOTE - In case of __init__ takes more than one paramter, "self" parameter has to be the first one
# NOTE - your_object.__class__ returns the type of this object
#   e.g., mem1 = str(); print(mem1.__class__)       # prints: <class 'str'>
#   e.g., mem2 = MyCalss(); print(mem2.__class__)   # prints: <class '__main__.MyClass'>
# 
# ----- Instance Attributes & Methods ------
# ------------------------------------------
# Instance Attributes are defined inside the constructor (__init__)
# Instance Attributes are defined as (self.attribute_name = attribute_value)
# Instance Methods take 'self' parameter which points to the instance
# Instance Methods can have more than one parameter like any function
# Instance Methods can access the class itself
# ----- Class Attibutes & Methods ------
# --------------------------------------
# Class Attributes are defined inside the class scope (at the same level of __init__ method)
# Class Methods must be defined under '@classmethod' decorator
# Class Methods must take 'cls' as the most first parameter
# Class Methods can take more than one parameter, keeping 'cls' as the first one
# ------ Static Methods ------
# ----------------------------
# Static Methods isn't bunded with the class or the instance
# Static Methods must be defined under '@staticmethod' decorator
# Static Methods can take any number of parameters
# 
# ------- Magic Methods (Dunders) -------
# ---------------------------------------
# __init__      -> is called automatically once the class's been instantiated
# self.__class__-> returns the class to which the class instance belongs
# __str__       -> Gives a human readable output of the ojbect (the class instanse)
#                   NOTE - If we print(instanceName), it'll print something isn't readable 
#                   NOTE - We use __str__ method to return some readable content about the instance
# __len__       -> It returns the length of the container,
#                   NOTE - It's called when we use built-in function len(your_ojbect/instance)
#                                                                                                                                                      #
######################################################################################################################################################

# __________________________________ Class __________________________________
print('_' * 35, 'Class', '_' * 35)


# class MyFirstClass:
#     def __init__(self):
#         print("New Instance's Been Created")
#     def method1(self, name):
#         print(f"Hello, {name}")

# mem1 = MyFirstClass()
# print(mem1)
# mem2 = str()
# print(type(mem2))           # <class 'str'>
# mem1.method1('Kareem')
# print(mem1.__class__)       # <class '__main__.MyFirstClass'>
# print(mem2.__class__)       # <class 'str'>


class Member:
    # Class Attributes
    user_count = 0
    
    # Class Methods
    @classmethod
    def get_user_count(cls):
        return cls.user_count
    
    # Static Methods
    @staticmethod
    def say_hello():
        print("Hello, World!")

    # Instance Methods
    def __init__(self, fname, mname, lname):
        # Instance Attributes
        self.fname = fname
        self.mname = mname
        self.lname = lname
        Member.user_count += 1      # Increment users counter

    def __str__(self):
        return f"Member {self.full_name()}"
    
    def __len__(self):
        return len(self.full_name())
        
    def full_name(self):
        return f"{self.fname} {self.mname} {self.lname}"

    
# mem1 = Member('Kareem', "Ashraf", 'Mostafa')        # Hello, Kareem Ashraf Mostafa
# print(mem1.full_name)       # Kareem Ashraf Mostafa
# print(dir(mem1))            # full_name is already there

# Member.say_hello()
# user1 = Member('Kareem', 'Ashraf', 'Mostafa')
# user2 = Member('Mohame', 'Ahmed', 'Mahmoud')
# user3 = Member('Ali', 'Hassan', 'Mohamed')
# user4 = Member('Sayed', 'Ali', 'Mostafa')
    
# print(Member.full_name(user1))      # Kareem Ashraf Mostafa
# print(user1.full_name())            # Kareem Ashraf Mostafa
# print(Member.get_user_count())      # 4
# print(user1.get_user_count())       # 4


# print(len(user1))       # prints the length of user1 full_name length
# print(user1)            # Member Kareem Ashraf Mostafa
#     # NOTE - this would print something like <__main__.Member object at 0x000023423afc32>
#                 # this isn't human readable. 
#                 # So, we use __str__ method to return some readable text which printed once instance is passed to print() built-in function
