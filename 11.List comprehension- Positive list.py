lst=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
        values=int(input())
        lst.append(values)
print("List is: ",lst)

new_lst=[i for i in lst if i>=0]
print("Positive Number list: ", new_lst)


# lst=[12,13,-54,-56,67,-3,-98,667,3,-563.45]
#doubt:  values=int(input("Enter Number ",i,":"))   is not working
#error: 3 arguments instead of 1 passed to values

