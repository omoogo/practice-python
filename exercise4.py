# Title: Divisors

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a
# divisor of 26 because 26 / 13 has no remainder.)

inputNumber = int(input('Please enter a number: '))

rangeOfNumbers = range(1, inputNumber + 1)

divisors = []

for number in rangeOfNumbers:
    if inputNumber % number == 0:
        divisors.append(number)

print(divisors)