# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 05 - Concept of the Module in python
# =====================================================

# A module is simply a Python file (.py) that contains variables, functions, classes, or other Python code.
#
# Instead of writing all your code in one file, you can divide it into multiple files according to their purpose.
#
# For example:
#
# Project
# │
# ├── main.py
# ├── mathematics.py
# └── student.py# main.py
#

# =====================================================
# Example 01 - Importing complete module.
# =====================================================
# Importing complete module.
import mathematics

answer1 = mathematics.add(10, 20)
answer2 = mathematics.subtract(30, 15)

print(answer1)
print(answer2)


# =====================================================
# Example 02 - Importing specific function.
# =====================================================
from mathematics import multiply

answer = multiply(5, 4)

print(answer)


# =====================================================
# Example 03 - Importing all functions.
# =====================================================
from mathematics import *

print(add(5, 3))
print(subtract(8, 2))

# =====================================================
# Example 04 - Importing using an Alias
# =====================================================
import mathematics as math

print(math.add(50, 30))