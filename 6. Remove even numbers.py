#3.From a list of integers ,create a list, removing even numbers


lst=[]

n=int(input("Enter the number of int values: "))


for i in range(0,n):
	values=int(input())
	lst.append(values)

print(lst)

for i in lst:
	if(i%2==0):
		lst.remove(i)
print("List after removing even numbers:")
print(lst)
		
