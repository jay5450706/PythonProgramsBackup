terms = int(input('Enter the number of terms: '))

n1, n2 = 0, 1

if terms <= 0:
    print("Enter a positive integer")
elif terms == 1:
    print(f"Fibonacci sequence: {n1}")
else:
    for term in range(terms):
        print(n1, end=' ')
        n = n1 + n2
        n1 = n2
        n2 = n