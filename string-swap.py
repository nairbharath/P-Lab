str1=input("Enter String1: ")
str2=input("Enter String2: ")
print("Before swap:",(str1,str2))
a=str2[0:2]+str1[2:]
b=str1[0:2]+str2[2:]
print("After swapping first two chars:",(a,b))
