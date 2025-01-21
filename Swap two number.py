a=int(input('Enter first no: '))
b=int(input('Enter second no: '))
print('Before swap a=', a,' and b= ',b)

a=a+b
b=a-b
a=a-b
print('After swap a= ', a, 'and b= ',b)