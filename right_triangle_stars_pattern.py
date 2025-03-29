rows = int(input("Enter the number of rows: "))

i = 1
columns = rows
while i <= rows:
    j = 1
    #spaces = 1 
    while j <= columns: #5
        if j > columns - i: #4
            print("*", end=' ')
        else:
            print(end='  ') #print(end='# ') for testing
        #spaces += 1
        j += 1
    i += 1
    print('')

# Enter the number of rows: 5
#         * 
#       * *
#     * * *
#   * * * *
# * * * * *