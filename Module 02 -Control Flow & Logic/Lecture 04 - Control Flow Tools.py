# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 04 - Control Flow Tools
# =====================================================

# Sometimes we want to change the normal execution of a loop
# or a conditional statement.
#
# Python provides three important control flow tools:
# 1. break
# 2. continue
# 3. pass

# =====================================================
# Example 01 - break Statement
# =====================================================

# The break statement immediately terminates the loop.

for number in range(1, 11):

    if number == 6:
        break

    print(number)

# =====================================================
# Example 02 - break with while Loop
# =====================================================

counter = 1

while True:

    print(counter)

    if counter == 5:
        break

    counter = counter + 1

# =====================================================
# Example 03 - Practical Example of break
# =====================================================

students = ["Ali", "Ahmed", "Sara", "Ayesha"]

for student in students:

    if student == "Sara":
        print("Student Found.")
        break

    print(student)

# =====================================================
# Example 04 - continue Statement
# =====================================================

# The continue statement skips the remaining statements
# of the current iteration and moves to the next iteration.

for number in range(1, 11):

    if number == 5:
        continue

    print(number)

# =====================================================
# Example 05 - continue with Even Numbers
# =====================================================

for number in range(1, 11):

    if number % 2 == 0:
        continue

    print(number)

# =====================================================
# Example 06 - continue with List
# =====================================================

marks = [85, 42, 76, 38, 90]

for mark in marks:

    if mark < 50:
        continue

    print(mark)

# =====================================================
# Example 07 - pass Statement
# =====================================================

# The pass statement does nothing.
# It is used as a placeholder when we want to write
# code later.

marks = 75

if marks >= 50:

    pass

print("Program Continues...")

# =====================================================
# Example 08 - pass inside Loop
# =====================================================

for number in range(1, 6):

    if number == 3:
        pass

    print(number)

# =====================================================
# Example 09 - pass with Function
# =====================================================

# We can also use pass when creating an empty function.

def display_student():

    pass

print("Function Created Successfully.")

# =====================================================
# Example 10 - Combining break and continue
# =====================================================

for number in range(1, 11):

    if number == 3:
        continue

    if number == 8:
        break

    print(number)

# =====================================================
# Example 11 - Practical Example
# =====================================================

students = [
    {"Name": "Ali", "Marks": 82},
    {"Name": "Ahmed", "Marks": 45},
    {"Name": "Sara", "Marks": 91},
    {"Name": "Ayesha", "Marks": 38}
]

# Skip failed students and display only passed students.

for student in students:

    if student["Marks"] < 50:
        continue

    print(student["Name"], "has Passed.")

# =====================================================
# Example 12 - Practical Example
# =====================================================

numbers = [15, 20, -5, 40, 60]

# Stop processing when a negative number is found.

for number in numbers:

    if number < 0:
        print("Negative Number Found.")
        break

    print(number)