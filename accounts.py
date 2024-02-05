import datetime
import pytz

class Account:
    """ Simple account class with balance """
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)
        self.transactions_list = []
        
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            #print("Added {} into your account".format(amount))
            self.transactions_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
    
    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
        elif amount > self.balance:
            print("You have no money for withdraw of {}, actually {}".format(amount, self.balance))
                      
    def show_balance(self):
        print("Balance is {} ".format(self.balance))   
    
    def show_transactions(self):
        print("History of transactions: ")
        for date, amount in self.transactions_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdraw"
            print("{:6} {} by {} on {} local time was {})".format(amount, tran_type, self.name, date, date.astimezone()))
            
if __name__ == '__main__' :
    marek = Account("Marek", 12000)
    kasia = Account("Kasia", 0)
    marek.deposit(3000)
    kasia.deposit(100)
    marek.withdraw(1400)
    marek.deposit(200)
    marek.show_balance()
    marek.show_transactions()