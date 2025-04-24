
"""Find the minimum of three values."""

number1 = int(input('Enter first integer: '))
number2 = int(input('Enter second integer: '))
number3 = int(input('Enter third integer: '))

#assuming that the first number is the minimum initially.
minimum = number1

#if we have more numbers then more if statements

if number2 < minimum:
	minimum = number2
if number3 < minimum:
	minimum = number3

print('Minimum value is', minimum)
