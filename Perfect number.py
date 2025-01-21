n=int(input('Enter a number : '))
s=0
for i in range(1,n):
 if(n%i==0):
    s=s+i
if(s==n):
    print(n,'is perfect nuber')
else:
      print(n,'is not perfect number')
