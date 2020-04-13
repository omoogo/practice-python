# Title: Character Input

# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# Add on to the previous program by asking the user for another number and 
# printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. 
# (Hint: the string "\n is the same as pressing the ENTER button)

import datetime

name = input('Please enter your name: ')
age = int(input('Please enter your age: '))

year_at_age_100 = datetime.datetime.today().year + (100 - age)
message = f'Hi {name}. You will turn 100 in the year {year_at_age_100}'

print(message)

number_of_times_to_print = int(input('Wait, can I have another number please? '))

for i in range(0, number_of_times_to_print):
    print(message)