# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 01 - Operators
# =====================================================

# Operators are special symbols in Python that perform
# different operations on variables and values.
#
# Python provides different types of operators such as:
# 1. Arithmetic Operators
# 2. Relational (Comparison) Operators
# 3. Logical Operators

# =====================================================
# Example 01 - Arithmetic Operators
# =====================================================

# Arithmetic operators are used to perform mathematical operations.

num1 = 20
num2 = 6

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus (Remainder):", num1 % num2)
print("Power:", num1 ** num2)

# =====================================================
# Example 02 - Arithmetic Operators with User Variables
# =====================================================

english = 85
math = 90
computer = 88

total_marks = english + math + computer

average_marks = total_marks / 3

print("\nTotal Marks:", total_marks)
print("Average Marks:", average_marks)

# =====================================================
# Example 03 - Relational (Comparison) Operators
# =====================================================

# Relational operators compare two values.
# The result is always either True or False.

num1 = 15
num2 = 10

print("\nnum1 == num2 :", num1 == num2)
print("num1 != num2 :", num1 != num2)
print("num1 > num2  :", num1 > num2)
print("num1 < num2  :", num1 < num2)
print("num1 >= num2 :", num1 >= num2)
print("num1 <= num2 :", num1 <= num2)

# =====================================================
# Example 04 - Relational Operators in Real Life
# =====================================================

marks = 72
passing_marks = 50

print("\nHas Student Passed?", marks >= passing_marks)

# =====================================================
# Example 05 - Logical Operators (AND)
# =====================================================

# AND returns True only if both conditions are True.

age = 20
cgpa = 3.45

print("\nEligible for Scholarship:", age >= 18 and cgpa >= 3.00)

# =====================================================
# Example 06 - Logical Operators (OR)
# =====================================================

# OR returns True if at least one condition is True.

attendance = 80
medical_certificate = False

print("\nCan Appear in Exam:",
      attendance >= 75 or medical_certificate == True)

# =====================================================
# Example 07 - Logical Operator (NOT)
# =====================================================

# NOT changes True into False and False into True.

is_logged_in = True

print("\nUser Logged In:", is_logged_in)
print("User Logged Out:", not is_logged_in)

# =====================================================
# Example 08 - Combining Relational and Logical Operators
# =====================================================

age = 22
marks = 78

eligible = age >= 18 and marks >= 60

print("\nEligible for Admission:", eligible)

# =====================================================
# Example 09 - Practical Example
# =====================================================

student_name = "Ali"
marks = 84
attendance = 88

# Student will pass if marks are greater than or equal to 50
# AND attendance is greater than or equal to 75.

result = marks >= 50 and attendance >= 75

print("\nStudent Name:", student_name)
print("Marks:", marks)
print("Attendance:", attendance)
print("Pass Status:", result)