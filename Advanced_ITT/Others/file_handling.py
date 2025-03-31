# FILE HANDLING DEMO IN PYTHON
# Demonstrates: "r" – Read, "w" – Write, "a" – Append, "x" – Create

# 1. "w" – Write mode: Creates a file or overwrites if it already exists
with open("demo_file.txt", "w") as f:
    f.write("Hello from write mode!\n")
    f.write("This file is created using 'w' mode.\n")
print("File written using 'w' mode.\n")

# 2. "a" – Append mode: Adds data to the end of the file without overwriting
with open("demo_file.txt", "a") as f:
    f.write("This line is added using 'a' (append) mode.\n")
print("Content appended using 'a' mode.\n")

# 3. "r" – Read mode: Reads data from the file
try:
    with open("demo_file.txt", "r") as f:
        print("Reading file using 'r' mode:")
        print(f.read())
except FileNotFoundError:
    print("File not found. Make sure it exists before reading.\n")

# 4. "x" – Create mode: Creates a new file, throws error if it exists
try:
    with open("new_file_created.txt", "x") as f:
        f.write("This file was created using 'x' mode.\n")
    print("New file created using 'x' mode.\n")
except FileExistsError:
    print("File already exists. 'x' mode will not overwrite it.\n")
