#oop 
class Customer:
    def __init__(self,name,email,pin):
        self.name = name 
        self.email = email
        self.__pin = pin 

    def verify_pin(self,pin):
        return pin == self.__pin
        
class BankAccount: 
    def __init__(self,customer):
        self.customer = customer
        self.__balance= 0 
        pass

    def deposit(self,amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance = {self.__balance}")

    def withdraw(self,amount):
        
        if amount >  self.__balance:
            return f"Insufficient funds"
        else: 
            self.__balance -= amount
            return f"Amount withdrawn: {amount}\n New Balance: {self.__balance}" 
        
    def get_balance(self):
        return self.__balance
    
class SavingsAccount(BankAccount):
    def apply_interest(self):
        interest = self.get_balance() * .03
        self.deposit(interest)
        return f"interest added"
    
class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        fee = 5
        total = amount + fee
        if total > self.get_balance():
            return f'insufficient funds minus fee'
        else: 
            super().withdraw(total)