n=int(input("Select degree input: \n1.Celcius \t2.Fahrenheit\n"))

if(n==1):
	degree=float(input("Enter the degree: "))
	celc_to_fahren=round(degree*(9/5)+32,2)
	print(degree," Celcius is ",celc_to_fahren," Fahrenheit")
elif(n==2):
	degree=float(input("Enter the degree: "))
	fahren_to_celc=round((degree-32)/(9/5),2)
	print(degree," Fahrenheit is ",fahren_to_celc," Celcius")
else:
	print("Invalid Choice")

