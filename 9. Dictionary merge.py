dict1={}
dict2={}
n= int(input("Enter the number of values in dict1:"))

for i in range(n):
    key1=input("Enter 1st key:")
    value1=input("Enter 1st value:")
    dict1[key1]=value1
print(dict1)


n1=int(input("Enter the number of values in dict 2:"))
for j in range(n1):
    key2=input("Enter 2nd key:")
    value2=input("Enter 2nd value:")
    dict1[key2]=value2
print(dict2)

dict3=dict1.copy()
for key,value in dict2.items():
    dict3.update(dict2)
print(dict3)
