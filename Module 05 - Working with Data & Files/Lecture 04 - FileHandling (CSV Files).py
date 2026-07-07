# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 04 - CSV File Handling (Using simple file handling and string manipulation functions)
# =====================================================


# A CSV (Comma Separated Values) file stores data
# where each value is separated by a comma.
# We will be Adding, Searching, Deleting, Editing of data in CSV File.
#
# Example:
#
# Name,Marks
# Ali,80
# Ahmed,75
# Sara,90
#
# A CSV file is actually a normal text file.

# =====================================================
# Example 01 - Creating a CSV File
# =====================================================

with open("students.csv", "w") as file:
    file.write("Name,Marks\n")

    file.write("Ali,80\n")

    file.write("Ahmed,75\n")

    file.write("Sara,90\n")

print("CSV File Created Successfully.")

# =====================================================
# Example 02 - Reading Complete CSV File
# =====================================================

with open("students.csv", "r") as file:
    data = file.read()

    print(data)

# =====================================================
# Example 03 - Reading CSV Line by Line
# =====================================================

with open("students.csv", "r") as file:
    for line in file:
        print(line.strip())
        # strip() removes unwanted spaces and the
        # newline (\n) character from both ends.

# =====================================================
# Example 04 - Reading Individual Values
# =====================================================

with open("students.csv", "r") as file:
    next(file)  # Skip Header
    # next() moves the file pointer to the next line.
    # Here it skips the header line.

    for line in file:
        data = line.strip().split(",")
        # strip() removes the newline character.

        # split(",") breaks a string into a list
        # wherever a comma is found.

        print("Name :", data[0])

        print("Marks:", data[1])

        print("-------------------")

# =====================================================
# Example 05 - Adding a New Student
# =====================================================

with open("students.csv", "a") as file:
    file.write("Bilal,88\n")

print("Student Added Successfully.")

# =====================================================
# Example 06 - Searching Student Record
# =====================================================

search_name = "Sara"

found = False

with open("students.csv", "r") as file:
    next(file)

    for line in file:

        data = line.strip().split(",")

        if data[0] == search_name:
            print("Student Found")

            print("Name :", data[0])

            print("Marks:", data[1])

            found = True

if not found:                   # we can write in both ways 1. if found == false or 2. if not founds
    print("Student Not Found")

# =====================================================
# Example 07 - Updating Student Marks
# =====================================================

updated_records = []

with open("students.csv", "r") as file:
    for line in file:

        data = line.strip().split(",")

        if data[0] == "Ahmed":
            data[1] = "95"

        updated_records.append(",".join(data))
        # join() combines all list elements into
        # one string separated by commas.

with open("students.csv", "w") as file:
    for record in updated_records:
        file.write(record + "\n")

print("Marks Updated Successfully.")

# =====================================================
# Example 08 - Deleting Student Record
# =====================================================

updated_records = []

with open("students.csv", "r") as file:
    header = file.readline()
    # readline() reads only one line from the file.

    updated_records.append(header.strip())

    for line in file:

        data = line.strip().split(",")

        if data[0] != "Ali":
            updated_records.append(",".join(data))

with open("students.csv", "w") as file:
    for record in updated_records:
        file.write(record + "\n")

print("Student Deleted Successfully.")

# =====================================================
# Example 09 - Display Updated File
# =====================================================

with open("students.csv", "r") as file:
    print(file.read())

# =====================================================
# Example 10 - Practical Example
# =====================================================

# Find all students who passed.

with open("students.csv", "r") as file:
    next(file)

    for line in file:

        data = line.strip().split(",")

        marks = int(data[1])
        # int() converts a string into an integer.

        if marks >= 50:

            print(data[0], "Passed")

        else:

            print(data[0], "Failed")

# =====================================================
# Example 11 - Practical Example
# =====================================================

# Calculate Total and Average Marks.

total = 0

count = 0

with open("students.csv", "r") as file:
    next(file)

    for line in file:
        data = line.strip().split(",")

        total = total + int(data[1])
        # Convert marks from string to integer.

        count = count + 1

print("Total Marks :", total)

print("Average Marks :", total / count)

# =====================================================
# Example 12 - Practical Example
# =====================================================

# Display Student having the Highest Marks.

highest_name = ""

highest_marks = 0

with open("students.csv", "r") as file:
    next(file)

    for line in file:

        data = line.strip().split(",")

        marks = int(data[1])

        if marks > highest_marks:
            highest_marks = marks

            highest_name = data[0]

print("Top Student :", highest_name)

print("Highest Marks:", highest_marks)

# =====================================================
# Example 13 - Practical Example
# =====================================================
# Complete Student Result Management.
student_name = input("Enter Student Name: ")

new_marks = input("Enter New Marks: ")

updated_records = []

found = False

with open("students.csv", "r") as file:
    for line in file:

        data = line.strip().split(",")

        if data[0] == student_name:
            data[1] = new_marks

            found = True

        updated_records.append(",".join(data))

with open("students.csv", "w") as file:
    for record in updated_records:
        file.write(record + "\n")

if found:

    print("Student Record Updated.")

else:

    print("Student Not Found.")

# =====================================================
# Useful String Functions Used in This Lecture
# =====================================================

# strip()      -> Removes spaces and newline (\n)
# split(",")   -> Converts a string into a list
# join()       -> Combines list elements into one string
# read()       -> Reads the complete file
# readline()   -> Reads one line from the file
# write()      -> Writes one string into a file
# writelines() -> Writes multiple strings into a file
# next(file)   -> Skips the current line of the file
# int()        -> Converts a string into an integers
