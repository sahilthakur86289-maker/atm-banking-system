class BankAccount:
    def __init__(self, account_holder, pin, balance=0):
        self.account_holder = account_holder
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            self.transaction_history.append("Deposited Rs. " + str(amount))
            print("Amount deposited successfully.")
        else:
            print("Please enter a valid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance = self.balance - amount
            self.transaction_history.append("Withdrawn Rs. " + str(amount))
            print("Amount withdrawn successfully.")

    def check_balance(self):
        print("Current Balance: Rs.", self.balance)

    def show_transaction_history(self):
        if len(self.transaction_history) == 0:
            print("No transactions yet.")
        else:
            print("\nTransaction History")
            for transaction in self.transaction_history:
                print("-", transaction)


class ATM:
    def __init__(self, account):
        self.account = account

    def get_amount(self, message):
        try:
            amount = int(input(message))
            return amount
        except ValueError:
            print("Please enter amount in numbers only.")
            return 0

    def start(self):
        print("Welcome to Simple ATM")
        print("Account Holder:", self.account.account_holder)

        entered_pin = input("Enter your 4 digit PIN: ")

        if self.account.check_pin(entered_pin):
            print("Login successful.")
            self.show_menu()
        else:
            print("Wrong PIN. Please try again.")

    def show_menu(self):
        while True:
            print("\n----- ATM Menu -----")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                amount = self.get_amount("Enter amount to deposit: ")
                self.account.deposit(amount)

            elif choice == "2":
                amount = self.get_amount("Enter amount to withdraw: ")
                self.account.withdraw(amount)

            elif choice == "3":
                self.account.check_balance()

            elif choice == "4":
                self.account.show_transaction_history()

            elif choice == "5":
                print("Thank you for using ATM.")
                break

            else:
                print("Invalid choice. Please select from 1 to 5.")
def create_account():
    print("Create Your Bank Account")
    name = input("Enter account holder name: ")
    pin = input("Set your 4 digit PIN: ")

    try:
        balance = int(input("Enter starting balance: "))
    except ValueError:
        print("Invalid balance. Starting balance set to 0.")
        balance = 0

    print("Account created successfully.\n")
    return BankAccount(name, pin, balance)


account1 = create_account()
atm = ATM(account1)
atm.start()
