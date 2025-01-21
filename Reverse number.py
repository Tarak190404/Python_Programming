n=int(input('Enter your number:'))
print('Reverse number is:')

while n>0:
  r=n%10
  print(r,end="")
  n=n//10
