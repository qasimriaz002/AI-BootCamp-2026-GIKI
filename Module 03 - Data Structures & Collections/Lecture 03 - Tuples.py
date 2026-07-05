# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 03 - Tuples
# =====================================================

# A tuple is a collection of multiple values.
#
# Tuples are:
# 1. Ordered
# 2. Immutable (Cannot be modified after creation)
# 3. Allow Duplicate Values
# 4. Support Indexing and Slicing

# =====================================================
# Example 01 - Creating a Tuple
# =====================================================

students = ("Ali", "Ahmed", "Sara", "Ayesha")

print(students)

# =====================================================
# Example 02 - Accessing Elements using Indexing
# =====================================================

print("First Student :", students[0])
print("Second Student:", students[1])
print("Last Student  :", students[-1])

# =====================================================
# Example 03 - Tuple Slicing
# =====================================================

numbers = (10, 20, 30, 40, 50, 60, 70)

print(numbers[1:5])

print(numbers[:4])

print(numbers[3:])

print(numbers[:])

# =====================================================
# Example 04 - Duplicate Values
# =====================================================

marks = (80, 75, 80, 90, 75)

print(marks)

# =====================================================
# Example 05 - Tuple is Immutable
# =====================================================

# Tuples cannot be modified after creation.
# The following statement will generate an error.

# students[1] = "Bilal"

# =====================================================
# Example 06 - Length of Tuple
# =====================================================

print("Total Students:", len(students))

# =====================================================
# Example 07 - Membership Operators
# =====================================================

print("Ali" in students)

print("Usman" in students)

# =====================================================
# Example 08 - Traversing Tuple using for Loop
# =====================================================

for student in students:

    print(student)

# =====================================================
# Example 09 - Traversing Tuple using while Loop
# =====================================================

index = 0

while index < len(students):

    print(students[index])

    index = index + 1

# =====================================================
# Example 10 - Built-in Functions
# =====================================================

numbers = (15, 40, 25, 60, 35)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Length:", len(numbers))

# =====================================================
# Example 11 - Tuple Concatenation
# =====================================================

tuple1 = (1, 2, 3)

tuple2 = (4, 5, 6)

tuple3 = tuple1 + tuple2

print(tuple3)

# =====================================================
# Example 12 - Tuple Repetition
# =====================================================

numbers = (10, 20)

print(numbers * 3)

# =====================================================
# Example 13 - Converting List into Tuple
# =====================================================

student_list = ["Ali", "Ahmed", "Sara"]

student_tuple = tuple(student_list)

print(student_tuple)

# =====================================================
# Example 14 - Converting Tuple into List
# =====================================================

student_list = list(student_tuple)

print(student_list)

# =====================================================
# Example 15 - Nested Tuple
# =====================================================

marks = (
    (80, 75, 90),
    (65, 70, 85),
    (90, 95, 92)
)

print(marks)

print("First Student Marks:", marks[0])

print("First Subject of First Student:", marks[0][0])

print("Third Subject of Second Student:", marks[1][2])

# =====================================================
# Example 16 - Practical Example
# =====================================================

student_names = ("Ali", "Ahmed", "Sara")

student_marks = (82, 74, 91)

for index in range(len(student_names)):

    print("-----------------------")
    print("Name :", student_names[index])
    print("Marks:", student_marks[index])

    if student_marks[index] >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")

