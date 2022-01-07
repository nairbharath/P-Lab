s=input("Enter a word: ")
print(s)

s=s[0]+s[1:].replace(s[0],"$")
print(s)


'''
Alternative 1 : Using func

def stringreplace(s):
    fchar=s[0]
    modchar=s.replace(fchar,"$")
    print(fchar+modchar)

str=input("Enter a string: ")
stringreplace(str)


Alternative 2: Using Func w/o extra var

def stringreplace(s):
    s=s[0]+s[1:].replace(s[0],"$")
    print(s)

str=input("Enter a string: ")
stringreplace(str)
'''
