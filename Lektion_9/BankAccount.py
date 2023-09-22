import sys
class Bankaccount():
    def __init__(self, AccountNum, Saldo):
        self.Accountnum = AccountNum
        self.Saldo = Saldo
    
    def Deposit(self):
        deposit = int(input("How much would you like to deposit? > "))
        self.Saldo += deposit
        print ("You now have", self.Saldo, "on your account!")
    
    def Withdraw(self):
        withdraw = int(input("How much would you like to withdraw? > "))
        self.Saldo -= withdraw
        print ("You now have", self.Saldo, "on your account!")

Bankaccount1 = Bankaccount(1993, 100)
Bankaccount1.Deposit()
Bankaccount1.Withdraw()