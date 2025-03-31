# Printing a simple string
print("Hello, Python!")

# Using a variable to store and print a string
message = "Welcome to Python programming!"
print(message)

# Using triple quotes for multiline strings
multiline_text = """May
the force
be with you."""
print(multiline_text)

# Accessing characters in a string using index
text = "Python"
# First character. Python uses 0 indexing i.e. index starts from 0
print("First character:", text[0])
print("Second character:", text[1])  # Second character
print("Last character:", text[-1])  # Last character

# Extracting parts of a string
text = "Hello, World!"
print("First 5 characters:", text[:5])   # First 5 characters
print("Last 5 characters:", text[-5:])   # Last 5 characters
print("Characters from index 2 to 6:", text[2:6])  # Substring

# Converting string to uppercase and lowercase
text = "Python is fun"
print("Uppercase:", text.upper())  # Convert to uppercase
print("Lowercase:", text.lower())  # Convert to lowercase
print("Titlecase:", text.title())  # Convert to titlecase

# Replacing words in a string
print("Replacing 'fun' with 'awesome':", text.replace("fun", "awesome"))

# Joining two strings
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Using escape characters
print("This is a \"quoted\" word.")  # Double quote inside string
print('It\'s a great day!')          # Single quote inside string
print("New line:\nNext line starts here.")  # New line character
print("Tab space:\tTabbed text")  # Tab character
