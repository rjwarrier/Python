# Creating a Tuple
# A tuple is an immutable sequence of values, defined using parentheses
fruits = ("apple", "banana", "cherry")
print("Tuple of fruits:", fruits)

# Iterating Over a Tuple
print("Iterating over the tuple:")
for fruit in fruits:
    print(fruit)

# Tuple Concatenation and Repeating
# Concatenation: Joining two tuples
more_fruits = ("orange", "grape")
combined_tuple = fruits + more_fruits
print("Concatenated Tuple:", combined_tuple)

# Repeating: Multiplying a tuple
repeated_tuple = fruits * 2
print("Repeated Tuple:", repeated_tuple)

# Tuple Coordinates
# Tuples are often used to represent coordinates (x, y) or (x, y, z)
point_2D = (3, 5)  # 2D coordinate
point_3D = (3, 5, 7)  # 3D coordinate
print("2D Point Coordinates:", point_2D)
print("3D Point Coordinates:", point_3D)
