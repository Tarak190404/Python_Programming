a=int(input('Enter First Number:'))
b=int(input('Enter second Number:'))
c=int(input('Enter third Number:'))

if a>b and a>c:
    max=a;
elif b>a and b>c:
      max=b;
else:
    max=c;
print('muximum number is',max)