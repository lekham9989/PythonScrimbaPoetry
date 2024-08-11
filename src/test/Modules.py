# MODULES
# Similar kind of functions can be kept at one file or place called 'Modules'
# We can call a already defined function existing in a particular module by importing the 'Module'
# ex: for modules are datetime, random, os, browser,math etc
# to import modules, we need to change something in index file, use the bigger library brython std lib

import platform
# keyword-import moduleName

# check what a module does when you import it - gives all the methods inside the module
print(dir(platform))

# check the python version of platform module
print(platform.python_version())

# import 2 or more modules
import string,os
print(dir(string))
print(dir(os))

# to shorten the module name
import platform as pl
print(pl.python_version())

# to make our work more simpler, we can import functions directly
from platform import python_version, system
print(python_version())
print(system())

# we can add alias name to function as well
from platform import python_version as pv
print(pv())