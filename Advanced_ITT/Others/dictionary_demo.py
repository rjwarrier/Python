# A dictionary is a collection of key-value pairs, enclosed in curly braces {}

# Let's create a dictionary to store details of a CA student
student_dict = {
    "name": "Amit",
    "course": "CA",
    "year": 2025,
    "subjects": ["Accounts", "Law", "Taxation"]
}

# Accessing dictionary values using keys
print("Student Name:", student_dict["name"])          # Output: Amit
print("Course:", student_dict["course"])              # Output: CA

# Adding a new key-value pair
student_dict["city"] = "Mumbai"
print("Updated Dictionary:", student_dict)

# Modifying an existing value
student_dict["year"] = 2026
print("Updated Year:", student_dict["year"])

# Accessing list inside dictionary
print("Subjects Enrolled:", student_dict["subjects"])

# Looping through dictionary keys and values
print("\n--- Student Details ---")
for key, value in student_dict.items():
    print(f"{key} ➜ {value}")

# Using get() method to safely access a key (returns None if not found)
print("Phone Number (optional):", student_dict.get("phone"))  # Output: None

# Removing a key-value pair using pop()
student_dict.pop("city")
print("After removing city:", student_dict)

# Checking if a key exists
if "name" in student_dict:
    print("Name key exists in dictionary.")
