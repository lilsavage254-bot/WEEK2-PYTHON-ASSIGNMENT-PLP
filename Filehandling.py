<<<<<<< HEAD
import os

filename = "conditionalstatements.py"
if os.path.exists(filename):   # This checks if the file exists
    os.remove(filename)        # This deletes the file
    print(f"{filename} has been deleted")
else:
    print("The file does not exist")

# The code below is an example of the "r" mode which allows you to read a file.
file_objects = open("OPEN PYTHON MODES.txt", "r")
file_contents = file_objects.read()
print(file_contents)
file_objects.close()

# The code below is an example of the "a" mode which allows you to append to a file.
file_objects = open("OPEN PYTHON MODES.txt", "a")
files = file_objects.writelines(["\nYUSRA", "\nMARURA", "\nNASSORO"])
print(files)
file_objects.close()

# The code below is an example of the "w" mode which allows you to write to a file.
# Writelines() allows you to add several lines in the file.
file_objects = open("OPEN PYTHON MODES.txt", "w")
write = file_objects.writelines(["\nPLAYING", "\nREADING", "\nWRITING"])
file_objects.close()
print(write)

# The code below is an example of the "r+" mode which allows you to use the read and write modes in the ame file.
file = open("OPEN PYTHON MODES.txt", "r+")
content = file.read()
file.write("\nI LOVE CODING")
file.close()
print(content)

=======
import os

filename = "conditionalstatements.py"
if os.path.exists(filename):   # This checks if the file exists
    os.remove(filename)        # This deletes the file
    print(f"{filename} has been deleted")
else:
    print("The file does not exist")

# The code below is an example of the "r" mode which allows you to read a file.
file_objects = open("OPEN PYTHON MODES.txt", "r")
file_contents = file_objects.read()
print(file_contents)
file_objects.close()

# The code below is an example of the "a" mode which allows you to append to a file.
file_objects = open("OPEN PYTHON MODES.txt", "a")
files = file_objects.writelines(["\nYUSRA", "\nMARURA", "\nNASSORO"])
print(files)
file_objects.close()

# The code below is an example of the "w" mode which allows you to write to a file.
# Writelines() allows you to add several lines in the file.
file_objects = open("OPEN PYTHON MODES.txt", "w")
write = file_objects.writelines(["\nPLAYING", "\nREADING", "\nWRITING"])
file_objects.close()
print(write)

# The code below is an example of the "r+" mode which allows you to use the read and write modes in the ame file.
file = open("OPEN PYTHON MODES.txt", "r+")
content = file.read()
file.write("\nI LOVE CODING")
file.close()
print(content)

>>>>>>> e0323a1ddc73c8762807ff50153f36c1a8248443
