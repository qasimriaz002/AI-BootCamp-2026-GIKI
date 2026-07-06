# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 02 - Error Handling (Exception Handling)
# =====================================================

# Sometimes errors occur while a program is running.
# Such errors are called Exceptions.
#
# If exceptions are not handled, the program stops immediately.
#
# Python provides the following keywords to handle exceptions:
# 1. try
# 2. except
# 3. finally

# =====================================================
# Example 01 - Program without Exception Handling
# =====================================================

# The following program will terminate because
# division by zero is not allowed.

# number = 10
# answer = number / 0
# print(answer)

# =====================================================
# Example 02 - Using try and except
# =====================================================

# The code that may generate an exception
# is placed inside the try block.

try:

    number = 10

    answer = number / 0

    print(answer)

except:

    print("An Error Occurred.")

print("Program Continues...")

# =====================================================
# Example 03 - Handling Specific Exception
# =====================================================

try:

    number = 25

    answer = number / 0

    print(answer)

except ZeroDivisionError:

    print("Cannot Divide by Zero.")

# =====================================================
# Example 04 - Handling Invalid User Input
# =====================================================

try:

    age = int(input("Enter Your Age: "))

    print("Your Age is:", age)

except ValueError:

    print("Please Enter a Valid Integer.")

# =====================================================
# Example 05 - Multiple except Blocks
# =====================================================

try:

    number = int(input("Enter a Number: "))

    answer = 100 / number

    print(answer)

except ValueError:

    print("Invalid Number Entered.")

except ZeroDivisionError:

    print("Number Cannot be Zero.")

# =====================================================
# Example 06 - Using finally Block
# =====================================================

# The finally block always executes,
# whether an exception occurs or not.

try:

    number = 20

    answer = number / 2

    print(answer)

except:

    print("An Error Occurred.")

finally:

    print("Program Execution Completed.")

# =====================================================
# Example 07 - Reading a File
# =====================================================

try:

    file = open("students.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:

    print("File Does Not Exist.")

finally:

    print("File Handling Completed.")

# =====================================================
# Example 08 - Accessing Invalid List Index
# =====================================================

students = ["Ali", "Ahmed", "Sara"]

try:

    print(students[5])

except IndexError:

    print("Invalid List Index.")

# =====================================================
# Example 09 - Accessing Invalid Dictionary Key
# =====================================================

student = {

    "Name":"Ali",

    "Marks":80

}

try:

    print(student["Age"])

except KeyError:

    print("Key Does Not Exist.")

# =====================================================
# Example 10 - Handling Multiple Exceptions Together
# =====================================================

try:

    number = int(input("Enter a Number: "))

    answer = 100 / number

    print(answer)

except (ValueError, ZeroDivisionError):

    print("Invalid Input.")

# =====================================================
# Example 11 - Practical Example
# =====================================================

students = {

    "Ali":82,

    "Ahmed":45,

    "Sara":91

}

try:

    student_name = input("Enter Student Name: ")

    print("Marks:", students[student_name])

except KeyError:

    print("Student Record Not Found.")

finally:

    print("Search Completed.")

# =====================================================
# Example 12 - Practical Example
# =====================================================

numbers = [20, 40, 60]

try:

    index = int(input("Enter Index Number: "))

    print("Value:", numbers[index])

except ValueError:

    print("Please Enter an Integer.")

except IndexError:

    print("Index is Out of Range.")

finally:

    print("Program Finished Successfully.")