def factorial(n):
    fact=1
    if n==0:
        print(n,"!=",fact)
    for i in range(1,n+1):
        fact=i*fact
    print(n,"!=",fact)
    
n=int(input("Enter the value of n:"))
factorial(n)




#Recursion
def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))


n=int(input("Enter a Number: "))
ans=fact(n)
print(ans)

