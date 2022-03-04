class Bankaccount:
    def __init__(self):
        self.accno=210029
        self.name="Bharath"
        self.acctype="Savings"
        self.balance=0
    def deposit(self):
        amount=int(input("Enter the amount to deposit:\t"))
        self.balance+=amount
        print("Amount Succesfully deposited")
    def withdraw(self):
        amount=int(input("Enter the amount to withdraw:\t"))
        if self.balance>=amount:
            self.balance-=amount
            print("Succesfully Withdrawn")
        else:
            print("Insufficient Balance")
    def display(self):
        print("Account number=",self.accno,"\nName=",self.name,"\nAccount type=",self.acctype,"\nAvailable balance=",self.balance)
ob=Bankaccount()
ob.deposit()
ob.withdraw()
ob.display()
