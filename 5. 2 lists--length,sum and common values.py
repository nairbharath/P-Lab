#5.ENter a list of integers
# i.check whether lists are of same length
# ii.sum of both lists are same
#iii. check for common values



lst1=[]
lst2=[]
s1=0
s2=0
common=[]

n1=int(input("Enter the number of elements of list1: "))

for i in range (0,n1):
	values=int(input())
	lst1.append(values)


n2=int(input("Enter the number of elements of list2: "))

for i in range (0,n2):
	values=int(input())
	lst2.append(values)

print(lst1)
print("String length: ",len(lst1))
print(lst2)
print("String Length: ",len(lst2))

if(len(lst1)==len(lst2)):
	print("Lists are of same length")
else:
	print("Lists dont have same length")



for i in range(0,n1):
	s1+=lst1[i]


for i in range(0,n2):
	s2+=lst2[i]

if(s1==s2):
	print("Sum of List 1=",s1," and List 2=",s2," are equal")
else:
	print("Sum of List 1=",s1," and List 2=",s2," are NOT equal")


for i in range (0,n1):
	for j in range (0,n2):
		if(lst1[i]==lst2[j]):
			common.append(lst1[i])
print("Common elements are: ",common)
