     #EMI Calculate
     #amount ----> principle(p)
     #period ----> time(t)
     #rate -----> interest(i)
     # I=p*r*t/100 ---->Simple interest

amount=float(input('Enter the base amount : '))
period=float(input('Enter the time period in years : '))
rate=float(input('Enter rate of interest : '))

interest=amount*period*rate/100
total=amount+interest
emi=total/(period*12)

print('Total amount is : ',total,'Rs') #ai line  korteo parish abar na o parish

print('EMI amount is : ',emi,'Rs')
