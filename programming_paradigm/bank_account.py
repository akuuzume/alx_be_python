class BankAccount():
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
    

    def deposit(self, amount):
        if amount>0:
              self.account_balance +=amount
        else:
              print("Insufficient balance to deposit")
        

    def withdraw(self, amount):
        if amount>0 and self.account_balance >=amount:
            self.account_balance -=amount
            return True
        else:
            return False
            
    def displace_balance(self):
         print(f"The balance is {self.account_balance}.3f")
