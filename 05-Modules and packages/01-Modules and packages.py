# Modules and packages
print('''Modules and packages''')

print('''Modules in Python are simply Python files with the .py extension, which implement a set of functions''')
# To import a module, we use the import command

# import the library
import math

# use it (ceiling rounding)
math.ceil(2.4)

print('''We can look for which functions are implemented in each module by using the dir function:''')
print(dir(math))

print('''We can read about it more using the help function, inside the Python interpreter:''')
help(math.ceil)

print(''' To create a module of your own, simply create a new .py file with the module name, 
and then import it using the Python file name (without the .py extension) using the import command.''')

print('''Packages are name-spaces which contain multiple packages and modules themselves.''')
print('''__init__.py. This file can be empty, and it indicates that the directory it contains is a Python package, 
so it can be imported the same way a module can be imported.\n''')

from Package import package_script
from Package.Subpackage import subpackage_script

package_script.package_function()
subpackage_script.subpackage_function()