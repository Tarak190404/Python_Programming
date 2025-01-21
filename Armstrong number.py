n=int(input('Enter your number:'))
temp=n
sum=0

while n>0:
  r=n%10
  sum=sum+r*r*r
  n=n//10

if temp==sum:
    print('Armstrong number')
else:
    print('Not Armstrong number')
