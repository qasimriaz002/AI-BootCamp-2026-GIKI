# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 02 - Sets
# =====================================================

# A set is a collection of unique values.
#
# Sets are:
# 1. Unordered
# 2. Mutable (Elements can be added or removed)
# 3. Do NOT allow duplicate values
# 4. Do NOT support indexing or slicing

# =====================================================
# Example 01 - Creating a Set
# =====================================================

students = {"Ali", "Ahmed", "Sara", "Ayesha"}

print(students)

# =====================================================
# Example 02 - Duplicate Values
# =====================================================

# Duplicate values are automatically removed.

numbers = {10, 20, 30, 20, 40, 10, 50}

print(numbers)

# =====================================================
# Example 03 - Adding an Element
# =====================================================

students.add("Hamza")

print(students)

# =====================================================
# Example 04 - Removing an Element
# =====================================================

students.remove("Ahmed")

print(students)

# =====================================================
# Example 05 - Using discard()
# =====================================================

# discard() does not generate an error if the element
# does not exist.

students.discard("Usman")

print(students)

# =====================================================
# Example 06 - Length of a Set
# =====================================================

print("Total Students:", len(students))

# =====================================================
# Example 07 - Membership Operators
# =====================================================

print("Ali" in students)

print("Bilal" in students)

# =====================================================
# Example 08 - Traversing a Set using for Loop
# =====================================================

# Since sets are unordered,
# the elements may appear in different order.

for student in students:

    print(student)

# =====================================================
# Example 09 - Union of Two Sets
# =====================================================

set1 = {10, 20, 30}

set2 = {30, 40, 50}

print(set1 | set2)

# =====================================================
# Example 10 - Intersection of Two Sets
# =====================================================

# Common elements in both sets.

print(set1 & set2)

# =====================================================
# Example 11 - Difference of Two Sets
# =====================================================

print(set1 - set2)

print(set2 - set1)

# =====================================================
# Example 12 - Symmetric Difference
# =====================================================

# Elements that are present in one set
# but not in both.

print(set1 ^ set2)

# =====================================================
# Example 13 - Converting List into Set
# =====================================================

marks = [80, 75, 80, 90, 75, 85]

print("Original List")
print(marks)

unique_marks = set(marks)

print("After Converting into Set")
print(unique_marks)

# =====================================================
# Example 14 - Converting Set into List
# =====================================================

marks_list = list(unique_marks)

print(marks_list)

# =====================================================
# Example 15 - Built-in Functions
# =====================================================

numbers = {25, 40, 15, 60, 35}

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Length:", len(numbers))

# =====================================================
# Example 16 - Practical Example
# =====================================================

# Suppose a teacher accidentally entered
# duplicate roll numbers.

roll_numbers = [101, 102, 103, 102, 105, 101, 106]

print("Original Roll Numbers")
print(roll_numbers)

# Convert list into set to remove duplicates.

unique_roll_numbers = set(roll_numbers)

print("Unique Roll Numbers")
print(unique_roll_numbers)