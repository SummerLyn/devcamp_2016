from bank_account_problem import Account
from bank_account_problem import Checking
from bank_account_problem import Savings




def main():
    test = Account("Summer", "Bryant", 3000)
    #print("Hello {0} {1}, your initial deposit is {2}".format())
    def take_withdraw(self):
        checking_or_savings = input("Checking or Savings? 'C or S'").lower()
        amount = int(input("How much do you wish to withdraw?"))

        if checking_or_savings == "c":
            self.checking.withdraw(money)
        elif checking_or_savings == "s":
            self.savings.withdraw(money)
        else:
            print("Please choose 'C' or 'S': ")

    def make_deposit(self):
        checking_or_savings = input("Checking or Savings? 'C or S': ").lower()
        amount = int(input("How much do you wish to deposit?: "))

        if checking_or_savings == "c":
            self.checking.deposit(money)
        elif checking_or_savings == "s":
            self.savings.deposit(money)
        else:
            print("Please choose 'C' or 'S': ")

    def transfer_within_account(self):
        money = int(input("How much do you wish to transfer?: "))
        checking_or_savings = input("Which account do you want to transfer to? 'C'hecking or 'S'avings? ")
        if checking_or_savings == 'c':
            self.transfer_within_account("savings", "checking", money)
        elif checking_or_savings == 's':
            self.transfer_within_account("checking","savings", money)
        else:
            print("Please choose 'C' or 'S': ")

    while True:
        user_answer = input("Enter 'w' for withdraw, 'd' for deposit, 't' for transfer, or 'q' to quit and view transaction history.>>> ").lower()

        if user_answer == 'd':
            deposit = int(input("How much do you want to deposit? "))
            test.deposit(deposit)
            print('Account balance is now: ' + str(test.balance))

        elif user_answer == 'w':
            withdraw = int(input("How much do you want to withdraw? "))

            if withdraw > test.initial_deposit:
                print("Not enough money to withdraw {0}.  Your current balance is {1}".format(withdraw, test.balance))

            else:
                test.withdraw(withdraw)
                print('Account balance is now: ' + str(test.balance))

        elif user_answer == 't':
            transfer_within_account(test)

        else:
            print('Your transaction history is {}:', test.print_trans_history()) #returning NONE
            break


main()
