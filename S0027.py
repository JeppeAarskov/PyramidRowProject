"""
Writing to and reading from a file

Inspect this code in detail.
Find out what every line of code does. For example by changing the code a bit.
Thereafter go on with the next file in numerical order in the teacher's exercise repository.
"""

mydata = ["Hi,\n", "this is a text file.\n", "It has 3 lines.\n"]  # this is a list of strings
myfile = "data/input01.txt"  # the name of the file. Note the / (slash) instead of a \ (backslash) in the file path!

# Writing to a file
with open(myfile, "w") as file:  # 'w' stands fro "write"
    file.writelines(mydata)  # writes the whole list of strings at once

# Reading from a file (method 1)
with open(myfile) as file:  # when the program exits the with-block, the file is automatically closed
    lines = file.readlines()  # reads the whole file at once
line_number = 0
for line in lines:
    line_number += 1
    print(f"Line {line_number}: {line.strip()}")  # .strip cleans the line from spaces, carriage returns and similar characters
print()


# Reading from a file (method 2)
line_number = 0
with open(myfile) as file:
    for line in file:
        line_number += 1
        print(f"Line {line_number}: {line.strip()}")
    print()