#Armstrong- sum of cube of each digit is equal to the term


num=int(input("Enter a number: "))
order=len(str(num))
sum=0
temp=num
while(temp>0):
	digit=temp%10
	sum+=digit**order
	temp//=10
if(sum==num):
	print(num," is Armstrong")
else:
	print(num,"is not Armstrong")

