a= float(input("Enter the first number: "))
b= float(input("Enter the second number: "))
q=a//b
if q>0:
    q+=1
m=a-b*q
print("The modulus of", q)