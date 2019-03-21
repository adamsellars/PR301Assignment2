"""
# ---------------------------------------------Created by Adam----------------------------------
# Testing greeting and help messages work as expected
>>> cmd = CommandLineInterpreter(Controller(ClassFinder(), View()))
# Test 1
>>> cmd.do_greet("line")
==================================================
Welcome to the command line interpreter.
Type help to view available commands
==================================================
<BLANKLINE>

# Test 2
>>> cmd.do_help("")
<BLANKLINE>
Documented commands (type help <topic>):
========================================
greet  help  load_file  print_file  quit  write_file
<BLANKLINE>

# Test 3
>>> cmd.do_help("greet")
==================================================
greet command help
==================================================
Description: A Greeting message
Syntax: greet
Parameter: none
Example: greet
<BLANKLINE>

# Test 4
>>> cmd.do_help("help")
List available commands with "help" or detailed help with "help cmd".

# Test 5
>>> cmd.do_help("load_file")
==================================================
load_file command help
==================================================
Description: Load a .txt file into the program
Syntax: load_file [path]
Parameter: [path] = full path name of the file starting from the root directory of this program
Example: load_file test4(myowncode).txt
<BLANKLINE>

# Test 6
>>> cmd.do_help("quit")
==================================================
quit command help
==================================================
Description: terminate the command line interpreter
Syntax: quit
Parameter: none
Example: quit
<BLANKLINE>

# Test 7
# surprise.txt doesn't exist should get an error message
>>> cmd.do_load_file("surprise.txt")
Error, file does not exist!

# Test 8
# this file does exist should get a success message
>>> cmd.do_load_file("test4(myowncode).txt")
<BLANKLINE>
file loaded...
<BLANKLINE>

>>> cmd.do_quit("")
Goodbye thank you for using the command line interpreter
True
"""

from View import View
from ClassFinder import ClassFinder
from Runner import Controller
from Runner import CommandLineInterpreter
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    doctest.testmod(verbose=True)
