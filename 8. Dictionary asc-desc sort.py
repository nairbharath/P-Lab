dictionary={}
n1=int(input("Number of elements in dictionary: "))
for i in range(n1):
    dictionary[i]=input("Enter element : ")
print("Sorting by Keys")
sortedByKey = {k:v for k,v in sorted(dictionary.items())}
print(sortedByKey)
print("Sorting By Values in asending order")
sortedByVal = {k:v for k,v in sorted(dictionary.items(), key = lambda v:v[1])}
print(sortedByVal)
print("Sorting by values in descending order")
sortedByVal = {k:v for k,v in sorted(dictionary.items(), key = lambda v:v[1],reverse =True)}
print(sortedByVal)

print("\nSorting only values, Keys not showing")
print("Ascending")
print(sorted(dictionary.values()))
print("Descending")
print(sorted(dictionary.values(),reverse=True))
