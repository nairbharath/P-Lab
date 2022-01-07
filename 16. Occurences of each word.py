txt=input("Enter a text: ").split(' ')
lst=[]
c=1

for i in range(0,len(txt)):
	for j in range(0,len(txt)):
		if(i==j):
			continue
		if(txt[i]==txt[j]):
			c+=1
	if txt[i] not in lst:
		print(txt[i],"occurs ",c," times")
	lst.append(txt[i])
	c=1
