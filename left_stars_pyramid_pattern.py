rows = int(input("Enter the number of rows: "))

for i in range(1, rows+1):
    for j in range(1, rows - i + 1):
        print(end='  ')

    for k in range(1, i+1):
        print("*", end=" ")
    print('')
for l in range(1, rows):
    for m in range(1, l + 1):
        print(end='  ')
    
    for n in range(1, rows-m+1):
        print('*', end=' ')
    print('')

#print("Another way")?


# with a single space this is the pattern
#     *     
#    * *    
#   * * *   
#  * * * *  
# * * * * * 
#  * * * *  
#   * * *   
#    * *    
#     *     

# Enter the number of rows: 5
#         * 
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *