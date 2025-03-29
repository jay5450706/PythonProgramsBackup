from math import factorial

rows = int(input("Enter the number of rows: "))

for n in range(rows):
    for space in range(1, rows - n):
        print(end=' ')

    for r in range(n + 1):
        ncr = factorial(n) // (factorial(r) * factorial(n - r))
        print(ncr, end=' ')

    print('')

# Enter the number of rows: 5
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1