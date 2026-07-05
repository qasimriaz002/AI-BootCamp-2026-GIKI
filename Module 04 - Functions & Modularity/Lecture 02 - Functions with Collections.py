# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 02 - Functions with Collections
# =====================================================

# 1. Functions with Lists
# Example 1: Passing a list to a function
marks = [75, 80, 92, 68, 90]

def display_marks(student_marks):
    print("Student Marks:")
    for mark in student_marks:
        print(mark)

display_marks(marks)

# Example 2: Returning a list from a function
def create_even_numbers():
    even_numbers = []

    for number in range(2, 21, 2):
        even_numbers.append(number)

    return even_numbers

numbers = create_even_numbers()

print(numbers)

# Example 3: Finding maximum marks
marks = [65, 72, 91, 85, 78]

def highest_marks(data):
    return max(data)

highest = highest_marks(marks)

print("Highest Marks:", highest)

# 2. Functions with Tuples
# Example 1: Passing a tuple
coordinates = (12, 35)

def display_coordinate(point):
    print("X =", point[0])
    print("Y =", point[1])

display_coordinate(coordinates)

# Example 2: Returning a tuple
def student_information():
    name = "Ali"
    age = 20
    cgpa = 3.65

    return (name, age, cgpa)

student = student_information()

print(student)

# Example 3: Tuple Unpacking
def rectangle():
    return (20, 10)

length, width = rectangle()

print("Length =", length)
print("Width =", width)

# 3. Functions with Sets
# Example 1: Passing a set
subjects = {"AI", "Python", "Database", "Python"}

def display_subjects(data):
    for subject in data:
        print(subject)

display_subjects(subjects)

# Example 2: Returning a set
def vowels():
    return {"a", "e", "i", "o", "u"}

letters = vowels()

print(letters)

# Example 3: Removing duplicate values
marks = [70, 80, 70, 90, 80, 95]

def unique_marks(data):
    return set(data)

print(unique_marks(marks))

# 4. Functions with Dictionaries
# Example 1: Passing dictionary
student = {
    "Name": "Ali",
    "Age": 20,
    "CGPA": 3.45
}

def display_student(data):

    print("Name:", data["Name"])
    print("Age:", data["Age"])
    print("CGPA:", data["CGPA"])

display_student(student)

# Example 2: Returning dictionary
def create_student():

    student = {
        "Name": "Ahmed",
        "Semester": 5,
        "Department": "Computer Science"
    }

    return student

record = create_student()

print(record)

# Example 3: Updating dictionary
def update_cgpa(student):

    student["CGPA"] = 3.80

student = {
    "Name":"Ali",
    "CGPA":3.40
}

update_cgpa(student)

print(student)

# Practical Example
# Student Management System
#
# This example combines functions, lists, and dictionaries to perform a meaningful task.

students = []

def add_student(name, age, department, marks):

    student = {
        "Name": name,
        "Age": age,
        "Department": department,
        "Marks": marks
    }

    students.append(student)


def display_students():

    print("\nStudent Records")

    for student in students:

        print("----------------------")
        print("Name:", student["Name"])
        print("Age:", student["Age"])
        print("Department:", student["Department"])
        print("Marks:", student["Marks"])


def calculate_average(student):

    total = sum(student["Marks"])
    average = total / len(student["Marks"])

    return average


add_student("Ali",20,"CS",[70,80,90])
add_student("Ahmed",21,"AI",[85,90,88])
add_student("Sara",19,"SE",[78,82,80])

display_students()

print("\nAverage Marks")

for student in students:

    avg = calculate_average(student)

    print(student["Name"],":",avg)