# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 02 - Conditional Statements
# =====================================================

# Conditional statements are used to make decisions in a program.
# The program checks whether a condition is True or False.
# If the condition is True, one block of code is executed.
# Otherwise, another block of code may execute.

# =====================================================
# Example 01 - Simple if Statement
# =====================================================

# The statements inside the if block execute only if the
# condition is True.

marks = 75

if marks >= 50:
    print("Congratulations! You have passed the exam.")

# =====================================================
# Example 02 - if Statement with Multiple Conditions
# =====================================================

age = 20

if age >= 18:
    print("You are eligible to apply for a driving license.")

# =====================================================
# Example 03 - if else Statement
# =====================================================

# If the condition is True, the if block executes.
# Otherwise, the else block executes.

marks = 42

if marks >= 50:
    print("You Passed.")
else:
    print("You Failed.")

# =====================================================
# Example 04 - Checking Even or Odd Number
# =====================================================

number = 17

if number % 2 == 0:
    print(number, "is an Even Number.")
else:
    print(number, "is an Odd Number.")

# =====================================================
# Example 05 - if elif else Statement
# =====================================================

# Python checks the conditions from top to bottom.
# As soon as one condition becomes True,
# the remaining conditions are skipped.

marks = 86

if marks >= 90:
    print("Grade: A+")

elif marks >= 80:
    print("Grade: A")

elif marks >= 70:
    print("Grade: B")

elif marks >= 60:
    print("Grade: C")

elif marks >= 50:
    print("Grade: D")

else:
    print("Grade: F")

# =====================================================
# Example 06 - Student Scholarship Eligibility
# =====================================================

cgpa = 3.65

if cgpa >= 3.80:
    print("100% Scholarship")

elif cgpa >= 3.50:
    print("75% Scholarship")

elif cgpa >= 3.00:
    print("50% Scholarship")

else:
    print("No Scholarship")

# =====================================================
# Example 07 - Nested if Statement
# =====================================================

# A nested if means an if statement inside another if statement.

age = 22
license_available = True

if age >= 18:

    print("Age requirement is satisfied.")

    if license_available == True:
        print("You can drive the car.")
    else:
        print("You cannot drive because you do not have a license.")

else:
    print("You are under 18 years old.")

# =====================================================
# Example 08 - Nested if Example
# =====================================================

username = "admin"
password = "12345"

if username == "admin":

    if password == "12345":
        print("Login Successful.")
    else:
        print("Incorrect Password.")

else:
    print("Invalid Username.")

# =====================================================
# Example 09 - Practical Example
# =====================================================

student_name = "Ali"
marks = 78
attendance = 82

# A student passes only if:
# 1. Marks are at least 50.
# 2. Attendance is at least 75%.

if marks >= 50:

    if attendance >= 75:
        print(student_name, "has Passed.")
    else:
        print(student_name, "has Failed due to Short Attendance.")

else:
    print(student_name, "has Failed due to Low Marks.")