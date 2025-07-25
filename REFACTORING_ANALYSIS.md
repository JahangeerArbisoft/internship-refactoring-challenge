# Identifying Problems in the Codebase (mainly the python files)

There is no project structure in the codebase. All files are contained in a flat layout - they should be filtered into their respective directories. 

Poor naming of variable names - confusing with the global names.


## config.py
1. This file contains sensitive info related the APIs - not added to .gitignore file.
   It should never be in the version control system. 

## main.py
1. No docstrings present that explain the functionality of the methods.
2. Some modules are imported but haven't been used - unnecessary    imports.
3. API keys and other sensitive information is hardcoded - it should be passed from 
   a class that has been added to .gitignore.
4. Code not compliant with PEP 8 practices.
  - unequal spaces/indentation
  - redundant code, e.g. if val == True and not if val
  - unequal spaces when assigning values to variables
  - no blank line available after method declaration

## test_file.py
1. Wrong indentation - error in the code.
2. Class TestClass has mixed indentation.
3. badly_formatted_function() has no spaces when parameters passed.
4. badly_formatted_function() contains unnecessary indents.
5. long_line_function() contains more characters on a single line than 
   the requirement (79).
6. Unequal spaces when objects are made and methods are called.

# utils.py
1. Email validation should use a basic reusable function.
2. Password hashing should be consistent across codebase.