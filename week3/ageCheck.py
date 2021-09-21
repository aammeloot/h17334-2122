# Input the name
name = input("What is your name?")
# Input the age
# At first the result of input() is a string
# We use int() to cast the string to an integer
age = input("How old are you?")
age = int(age)

# Similar algorithm to pseudo-code
if age < 18:
    print("You can't order beer")
else:
    print("You can order anything you like")

