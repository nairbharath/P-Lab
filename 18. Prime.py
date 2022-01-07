def Prime(n):
    if n>1:
        for i in range (2,int(n/2)+1):
            if(n%i==0):
                print(n," is not a Prime")
                print(i,"*", n//i," is ",n)
                break
        else:
            print(n," is Prime")
    else:
         print(n," is not Prime")

n=int(input("ENTER A NUMBER: "))
Prime(n)
