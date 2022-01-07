#WAP to read a list of int values for all values>100,replace with word "over"

lst=[]
x=[]
n=int(input("Enter the number of int values: "))


for i in range(0,n):
	values=int(input())
	lst.append(values)

print(lst)

for i in range(0,n):
	if(lst[i]>100):
		lst[i]="over"	
		
	
print(lst)


