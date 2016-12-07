'''
Create a bank account management software for a brand new bank opening up.

Every bank account create should have an
Owner First Name
Last Name
Initial Deposit

There should be methods to deposits and withdraw money from your account.
...

'''

class Account:

    def __init__(self, first, last, initial_deposit):
        self.first = first
        self.last = last
        self.initial_deposit = initial_deposit
        self.transaction_history = []
        self.balance = initial_deposit

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        self.transaction_history.append("Deposited " + str(deposit_amount))


    def withdraw(self, withdraw_amount):
        self.balance -= withdraw_amount
        #print("Not enough money to withdraw {0}.  Your current balance is {1}".format())
        self.transaction_history.append("Withdrew " + str(withdraw_amount))

    def print_trans_history(self):
        for i in self.transaction_history:
            print(i)

'''
an Account class a Checking class and a Savings class
'''
