# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 03 - Working with Multiple Functions
# =====================================================

# Here we will see how we call one function inside the other function
# For this purpose I created two different functions as following

# EXAMPLE 1
# Here we created a function to calculate total marks.
def calculate_total(marks):

    x = sum(marks)

    return x


# This function calls calculate_total().
def display_result(student_name, marks):

    total = calculate_total(marks)

    print("Student:", student_name)
    print("Marks:", marks)
    print("Total Marks:", total)


stdmarks = [80, 75, 90]

display_result("Ahmed", stdmarks)

# =====================================================
# Example - Creating List of Dictionaries
# =====================================================

# This function receives two lists.
# The first list contains the names of students.
# The second list contains the marks of students.
#
# The function combines both lists and creates
# a new list in which every element is a dictionary.


#EXAMPLE 2
def create_student_list(s_nameList, s_marksList):

    # Empty list to store dictionaries of students.
    s_studentList = []

    # Loop is used to visit every index of the lists.
    for i in range(len(s_nameList)):

        # Creating dictionary for one student.
        s_student = {
            "Name": s_nameList[i],
            "Marks": s_marksList[i]
        }

        # Adding dictionary into the list.
        s_studentList.append(s_student)

    # Returning the complete list.
    return s_studentList


# Creating two separate lists.
s_nameList = ["Ali", "Ahmed", "Sara", "Ayesha"]
s_marksList = [85, 72, 91, 78]

# Calling the function.
students = create_student_list(s_nameList, s_marksList)

# Displaying the complete list.
print(students)

#EXAMPLE 3
# This function call itself again and again
# If same function calls itself again and again then it is called as recursion
# This function calculates the factorial of a number.
# Factorial means:
#
# 5! = 5 × 4 × 3 × 2 × 1 = 120

def factorial(number):#1st 5 ==

    # Base Case
    # Factorial of 0 and 1 is always 1.
    if number == 0 or number == 1:
        return 1

    # Recursive Case
    return number * factorial(number - 1)
            #5    *  factorical(4) ---> return 5 * 24 = 120
            #4    *  factional (3) ---> return 4 * 6 = 24
            #3    *  factional (2) ---> return 3 * 2 = 6
            #2    *  factional (1) ---> return 2 * 1 = 2


answer = factorial(5)

print("Factorial =", answer)


# Example 4
# Display List Using Recursion
marks = [70, 80, 90, 85, 75]

# This function displays every element of the list
# without using a loop.
def display_marks(data, index):

    # Base Case
    if index == len(data):
        return

    print(data[index])

    # Recursive Call
    display_marks(data, index + 1)

display_marks(marks, 0)