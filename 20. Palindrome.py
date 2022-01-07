'''
#Palindrome- same on reversing(w/o using string)

#Palindrome for number? FTW?

num=int(input("Enter a number:"))
rev=0
temp=num

while(temp>0):
	digit=temp%10
	rev=(rev*10)+digit
	temp//=10
if(rev==num):
	print(num,"is Palindrome")
else:
	print(num,"is not PALINDROME")

'''	
	

#USING INBUILT FUNCTION: slice operation [start:end:step]
#Here, step value of -1 reverses a string.

string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")



rev_string=reversed(string)

if list(string)==list(rev_string):
    print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
 
      
      

'''
# Program to check if a string is palindrome or not

my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")

      
      
'''
