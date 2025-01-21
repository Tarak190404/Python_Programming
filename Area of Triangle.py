#3 input------>a,b,c
# s=(a+b+c)/2 //semi perieter
# area=(s*(s-a)*(s-b)*(s-c))**0.5

a=int(input('Enter 1st side: '))
b=int(input('Enter 2nd side: '))
c=int(input('Enter 3rd side: '))
s=(a+b+c)/2 
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('Enter area of Triangle: ',area)