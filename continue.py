n = 0

while n <= 10:
    n += 1
    if not n % 2 == 0:
        continue
    print(n, end=' ')