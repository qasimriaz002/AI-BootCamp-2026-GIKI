# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 01 - Functions
# =====================================================

# A function is a reusable block of code.
# Instead of writing the same code again and again,
# we write it once inside a function and call it whenever needed.

# Example:
# Suppose a teacher has to greet every student.
# Rather than writing the greeting statement 100 times,
# we can create a function once and call it for every student.


# At this point, Python has only stored the function in memory.
# The statements inside the function will not execute until
# the function is called.

# Creating our first function
def greet():
    print("Assalam-o-Alaikum Students!")
    print("Welcome to Python Programming.")

# At this point, Python has only stored the function in memory.
# The statements inside the function will not execute until
# the function is called.

# Calling the function
greet()

print("----------------------------------")


# Function with one parameter
# The parameter 'name' receives a value when the function is called.
def introduce(name):
    print("Hello", name)
    print("Welcome to GIK Institute.")

introduce("Ali")
introduce("Ahmed")

print("----------------------------------")


# Function with two parameters
def add(num1, num2):
    result = num1 + num2
    print("Sum =", result)
    return result

x = add(10, 20)
print("Printing outside the function")
print(x)
# add(50, 70)

print("----------------------------------")


# Returning a value from a function.
# return sends the result back to the place
# from where the function was called.

def multiply(a, b):
    answer = a * b
    return answer

value = multiply(5, 6)

print("Returned Value =", value)