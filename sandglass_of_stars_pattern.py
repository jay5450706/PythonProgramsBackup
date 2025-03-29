rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    for space in range(1, rows - i + 1):
        print(end=' ')

    for star in range(1, i + 1):
        print('*', end=' ')
    print('')

for j in range(1, rows + 1):
    for space in range(1, rows - j + 1):
        print(end=' ')
    
    for star in range(1, j + 1):
        print('*', end=' ')
    print('')

# Enter the number of rows: 5
# * * * * * 
#  * * * *  
#   * * *   
#    * *    
#     *     
#     *     
#    * *
#   * * *
#  * * * *
# * * * * *