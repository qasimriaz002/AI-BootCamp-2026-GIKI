# =====================================================
# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)
# =====================================================
#
# Lecture 03 - Variables & Data Types
# =====================================================

#
# A variable is a named memory location used to store data.
#
# Think of a variable as a labeled box.
# We can store information inside the box,
# retrieve it later,
# or replace it with another value.
#

# -----------------------------------------------------
# Integer
# -----------------------------------------------------

# Integer stores whole numbers.

student_age = 20

print("Student Age =", student_age)

#
# Observe that no quotation marks are used because
# 20 is a NUMBER, not text.
#

# -----------------------------------------------------
# Float
# -----------------------------------------------------

# Float stores decimal numbers.

student_cgpa = 3.67

print("Student CGPA =", student_cgpa)

# -----------------------------------------------------
# String
# -----------------------------------------------------

# String stores text.

student_name = "Ali"

print("Student Name =", student_name)

#
# Since Ali is text,
# quotation marks are necessary.
#

# -----------------------------------------------------
# Boolean
# -----------------------------------------------------

# Boolean stores only two values.

student_pass = True

print("Student Pass Status =", student_pass)

#
# Boolean values are always
#
# True
# False
#

# -----------------------------------------------------
# Using Multiple Variables Together
# -----------------------------------------------------

print("Name :", student_name)
print("Age :", student_age)
print("CGPA :", student_cgpa)
print("Passed :", student_pass)

#
# Every variable stores its own value independently.
#
# Memory Visualization
#
# student_name  --->  "Ali"
# student_age   --->  20
# student_cgpa  --->  3.67
# student_pass  --->  True
#