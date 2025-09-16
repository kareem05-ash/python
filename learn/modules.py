########################################################################################################################################################################################################
# -------------------- Modules & Packages --------------------
# ------------------------------------------------------------
# ** Built-In Modules **
# NOTE - We can import the whole module to use all its methods. e.g., import os; os.path.dirname()
# NOTE - We can import a specific method from any module. e.g., from random import randint; randint(100, 300)
# NOTE - We can import multiple modules in the same file. e.g., import os, random, functools
# NOTE - We can import multiple methods from a specific module. e.g., from random import random, randint, randrange 
# NOTE - We can import all the methods from a specific module using '*'. e.g,. from os import *
# ** User Defined Modules **
# NOTE - We should add path of the module directory first to resolve the module
# NOTE - We can use method 'dir(module_name)' to show the supported methods in the module
# NOTE - We must type this line before any module calling: import sys; sys.path.append(r"the\path\to\module\dir")
# ** Install External Packages ** 
# NOTE - Modules are a single py file with some methods. Packages are set of modules
# NOTE - We can install external packages py this command: pip install package_name/module_name
# NOTE - We can updates the version of any package or module by this command: pip install package_name/module_name --upgrade
# NOTE - There're many external packages such as: {pyfiglet, termcolor, etc....}
#       NOTE - termcolor => Using Method colored(text, color, , , ) In It, we can configure the font color, background, style and so on.. 
#       NOTE - pyfiglet  => Using Method figlet_format(text) In It, we can restyle the text                                                                                                                                                         # 
########################################################################################################################################################################################################

# Built-In Modules
from random import randint, random
print(f"Random Float Number: {random()}")
print(f"Random Integer Number: {randint(10, 100)}")
# import random
# print(random)

# User Modules
import sys
sys.path.append("F:\GitHub\python\modules")
print(sys.path)

import kareem as mine
mine.sayhello('kareem')
mine.sayloveu('kareem')
mine.sayhowru('kareem')

print(dir(mine))

import pyfiglet
import termcolor
print(pyfiglet.figlet_format("Kareem"))
print(termcolor.colored(pyfiglet.figlet_format("Kareem Ashraf"), (255, 0, 255), 'on_black', ['bold', 'blink']))