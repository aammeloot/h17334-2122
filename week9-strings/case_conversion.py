# Case conversion real-world example
answer = input("What is the capital of Germany?")
if answer.upper() == "BERLIN":
    print("Well done!")
else:
    print("Try again!")

# By converting case to uppercase and comparing
# with uppercase 'BERLIN', we ensure that
# any case entered by the player will be 
# accepted as a valid answer