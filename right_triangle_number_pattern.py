rows = int(input('Enter the number of rows: '))

#if the number of rows is not greater than 2 and less than 10
if not (rows > 2 and rows < 10):
    print('Number of rows should be between 2 and 10 Exclusive')
else:
    for i in range(1, rows+1):
        for j in range(1, i+1):
            print(i, end=' ')
        print('')

#Another way
print()
print('Using While loop')
if not (rows > 2 and rows < 10):
    print('')
else:
    i = 1
    while i < rows + 1:
        j = 1
        while j < i + 1:
            print(i, end=' ')
            j += 1
        i += 1
        print('')


        
