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
        self.checking = Checking(initial_deposit)
        self.savings = Savings(0)

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        self.transaction_history.append("Deposited " + str(deposit_amount))


    def withdraw(self, withdraw_amount):
        self.balance -= withdraw_amount
        self.transaction_history.append("Withdrew " + str(withdraw_amount))

    def print_trans_history(self):
        for i in self.checking.transaction_history:
            print(i)
        for i in self.savings.transaction_history:
            print(i)




class Checking:

    def __init__(self, money):
        self.balance = money
        self.initial_deposit = money
        self.transaction_history = []

    def deposit(self, money):
        self.balance += money
        self.transaction_history.append("You've deposited ${}".format(str(money)))

    def withdraw(self, money):
        self.balance -= money
        self.transaction_history.append("You've withdrawn ${}".format(str(money)))
        if withdraw > money:
            print("Not enough money in account to withdraw {0}.  Your current balance is {1}".format(money, self.transaction_history))
        else:
            self.balance -= money
        return self.balance

    def print_transaction_history(self):
        for i in self.transaction_history:
            print(i)


class Savings:
    interest_rate = 2.01

    def __init__(self, money):
        self.balance = money
        self.initial_deposit = money
        self.transaction_history = []
        self.interest_rate = Savings.interest_rate

    def deposit(self, money):
        self.balance += money
        self.transaction_history.append("You've deposited ${}".format(str(money)))

    def withdraw(self, money):
        self.balance -= money
        self.transaction_history.append("You've withdrawn ${}".format(str(money)))
        if withdraw > money:
            print("Not enough money in account to withdraw {0}.  Your current balance is {1}".format(money, self.transaction_history))
        else:
            self.balance -= money
        return self.balance

    def print_transaction_history(self):
        for i in self.transaction_history:
            print(i)

    def interest(self):
        self.balance = self.balance * self.interest_rate
        self.transaction_history.append("After interest accrued, your new balance is {}".format(str(self.balance)))
