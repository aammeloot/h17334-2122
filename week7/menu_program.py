# This is an example of a menu program
# The strcture revolves around a main loop
# That repeats until the "quit" option has been chosen

# There is a process of input validation for the user input

# The branching involves a series of if / elif / else 
# Running the appropriate code for the user choice


# Variable containing the user's choice
choice = ''

# start with the loop straight away
# while option is not "quit"
while choice != 4:
    # Display the options
    print('Welcome to the program')
    print('1 - This does one thing')
    print('2 - This does another things')
    print('3 - This does one last thing')
    print('4 - Quit the program')

    # Input the user's choice
    validChoice = False
    # Get the 3-step process
    while validChoice == False:
        choice = input('Please enter your selection (1-4)')
        if not choice.isdigit():
            print('Please ensure you enter an integer')
        else:
            choice = int(choice)
            if choice < 1 or choice > 4:
                print('Selection out of boundaries')
            else:
                validChoice = True
    
    # Dispatch the calls to the right functions
    if choice == 1:
        print('This is choice 1')
        print('You need to write your own code')
    elif choice == 2:
        print('This is choice 2')
        print('You need to write your own code')
    elif choice == 3:
        print('This is choice 3')
        print('You need to write your own code')
    else:    
        print('Bye bye')

    