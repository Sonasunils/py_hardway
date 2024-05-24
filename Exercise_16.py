from sys import argv  # Import the argv module from the sys package

# Unpack the arguments passed to the script, where `script` is the name of the script and `filename` is the file to be edited
script, filename = argv

# Print a message indicating that the file will be erased
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Wait for user input to either cancel or continue
input("?")

# Open the file in write mode, which truncates the file to zero length (erasing its contents)
print("Opening the file...")
target = open(filename, 'w')

# Explicitly truncate the file, though this is redundant since opening in 'w' mode already truncates the file
print("Truncating the file. Goodbye!")
target.truncate()

# Prompt the user to input three lines of text
print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Print a message indicating the lines will be written to the file
print("I'm going to write these to the file.")

# Write the input lines to the file, each followed by a newline character
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Close the file
print("And finally, we close it.")
target.close()
