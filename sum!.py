n=int(input('enter a number : '))
sum=0

for i in range (n+1):
 fact=1
 for j in range (1,i):
   fact=fact*j
 #term=1 / fact
 sum=sum+fact
print('sum = ',sum)
