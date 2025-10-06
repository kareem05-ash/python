######################################################################################################################################################
# ******************** Object Oriented Programming (OOP) ********************
# ---------------------------------------------------------------------------
# __________________________________ Class __________________________________
# ___________________________________________________________________________
# NOTE - Class is the blueprint or the constructor of the object. In other word, class is the mum of objects
# NOTE - Class is formed with attributes & methods
#   Attributes  -> Each object from the class has its attributes
#   Methods     -> Available built-in methods (over your class scope) can be used by any object from the class\
# NOTE - Class is defined by keyword 'class' as: class YourClassName: 
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
# ----- Class Attributes & Methods ------
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
# __eq__        -> e.g., inst1.__eq__(inst2)
#                   NOTE - It returns true if inst1 is the same as inst2
#                   NOTE - The equality check is fully confugurable (by you)
#                   NOTE - If it's not defined, the default equality will be as instanses addresses (default python equality)
#                                        
# ------- Usefull Methods -------
# -------------------------------
# isinstance(object, class)     -> It takes 2 parameters (object, class)
#                               -> It returns true if this object is an instance of this class
#                               -> It returns false if this object isn't an instance of this class
# ClassName.mro()               -> It returns the order of inherted Parent classes
#   e.g., Child.mro()   => returns: [<class ' __main__.Child'>, <class ' __main__.Parent2'>, <class ' __main__.Parent2'>, <class 'object'>]
# ------------------ Inheritance ---------------------
# ----------------------------------------------------
# NOTE - There are more than one type of inheritance: Simple Inheritance, Multiple Inheritance, 
#   [1] Simple Inheritance      -> class Child(Parent): Child inherits all Parent methods and attributes
#   [2] Multiple Inhertiance    -> class Child(Parent1, Parent2): Child inherits all Parent1 and Parent2 mehtods and attributes
#       NOTE - Child class inherits matched methods or attributes from Parent1 not Parent2 as your order {class Child(Parent1, Parent2)}
#       NOTE - To get the order of inherited parent class, use mro() methods
#       NOTE - If a sub child class inherts from a child class which child inherts from parent then sub child class inherts all parent and child methods and attributes
# NOTE - Child class can access any method in Parent class
# NOTE - Child instanses can access any Parent instanse attribute by passing the attribute to __init()__ through super() method
# 
# e.g., 
#       class Parent:
#           def __init__(self, parent_attr):
#               self.parent_attr = parent_attr
#       
#       class Child(Parent):
#           def __init__(self, parent_attr, child_attr):
#               super().__init__(parent_attr)
#               self.child_attr = child_attr
#  
# -------- Polymerphism ---------
# -------------------------------
# NOTE - Polymerphism is to give any method_name more than one behaviour
#           e.g., len([1, 2, 3]) , len("kareem") >> len() at the first ex returns the number of list items but in the second ex returns the number of characters which is different behavioud. So, len() is polymerphism
# NOTE - To implement polymerphism in Inherted classes, just define override methods in Child class
#           = In Parent scope, this method does something but in Child scope this method does something else  
# 
# ----------------------------- Encapsulation ------------------------------
# --------------------------------------------------------------------------
# There are 3 types of attributes in classes:
# [1] => Public:
#       - Every attribute and method which its name doesn't begins with '_' or '__' is puplic
#       - Every public attributes and methods can be modified from anywhere
# [2] => Protected:
#       - Every attribute and method can be protected if its name begins with '_' e.g. self._name = name
#       - Every protected attribute and method can be accessed from anywhere but it just has name like (_attr) to tell others that this attribute is protected
# [3] => Private:
#       - Every attribute and method can be private if its name begins with '__' e.g., self.__name = name
#       - Every private attribute and method can be accessed and modified from the calss itself (cls) only     
#           NOTE - We can access private attribtes or methods as:
#               e.g., print(inst1._MyClass__total_members) 
# 
# 
# ----------------------------- Getter & Setter --------------------------
# ------------------------------------------------------------------------
# - Getter: is a method inside the class which access the private data and return it
# - Setter: is a method inside the class which access the private data and set new values to this data
#  
# 
# ------------- @property Decorator -----------
# ---------------------------------------------
# - We can define instanse methods under @property decorator in case of this method doesn't take any parameter (uless self)
# - If we defined it under @property decorator, we call this function as an property (attribute) no method (without paranthesis)
#       e.g., @property
#             def property_func(self):
#                   return 1000
#        print(property_func)       # This is valid and prints: 1000
#        print(property_func())     # This is NOT valid and releases TypeError 'object isn't callable'  
# 
# --------------- ABCs -> Abstract Base Class ----------------
# ------------------------------------------------------------
# NOTE - ABC is a base class which all its sub-classes has to follow its orders
# NOTE - Any sub-class from ABC has to override the abstract method in ABC
# - First of all, we need to import from (abc) moduel "ABSMeta", "abstractmethod"
# - ABCMeta is used to define metaclass for your class (which intended to be ABC) by "ABCMeta"
# - Methods to be abstract methods has to be defined under "abstractmethod" decorator
#   e.g., 
# from abc import ABCMeta, abstractmethod
# class MyABC(metaclass = ABCMeta):
#     @abstractmethod
#     def my_abc_method(self): pass
# class Child1(MyABC):
#     def my_abc_method(self):
#         return 'NO'
# class Child2(MyABC):
#     def my_abc_method(self):
#         return 'YES'                                                                                                        #
######################################################################################################################################################

