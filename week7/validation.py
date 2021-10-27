
# Revision: while loops and validation
# Example below

'''
ans = 'y'
while ans == 'y':
    ans = input('Do you want to continue? (y/n)')

print('Ended.')
'''

# Write a simple program: Ask the user for their age
# Determine if the user's entitled to a driving licence
# UK legal age 17y/o

# Version 1 Without validation

'''
age = int(input("How old are you?"))

if age >= 17:
    print("You are entitled to a driving licence")
else:
    print("You are not entitled to a driving licence")
'''

# Version 2 with boundary validation
# Input the age, but before proceeding
# Use a while loop to ask again in case
# It's not with boundaries

# The loop acts as a 'gatekeeper' to the rest of 
# of the program

'''
age = int(input("How old are you?"))
while age < 0 or age > 100:
    print("Your age is out of the boundaries (0-100)")
    age = int(input("How old are you?"))

if age >= 17:
    print("You are entitled to a driving licence")
else:
    print("You are not entitled to a driving licence")
'''

# Version 3 - With exception handling
# That's the "grown up" way
# This is NOT the way I will recommend in the assessment 

'''
age = -1
while age < 0 or age > 100:
    try:
        age = int(input("How old are you?"))
    except ValueError:
        print("Please make sure you enter an integer")

if age >= 17:
    print("You are entitled to a driving licence")
else:
    print("You are not entitled to a driving licence")
'''

# Version 4 - Check if the input is digits only

# Step 1 - Check if digit only
# Step 2 - Convert to integer
# Step 3 - Check if within boundaries

# Create a validity flag:
ageValid = False
# While loop repeating while the age is not valid
while ageValid == False:
    age = input('How old are you?')    # Just a string
    if not age.isdigit():   # Reject if not a number
        print("Invalid: doesn't contain a number")
    else:         # Else, continue
        age = int(age)
        if age < 0 or age >100:
            print("Age is not within boundaries (0-100)")
        else:
            ageValid = True  # this is basically ending the loop 


if age >= 17:
    print("You are entitled to a driving licence")
else:
    print("You are not entitled to a driving licence")