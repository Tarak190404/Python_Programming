n=int(input("enter your number: "))
n1=0
n2=1
n3=n2
count=1
print("Fibonaci serise is:")
while count<=n:
    print(n3,end=" ")
    count+=1
    n1,n2=n2,n3
    n3=n1+n2
   
