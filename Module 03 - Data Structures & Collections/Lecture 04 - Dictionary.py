# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 04 - Dictionaries
# =====================================================

# A dictionary is a collection of data stored in the form
# of Key : Value pairs.
#
# Dictionaries are:
# 1. Mutable (Can be modified)
# 2. Ordered (Python 3.7+)
# 3. Keys must be unique
# 4. Values can be duplicated
# 5. Accessed using Keys instead of Index Numbers

# =====================================================
# Example 01 - Creating a Dictionary
# =====================================================

student = {
    "Name": "Ali",
    "Age": 20,
    "Department": "Computer Science",
    "CGPA": 3.65
}

print(student)

# =====================================================
# Example 02 - Accessing Dictionary Values
# =====================================================

# Dictionary values are accessed using their keys.

print("Name:", student["Name"])
print("Age:", student["Age"])
print("Department:", student["Department"])

# =====================================================
# Example 03 - Modifying Dictionary Values
# =====================================================
#
# student["CGPA"] = 3.90
#
# print(student)

# # =====================================================
# # Example 04 - Adding New Key-Value Pair
# # =====================================================
#
# student["Semester"] = 5
#
# print(student)
#
# # =====================================================
# # Example 05 - Removing Data
# # =====================================================
#
# del student["Age"]
#
# print(student)

# # =====================================================
# # Example 06 - Length of Dictionary
# # =====================================================
#
# print("Total Items:", len(student))
#
# # =====================================================
# # Example 07 - Membership Operator
# # =====================================================
#
# # Membership operators check only the keys.
#
# print("Name" in student)
#
# print("Marks" in student)
#
# # =====================================================
# # Example 08 - Traversing Dictionary Keys
# # =====================================================
#
# for values in student:
#
#     print()

# # =====================================================
# # Example 09 - Traversing Dictionary Values
# # =====================================================
#

# x = [11,12,13]
x = student.values()
print(type(x))
# for value in x:
#
#     print(value)

# # =====================================================
# # Example 10 - Traversing Keys and Values
# # =====================================================
#
# # items() returns both key and value.
#
# for key, value in student.items():
#
#     print(key, ":", value)
#
# # =====================================================
# # Example 11 - Dictionary Built-in Methods
# # =====================================================
#
# print(student.keys())
#
# print(student.values())
#
# print(student.items())
#
# # =====================================================
# # Example 12 - Nested Dictionary
# # =====================================================
#
# students = {
#
#     "Student1": {
#         "Name": "Ali",
#         "Marks": 85
#     },
#
#     "Student2": {
#         "Name": "Ahmed",
#         "Marks": 78
#     }
#
# }
#
# print(students)
#
# print(students["Student1"])
#
# print(students["Student1"]["Name"])
#
# print(students["Student2"]["Marks"])
#
# # =====================================================
# # Example 13 - Dictionary inside List
# # =====================================================
#
# students = [
#
#     {"Name":"Ali","Marks":80},
#
#     {"Name":"Ahmed","Marks":75},
#
#     {"Name":"Sara","Marks":90}
#
# ]
#
# print(students)
#
# print(students[0])
#
# print(students[1]["Name"])
#
# # =====================================================
# # Example 14 - List inside Dictionary
# # =====================================================
#
# student = {
#
#     "Name":"Ali",
#
#     "Marks":[80,75,90]
#
# }
#
# print(student)
#
# print(student["Marks"])
#
# print(student["Marks"][0])
#
# # =====================================================
# # Example 15 - Practical Example
# # =====================================================
#
# students = [
#
#     {
#         "Name":"Ali",
#         "Marks":82,
#         "Department":"CS"
#     },
#
#     {
#         "Name":"Ahmed",
#         "Marks":45,
#         "Department":"AI"
#     },
#
#     {
#         "Name":"Sara",
#         "Marks":91,
#         "Department":"SE"
#     }
#
# ]
#
# # Loop visits every dictionary stored in the list.
#
# for student in students:
#
#     print("----------------------------")
#
#     print("Name:", student["Name"])
#
#     print("Department:", student["Department"])
#
#     print("Marks:", student["Marks"])
#
#     if student["Marks"] >= 50:
#
#         print("Result: Pass")
#
#     else:
#
#         print("Result: Fail")