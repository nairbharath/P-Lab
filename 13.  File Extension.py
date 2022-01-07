
'''
txt=input("Enter a file name: ").split('.')
print(txt[1])

OR
print ("The extension of the file is : " + repr(extn[-1]))
'''

txt=input("Enter a file name: ")
extn=txt.split('.')
print("Extension of file : ",extn[-1])

