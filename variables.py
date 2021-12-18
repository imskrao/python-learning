# Variables
full_name = 'Santosh Kumar Rao'
age = 24
isDeveloper = True
langOne, langTwo, langThree = 'JavaScript', 'Python', 'Go'

# Taking name as input from user
name = input('What is your full name? ')
# Taking birth year as input from user
birth_year = input(f'Hi {name}! What is birth year? ')
# calculating the age of the user after converting string to number my int function
age = 2021 - int(birth_year)
# Printing the result using F-string formatting
print(f'Hi {name}! You are {str(age)} Years old')

test_string = 'Python is Awesome'
# P
print(test_string[0])

# e
print(test_string[-1])

# Pytho
print(test_string[0:5])

# Python is Awesome
print(test_string[0:])

# Pytho
print(test_string[:5])

# Python is Awesome
print(test_string[:])

# ython is Awesom
print(test_string[1:-1])

# Will clone test_string into test_string_2
test_string_2 = test_string[:]

