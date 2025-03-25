rows = int(input('Enter the number of rows: '))

#if the number of rows is not greater than or equal to 2 and less than or equal to 20
if not (rows >= 2 and rows <= 20):
    print('Number of rows should be between 2 and 20 Inclusive')
else:
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(i*j, end=' ')
        print('')