myString = "Computer Science"

# Find out the length of a string
# Function len() built-in across all of Python
result = len(myString) # Processing myString in function len()
print(result)

# Convert a string to uppercase
# Method .upper() specific to strings
result2 = myString.upper() # Processing myString using one of its methods
print(result2)

# Enter a name and return its length
name = input("Enter your name")
print("The number of characters in your name is", len(name))
print("The uppercase version of your name is", name.upper())

# Indexing and negative indexing
print("The first letter of your name", name[0])
print("The last letter of your name is", name[-1])
print("Your name backwards: ", name[::-1])

