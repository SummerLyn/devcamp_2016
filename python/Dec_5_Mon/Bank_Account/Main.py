from bank_account_problem_code_answer import Account

def main():
    account_1 = Account("John", "Doe", "5000")

    while True:
        user_answer = input('Enter w for withdraw or d for deposit or q to quit and view transaction history. ')

        if user_answer == 'd':
            deposit = int(input("How much do you want to deposit? "))
            account_1.deposit(deposit)
            print('Account balance is now: ' + str(account_1.balance))

        elif user_answer == 'w':
            withdraw = int(input("How much do you want to withdraw? "))
            account_1.withdraw(withdraw)
            print('Account balance is now: ' + str(account_1.balance))
        else:
            print(account_1.print_trans_history())
            break


main()