# # __________________________________ Class __________________________________
# print('_' * 35, 'Class', '_' * 35)


# # class MyFirstClass:
# #     def __init__(self):
# #         print("New Instance's Been Created")
# #     def method1(self, name):
# #         print(f"Hello, {name}")

# # mem1 = MyFirstClass()
# # print(mem1)
# # mem2 = str()
# # print(type(mem2))           # <class 'str'>
# # mem1.method1('Kareem')
# # print(mem1.__class__)       # <class '__main__.MyFirstClass'>
# # print(mem2.__class__)       # <class 'str'>


# class Member:
#     # Class Attributes
#     user_count = 0
    
#     # Class Methods
#     @classmethod
#     def get_user_count(cls):
#         return cls.user_count
    
#     # Static Methods
#     @staticmethod
#     def say_hello():
#         print("Hello, World!")

#     # Instance Methods
#     def __init__(self, fname, mname, lname):
#         # Instance Attributes
#         self.fname = fname
#         self.mname = mname
#         self.lname = lname
#         Member.user_count += 1      # Increment users counter

#     def __str__(self):
#         return f"Member {self.full_name()}"
    
#     def __len__(self):
#         return len(self.full_name())
        
#     def full_name(self):
#         return f"{self.fname} {self.mname} {self.lname}"

    
# # mem1 = Member('Kareem', "Ashraf", 'Mostafa')        # Hello, Kareem Ashraf Mostafa
# # print(mem1.full_name)       # Kareem Ashraf Mostafa
# # print(dir(mem1))            # full_name is already there

# # Member.say_hello()
# # user1 = Member('Kareem', 'Ashraf', 'Mostafa')
# # user2 = Member('Mohame', 'Ahmed', 'Mahmoud')
# # user3 = Member('Ali', 'Hassan', 'Mohamed')
# # user4 = Member('Sayed', 'Ali', 'Mostafa')
    
# # print(Member.full_name(user1))      # Kareem Ashraf Mostafa
# # print(user1.full_name())            # Kareem Ashraf Mostafa
# # print(Member.get_user_count())      # 4
# # print(user1.get_user_count())       # 4


# # print(len(user1))       # prints the length of user1 full_name length
# # print(user1)            # Member Kareem Ashraf Mostafa
# #     # NOTE - this would print something like <__main__.Member object at 0x000023423afc32>
# #                 # this isn't human readable. 
# #                 # So, we use __str__ method to return some readable text which printed once instance is passed to print() built-in function


# class Food:             # Parent Class
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name}'s been created from parent class")
#     def eat(self):
#         print("Eat method from parent class")

# class Apple(Food):      # Child Class
#     def __init__(self, name):
#         super().__init__(name)
#         print(f"{self.name}'s been created from child class")
        
#     def get_from_tree(self):
#         print('Get From Tree From Child Class')

# from_food = Food('Banana')
# from_apple = Apple('Apple')

# from_apple.eat()
# from_apple.get_from_tree()



# class Member:
#     def __init__(self, name):
#         self.__name = name


# mem1 = Member("Kareem")

# # print(mem1.__name)      # Objet has no atttribute '__name' (can't be accessed)

# print(mem1._Member__name)   # Here, it's accessed (Kareem)



# class Member:
#     @property
#     def num(self):
#         return 1000
    

# one = Member()
# # print(one.num())  # TypeError: 'int' object is not callable
# print(one.num)      # 1000