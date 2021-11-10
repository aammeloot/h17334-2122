# Demo of the in operator
myString = input("Input a sentence")
searchTerm = input("Input a word you search for")

if searchTerm in myString:
    print(searchTerm, "is in", myString)
else:
    print("Not found")
