# -----------------------
# Function Basic
# -----------------------

# Define a basic function named 'greet' that takes no arguments
def greet():
    # This function simply prints a welcome message
    print("Hello, welcome to Python functions!")


# Call the 'greet' function
greet()

# -----------------------
# Function with Operators
# -----------------------

# Define a function that accepts two arguments and returns their sum


def add_numbers(a, b):
    return a + b  # Return the result of adding a and b


# Call the 'add_numbers' function with 10 and 5 as arguments
result = add_numbers(10, 5)

# Print the result returned from the function
print("Sum:", result)

# -------------------------------
# Functions with Default Parameters
# -------------------------------

# Define a function with a default parameter
# If 'exponent' is not provided, it defaults to 2


def power(base, exponent=2):
    return base ** exponent  # Return base raised to the power of exponent


# Call 'power' with only the base; exponent uses the default value (2)
print("Square of 4:", power(4))

# Call 'power' with both base and exponent
print("4 to the power of 3:", power(4, 3))

# --------------------------------------------
# Functions with Variable Number of Arguments
# --------------------------------------------

# Define a function that accepts a variable number of arguments
# The asterisk (*) allows passing any number of positional arguments


def sum_all(*numbers):
    return sum(numbers)  # Use built-in sum() function to add all values


# Call the function with 3 arguments
print("Sum of 1, 2, 3:", sum_all(1, 2, 3))

# Call the function with 4 arguments
print("Sum of 5, 10, 15, 20:", sum_all(5, 10, 15, 20))
