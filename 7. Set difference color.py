s1=input("Enter the colors for list 1:")
s1=s1.split(",")
s1=set(s1)

s2=input("Enter the colors for list 2:")
s2=s2.split(",")
s2=set(s2)

s1.difference_update(s2)
print("Colours present in list1 but not in list 2: ",s1)
