# Title: Odd Or Even

# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = int(input('Give me a number yo: '))

if number % 2 == 0:
    print('Your number is even')
else:
    print('Your number is odd')
    
# extras
number = int(input('Let\'s do the extras. Another number please: '))

if number % 4 == 0:
    print('Your number is a multiple of 4')
else:
    print('Your number is not a number of 4')

number = int(input('Last extra. A number please? '))
check = int(input('And a number to divide by: '))

if number % check == 0:
    print('Your check divides evenly into the number')
else:
    print('Your check doesn\'t divide evenly')