def even_odd(number):
    remainder = number % 2
    if remainder == 0:
        print("Number is even")
    else:
        print("Number is odd")

def input_int(message):
    temp_result = input(message)

even_odd(5)
even_odd(78)
even_odd(3)
even_odd(6)

age = input_int("How old are you?")
collection = input_int("How many PS5 games do you own?")

print(age, collection)