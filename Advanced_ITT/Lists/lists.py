# Introduction to Lists in Python

# Creating a list
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

# Modifying a list
my_list.append(60)  # Adding an element
my_list.insert(2, 25)  # Inserting 25 at index 2
my_list[1] = 15  # Changing the second element
print("Modified List:", my_list)

# Finding the length of the list
list_length = len(my_list)
print("Length of List:", list_length)

# Sorting the list
my_list.sort()
print("Sorted List:", my_list)

# Reversing the list
my_list.reverse()
print("Reversed List:", my_list)
