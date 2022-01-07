#GCD of two numbers


num1=int(input("Enter Number 1:"))
num2=int(input("Enter Number 2:"))

if(num1>num2):
	small=num2
else:
	small=num1

for i in range(1,small+1):
	if(num1%i==0 and num2%i==0):
		gcd=i
#Here the gcd value is overwriting through every iteration

print("GCD is:", gcd)
