class MoneyNotEnoughError(Exception):
    """The money to be sent must be less than or equal to the initial balance"""
    pass


class PINCodeError(Exception):
    """The given PIN code must match the initial one"""
    pass


class UnderageTransactionError(Exception):
    """To perform online transactions, you must be 18 or older"""
    pass


class MoneyIsNegativeError(Exception):
    """The given money is a negative number"""
    pass


LEGAL_AGE = 18


class TransactionValidator:

    @staticmethod
    def validate_money(amount):
        if amount < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

    @staticmethod
    def validate_balance(amount, balance):
        if amount > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

    @staticmethod
    def validate_pin_code(entered_pin, correct_pin):
        if entered_pin != correct_pin:
            raise PINCodeError("Invalid PIN code")

    @staticmethod
    def validate_age(age):
        if age < LEGAL_AGE:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")


class BankAccount:

    def __init__(self, pin, balance, age):
        self.pin = pin
        self.balance = balance
        self.age = age

    def send_money(self, amount, entered_pin):
        TransactionValidator.validate_money(amount)
        TransactionValidator.validate_balance(amount, self.balance)
        TransactionValidator.validate_pin_code(entered_pin, self.pin)
        TransactionValidator.validate_age(self.age)

        self.balance -= amount
        print(f"Successfully sent {amount:.2f} money to a friend")
        print(f"There is {self.balance:.2f} money left in the bank account")

    def receive_money(self, amount):
        TransactionValidator.validate_money(amount)

        added_money = amount / 2
        self.balance += added_money
        print(f"{added_money:.2f} money went straight into the bank account")


class OnlineBankingApp:

    def __init__(self):
        pin, balance, age = map(int, input().split(", "))
        self.account = BankAccount(pin, balance, age)

    def run(self):
        while True:
            command, *args = input().split("#")

            if command == "End":
                break

            if command == "Send Money":
                amount = int(args[0])
                entered_pin = int(args[1])
                self.account.send_money(amount, entered_pin)

            elif command == "Receive Money":
                amount = int(args[0])
                self.account.receive_money(amount)


app = OnlineBankingApp()
app.run()
