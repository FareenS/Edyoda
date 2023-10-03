class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount.")

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.balance * self.interestRate) / 100


demo1 = SavingsAccount("Ashish", 2000, 5)
demo1.deposit(500)
print("Balance after deposit:", demo1.getBalance()) 
demo1.withdrawal(500)
print("Balance after withdrawal:", demo1.getBalance()) 
interest = demo1.interestAmount()
print("Interest Amount:", interest) 