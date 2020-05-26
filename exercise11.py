"""
Title: Check Primality Functions

Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. Take this 
opportunity to practice using functions, described below.

"""

def is_prime_number(inputNumber):
    rangeOfNumbers = range(1, inputNumber + 1)

    for number in rangeOfNumbers:
        if inputNumber % number == 0 and number != 1 and number != inputNumber:
            return False

    return True

number = int(input('Give me a number: '))

if is_prime_number(number):
    print("It's a prime number!")
else:
    print("It's NOT a prime number!")