num = int(input('Enter an integer: '))

if num <= 1:
    print(f'{num} is not a prime number.')
elif num > 1:
    for i in range(2, num):
        if(num % i == 0):
            print(f'{num} is not a prime number.')
            print(f'{i} is a factor of {num}.')
            break
    else:
        print(f'{num} is a prime number.')