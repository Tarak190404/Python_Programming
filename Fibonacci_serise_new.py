n=int(input('Enter a number : '))
a=0
b=1
print('Fibonacci serise is : ' ,a,b,end=" ")
for i in range(2,n):
 c=a+b
 a=b
 b=c
 print(c,end=" ")
