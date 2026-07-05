# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 03 - Loops
# =====================================================

# Loops are used to execute the same block of code
# multiple times without writing it again and again.
#
# Python provides two types of loops:
# 1. while loop
# 2. for loop

# =====================================================
# Example 01 - while Loop
# =====================================================

# A while loop keeps executing until its condition
# becomes False.

counter = 1

while counter <= 5:

    print("Counter =", counter)

    counter = counter + 1

# =====================================================
# Example 02 - while Loop with Sum
# =====================================================

number = 1
total = 0

while number <= 5:

    total = total + number

    number = number + 1

print("Sum =", total)

# =====================================================
# Example 03 - while Loop with List
# =====================================================

students = ["Ali", "Ahmed", "Sara", "Ayesha"]

index = 0

while index < len(students):

    print(students[index])

    index = index + 1

# =====================================================
# Example 04 - for Loop using range()
# =====================================================

# range(1,6) generates the numbers:
# 1, 2, 3, 4, 5

for number in range(1, 6):

    print(number)

# =====================================================
# Example 05 - for Loop with Step Size
# =====================================================

# Third value represents the increment.

for number in range(0, 11, 2):

    print(number)

# =====================================================
# Example 06 - for Loop with List
# =====================================================

subjects = ["Python", "Database", "AI", "Machine Learning"]

for subject in subjects:

    print(subject)

# =====================================================
# Example 07 - for Loop with Tuple
# =====================================================

marks = (70, 75, 80, 85)

for mark in marks:

    print(mark)

# =====================================================
# Example 08 - for Loop with Dictionary
# =====================================================

student = {
    "Name": "Ali",
    "Age": 20,
    "Department": "CS"
}

# items() returns both key and value.

for key, value in student.items():

    print(key, ":", value)

# =====================================================
# Example 09 - Nested Loop
# =====================================================

# A nested loop means one loop inside another loop.

for row in range(1, 4):

    for column in range(1, 4):

        print("*", end=" ")

    print()

# =====================================================
# Example 10 - Multiplication Table
# =====================================================

table = 5

for number in range(1, 11):

    print(table, "x", number, "=", table * number)

# =====================================================
# Example 11 - Multiplication Tables (Nested Loop)
# =====================================================

for table in range(2, 6):

    print("\nTable of", table)

    for number in range(1, 11):

        print(table, "x", number, "=", table * number)

# =====================================================
# Example 12 - Practical Example
# =====================================================

students = [
    {"Name": "Ali", "Marks": 80},
    {"Name": "Ahmed", "Marks": 65},
    {"Name": "Sara", "Marks": 92}
]

# Loop visits every student dictionary one by one.

for student in students:

    print("----------------------")
    print("Name :", student["Name"])
    print("Marks:", student["Marks"])

    if student["Marks"] >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")