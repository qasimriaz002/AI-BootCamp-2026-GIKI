# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 01 - File Handling
# =====================================================

# File Handling allows us to permanently store data
# inside a file. The data remains available even after
# the program is closed.

# Python provides the open() function to work with files.

# Syntax:
# variable = open("filename", "mode")

# Common File Modes:
# "r"  -> Read
# "w"  -> Write (Creates a new file if it does not exist)
# "a"  -> Append
# "r+" -> Read and Write

# =====================================================
# Example 01 - Writing into a File
# =====================================================

# Opening a file in write mode.
# If the file does not exist, Python will create it.

file = open("students.txt", "w")

file.write("Ali\n")
file.write("Ahmed\n")
file.write("Sara\n")

# Always close the file after using it.
file.close()

print("Data Written Successfully.")

# =====================================================
# Example 02 - Reading from a File
# =====================================================

file = open("students.txt", "r")

# Reads complete file.
data = file.read()

print(data)

file.close()

# =====================================================
# Example 03 - Reading File Line by Line
# =====================================================

file = open("students.txt", "r")

for line in file:

    print(line)

file.close()

# =====================================================
# Example 04 - Using readline()
# =====================================================

file = open("students.txt", "r")

print(file.readline())
print(file.readline())

file.close()

# =====================================================
# Example 05 - Appending Data
# =====================================================

# Append mode adds new data without deleting old data.

file = open("students.txt", "a")

file.write("Ayesha\n")

file.close()

print("New Student Added.")

# =====================================================
# Example 06 - Writing Multiple Lines
# =====================================================

students = ["Bilal\n", "Usman\n", "Fatima\n"]

file = open("students.txt", "a")

file.writelines(students)

file.close()

print("Multiple Students Added.")

# =====================================================
# Example 07 - Using with Statement
# =====================================================

# The with statement automatically closes the file.

with open("students.txt", "r") as file:

    data = file.read()

    print(data)

# No need to call file.close()

# =====================================================
# Example 08 - Storing Student Records
# =====================================================

students = [
    "Ali,80\n",
    "Ahmed,75\n",
    "Sara,90\n"
]

with open("marks.txt", "w") as file:

    file.writelines(students)

print("Student Records Saved.")

# =====================================================
# Example 09 - Reading Student Records
# =====================================================

with open("marks.txt", "r") as file:

    for record in file:

        print(record)

# =====================================================
# Example 10 - Practical Example
# =====================================================
#
# Student names and marks are stored in two lists.

student_names = ["Ali", "Ahmed", "Sara", "Jamil"]
student_marks = [80, 75, 92, 44]

# Writing student information into a file.

with open("student_result.csv", "w") as file:

    for i in range(len(student_names)):

        file.write(student_names[i] + "," + str(student_marks[i]) + "\n")

print("Student Result File Created.")

# =====================================================
# Example 11 - Reading Student Result File
# =====================================================

with open("student_result.txt", "r") as file:

    for record in file:

        print(record)

        data = record.strip().split(",")
        # strip() removes unwanted spaces and the
        # newline (\n) character from both ends.

        print("Name :", data[0])
        print("Marks:", data[1])
        print("-------------------")