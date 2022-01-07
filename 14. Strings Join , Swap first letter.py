


str1=input("Enter first word:")
str2=input("Enter second word:")

x=str1[0:1]+str2[1:]
y=str2[0:1]+str1[1:]

z=" ".join([x,y])
print(z)


'''
OR

z=x+" "+y
print(z)
'''
'''
OR
print("%s %s"%(x,y))
'''
'''
OR
print("{} {}".format(x,y))
'''

