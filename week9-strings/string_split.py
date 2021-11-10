# String split - default looks for spaces
sentence = "Today the Sun is shining. We cannot certainly be in Scotland."
words = sentence.split()
print(words)

# Print all the words one by one 
for w in words:
    print(w)

# Print the first letter of every word
for w in words:
    print(w[0])

# Use a different parameter
today = "10/11/2021"
elts = today.split("/")

print("Day:", elts[0])
print("Month:", elts[1])
print("Year:", elts[2])

