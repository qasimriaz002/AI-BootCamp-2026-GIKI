# =====================================================
# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)
# =====================================================
#
# Lecture 04 - Type Casting
# =====================================================

#
# Sometimes we need to convert one data type into another.
#
# This process is called
#
# Type Casting
#

# -----------------------------------------------------
# Integer to Float
# -----------------------------------------------------

age = 20

print(age)

new_age = float(age)

print(new_age)

#
# Observe
#
# 20 becomes
#
# 20.0
#

# -----------------------------------------------------
# Float to Integer
# -----------------------------------------------------

cgpa = 3.89

print(cgpa)

new_cgpa = int(cgpa)

print(new_cgpa)

#
# Observe
#
# Decimal part is removed.
#

# -----------------------------------------------------
# Integer to String
# -----------------------------------------------------

marks = 95

print(marks)

marks_text = str(marks)

print(marks_text)

#
# Now marks_text is TEXT.
#

# -----------------------------------------------------
# String to Integer
# -----------------------------------------------------

roll_number = "101"

print(roll_number)

roll_number = int(roll_number)

print(roll_number)

#
# Observe
#
# "101"
#
# becomes
#
# 101
#

# -----------------------------------------------------
# Boolean Conversion
# -----------------------------------------------------

print(bool(1))

print(bool(0))

print(bool("Python"))

print(bool(""))

#
# Observe
#
# 1         -> True
# 0         -> False
#
# Non-empty string -> True
#
# Empty string -> False
#

# -----------------------------------------------------
# Checking Data Types
# -----------------------------------------------------

number = 50

print(type(number))

number = float(number)

print(type(number))

number = str(number)

print(type(number))