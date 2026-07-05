# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 01 - Lists
# =====================================================

# A list is a collection of multiple values.
# A single list can store integers, floating point numbers,
# strings and even mixed data types.
#
# Lists are:
# 1. Ordered
# 2. Mutable (Can be modified)
# 3. Allow Duplicate Values

# =====================================================
# Example 01 - Creating a List
# =====================================================

students = ["Ali", "Ahmed", "Sara", "Ayesha"]

print(students)

# =====================================================
# Example 02 - Accessing Elements using Indexing
# =====================================================

# Index always starts from 0.

print("First Student :", students[0])
print("Second Student:", students[1])
print("Third Student :", students[2])

# Negative indexing starts from the end.

print("Last Student :", students[-1])
print("Second Last Student:", students[-2])

# =====================================================
# Example 03 - Modifying List Elements
# =====================================================

students[1] = "Bilal"

print(students)

# =====================================================
# Example 04 - List Slicing
# =====================================================

# Slicing allows us to access multiple elements
# from the list.

numbers = [10,20,30,40,50,60,70]

print(numbers[1:5])
print(numbers[:4])
print(numbers[3:])
print(numbers[:])
print(numbers[-3:])

# =====================================================
# Example 05 - Length of List
# =====================================================

print("Total Students:", len(students))

# =====================================================
# Example 06 - Adding Elements
# =====================================================

students.append("Hamza")

print(students)

# =====================================================
# Example 07 - Inserting an Element
# =====================================================

students.insert(2, "Usman")

print(students)

# =====================================================
# Example 08 - Removing Elements
# =====================================================

students.remove("Sara")

print(students)

# =====================================================
# Example 09 - Removing Last Element
# =====================================================

students.pop()

print(students)

# =====================================================
# Example 10 - List with for Loop
# =====================================================

# The loop visits every element of the list one by one.

for student in students:

    print(student)

# =====================================================
# Example 11 - List with Index using range()
# =====================================================

for index in range(len(students)):

    print(index, students[index])

# =====================================================
# Example 12 - List with while Loop
# =====================================================

index = 0

while index < len(students):

    print(students[index])

    index = index + 1

# =====================================================
# Example 13 - Built-in Functions
# =====================================================

marks = [78, 90, 65, 82, 95]

print("Maximum Marks:", max(marks))
print("Minimum Marks:", min(marks))
print("Total Marks:", sum(marks))
print("Total Subjects:", len(marks))

# =====================================================
# Example 14 - Sorting a List
# =====================================================

marks.sort()

print("Ascending Order")
print(marks)

marks.reverse()

print("Descending Order")
print(marks)

# =====================================================
# Example 15 - Membership Operators
# =====================================================

print("Ali" in students)

print("Zain" in students)

# =====================================================
# Example 16 - Concatenating Lists
# =====================================================

list1 = [1,2,3]

list2 = [4,5,6]

list3 = list1 + list2

print(list3)

# =====================================================
# Example 17 - Repeating a List
# =====================================================

numbers = [1,2,3]

print(numbers * 3)

# =====================================================
# Example 18 - Mixed Data Types
# =====================================================

student = ["Ali",20,3.65,True]

print(student)

# =====================================================
# Example 19 - Nested List
# =====================================================

marks = [
    [80,75,90],
    [65,70,85],
    [90,95,92]
]

print(marks)

print("First Student Marks :", marks[0])

print("First Subject of First Student :", marks[0][0])

print("Second Subject of Third Student :", marks[2][1])

# =====================================================
# Example 20 - Practical Example
# =====================================================

student_names = ["Ali","Ahmed","Sara","Ayesha"]

student_marks = [82,74,91,68]

# Loop is used to display the name and marks
# of every student.

for index in range(len(student_names)):

    print("------------------------")
    print("Name :", student_names[index])
    print("Marks:", student_marks[index])

    if student_marks[index] >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")