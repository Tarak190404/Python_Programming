  # a+b+c=Result
  # 0+1+2=3
  #1+2+3=6
  #2+3+6=11..... ai vabe kaj kore...

n=int(input('Enter a number : '))
a=0
b=1
c=2
print('Tribonacci serise is : ',a,b,c,end=" ")
for i in range(3,n):
 d=a+b+c
 a=b
 b=c
 c=d
 print(c,end=" ")
