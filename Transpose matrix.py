      # matrix transpose

rows=int(input('Enter a numbwer'))
colm=int(input('Enter a numbwer'))
matrix=[]
print('Enter the elements of the matrix :')
for i in range(rows):
   rows=[]
   for j in range(colm):
      element=int(input(f,'Enter element at possition at({i+1},{j+1}):')) 
      rows.append(element)
matrix.append(rows)
print('\n Original Matrix:')
print(rows)
trnaspose =[[matrix[j][i] for j in range(rows)] for i in range(colm)]
print('\n Transpose matrix:')
for row in tranaspose:
    print(rows)
     
