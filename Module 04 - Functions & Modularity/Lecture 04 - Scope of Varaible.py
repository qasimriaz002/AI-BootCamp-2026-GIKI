# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 04 - Scope of variables
# =====================================================

# Scope of the variables defines where a variable can be called or used in code
# We have two types of scopes Local Scope or Global Scope examples are given below for both

# =====================================================
# Example 1 - Local Scope
# =====================================================
# A local variable is created inside a function.
# It can only be used inside that function.

def display_student():

    s_name = "Ali"      # Local Variable

    print("Student Name:", s_name)

# Calling the function.
display_student()

# The following statement will generate an error because
# s_name only exists inside the function.

# print(s_name)

# =====================================================
# Example 02 - Global Scope
# =====================================================
# A global variable is created outside all functions.
# It can be accessed from anywhere in the program.

s_name = "Ahmed"       # Global Variable

def display_student():

    print("Student Name:", s_name)

display_student()

print("Outside Function:", s_name)

# =====================================================
# Example 03 - How Local Scope Hides by Global Scope
# =====================================================

# Global Variable
s_name = "Ali"

def display_student():

    # Local Variable
    s_name = "Ahmed"

    print("Inside Function:", s_name)

display_student()

print("Outside Function:", s_name)

# =====================================================
# Example 04 - Using global Keyword
# =====================================================

# Global Variable
counter = 0

def increase_counter():

    global counter

    counter = counter + 1

increase_counter()
increase_counter()
increase_counter()

print("Counter =", counter)

# =====================================================
# Example 05 - Local Variable
# =====================================================

counter = 0

def increase_counter():

    counter = 10

    print("Inside Function:", counter)

increase_counter()

print("Outside Function:", counter)

# =====================================================
# Example 07 - Student Count
# =====================================================

# Global variable stores the total number of students.
student_count = 0


# This function adds one student.
def add_student():

    global student_count

    student_count = student_count + 1


# This function displays the total students.
def display_count():

    print("Total Students:", student_count)


add_student()
add_student()
add_student()

display_count()