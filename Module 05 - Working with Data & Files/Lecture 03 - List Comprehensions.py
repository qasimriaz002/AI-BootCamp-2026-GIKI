# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 03 - List Comprehensions
# =====================================================

# List Comprehension is a short and simple way to create
# a new list from an existing list or any iterable object.
#
# Instead of writing multiple lines using loops,
# we can create a list in a single line.

# General Syntax:
#
# new_list = [expression for variable in iterable]

# =====================================================
# Example 01 - Creating a List using for Loop
# =====================================================

# Creating a list of numbers from 1 to 10 using a for loop.

numbers = []

for number in range(1, 11):

    numbers.append(number)

print(numbers)

# =====================================================
# Example 02 - Creating the Same List using List Comprehension
# =====================================================

numbers = [number for number in range(1, 11)]

print(numbers)

# =====================================================
# Example 03 - Square of Numbers
# =====================================================

# Create a new list containing squares of numbers.

squares = [number ** 2 for number in range(1, 11)]

print(squares)

# =====================================================
# Example 04 - Cube of Numbers
# =====================================================

cubes = [number ** 3 for number in range(1, 11)]

print(cubes)

# =====================================================
# Example 05 - Using List Comprehension with Existing List
# =====================================================

marks = [60, 70, 80, 90]

updated_marks = [mark + 5 for mark in marks]

print(updated_marks)

# =====================================================
# Example 06 - Using if Condition
# =====================================================

# Store only even numbers.

even_numbers = [number for number in range(1, 21) if number % 2 == 0]

print(even_numbers)

# =====================================================
# Example 07 - Using if Condition
# =====================================================

# Store only odd numbers.

odd_numbers = [number for number in range(1, 21) if number % 2 != 0]

print(odd_numbers)

# =====================================================
# Example 08 - List of Student Names
# =====================================================

students = ["Ali", "Ahmed", "Sara", "Ayesha"]

new_students = [student for student in students]

print(new_students)

# =====================================================
# Example 09 - Converting Names into Upper Case
# =====================================================

students = ["Ali", "Ahmed", "Sara", "Ayesha"]

upper_names = [student.upper() for student in students]

print(upper_names)

# =====================================================
# Example 10 - Using if else in List Comprehension
# =====================================================

marks = [82, 45, 91, 38, 75]

results = ["Pass" if mark >= 50 else "Fail" for mark in marks]

print(results)

# =====================================================
# Example 11 - Creating a List from a String
# =====================================================

word = "PYTHON"

letters = [letter for letter in word]

print(letters)

# =====================================================
# Example 12 - Nested List Comprehension
# =====================================================

# Create a multiplication table.

table = [[row * column for column in range(1,6)] for row in range(1,6)]

print(table)

# =====================================================
# Example 13 - Practical Example
# =====================================================

student_names = ["Ali", "Ahmed", "Sara", "Ayesha"]

student_marks = [82, 74, 91, 68]

# Create a list of dictionaries.

students = [

    {

        "Name": student_names[index],

        "Marks": student_marks[index]

    }

    for index in range(len(student_names))

]

print(students)

# =====================================================
# Example 14 - Practical Example
# =====================================================

marks = [82, 45, 91, 38, 75]

# Create a list containing only passed students' marks.

passed_marks = [mark for mark in marks if mark >= 50]

print(passed_marks)

# =====================================================
# Example 15 - Practical Example
# =====================================================

numbers = [1,2,3,4,5,6,7,8,9,10]

# Create a new list containing squares
# of only even numbers.

even_squares = [

    number ** 2

    for number in numbers

    if number % 2 == 0

]

print(even_squares)