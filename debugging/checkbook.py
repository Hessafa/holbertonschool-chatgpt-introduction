class Checkbook:
    """
    A simple checkbook class that tracks balance and allows deposits and withdrawals.
    """

    def __init__(self):
        """Initializes a Checkbook instance with a zero balance."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits the specified amount into the checkbook.

        Parameters:
            amount (float): The amount to deposit.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the checkbook if sufficient funds are available.

        Parameters:
            amount (float): The amount to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Displays the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function that allows the user to deposit, withdraw, view balance, or exit.
    Handles invalid input to avoid crashes.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            break
        elif action in ('deposit', 'withdraw'):
            try:
                amount = float(input(f"Enter the amount to {action}: $"))
                if amount <= 0:
                    print("Please enter a positive amount.")
                    continue
                if action == 'deposit':
                    cb.deposit(amount)
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
