#separate odd and even numbers 
#input should be any number from  1 and not greater than 100 inclusive

print('Press q to quit')

even_numbers = []
odd_numbers = []

while True:
    n = input('Separate Odd and Even Numbers to: ')
    if(n == 'q'):
        break
    if not (n.isnumeric() and int(n) > 0 and int(n) < 100):
        print('Invalid Input')
        continue
    n = int(n)
    li = list(range(1, n+1))
    for number in li:
        if number%2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    if not even_numbers or not odd_numbers:
        print('Empty list')
    else:
        print('Even Numbers')
        print(even_numbers)
        print('Odd Numbers')
        print(odd_numbers)
        print()
        even_numbers.clear()
        odd_numbers.clear()