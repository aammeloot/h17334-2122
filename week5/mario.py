# Super Mario Bros 2
# Character selection = an array of strings

characters = ['Mario', 'Luigi', 'Toad', 'Princess Peach']

# Will display all the elements keeping the [] etc
print(characters)

# You can use a for-in loop to display the elements one by one
for name in characters:
    print(name)

# Access specific values -> use an index
print(characters[0])
print(characters[2])
# print(characters[11]) # This results in a out of range error

# I can "slice" lists into part-lists
print(characters[:2])
print(characters[1:])
print(characters[1:2])

# How many Characters?
print(len(characters))

# Add a character 
characters.append('Bowser')
print(characters)
 
# Check is something is in the list
if 'Bowser' in characters:
    print('You have a baddie in your list')

if not 'Zelda' in characters:
    print('No sign of Zelda, you are not mixing franchises')

# Find the index of an element
print('The baddie is in position', characters.index('Bowser'))

# Remove Bowser
n = characters.pop(4)
print('You have removed', n,'the list is now', characters)

characters.sort(reverse=True)
print(characters)

