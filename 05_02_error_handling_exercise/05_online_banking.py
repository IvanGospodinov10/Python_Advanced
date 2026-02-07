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


def validate_money(amount):
    if amount < 0:
        raise MoneyIsNegativeError("The amount of money cannot be a negative number")


def send_money(user_age, amount, entered_pin, balance, user_pin):
    validate_money(amount)

    if amount > balance:
        raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

    if entered_pin != user_pin:
        raise PINCodeError("Invalid PIN code")

    if user_age < LEGAL_AGE:
        raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

    balance -= amount
    print(f"Successfully sent {amount:.2f} money to a friend")
    print(f"There is {balance:.2f} money left in the bank account")
    return balance


def received_money(amount, balance):
    validate_money(amount)

    added_money = amount / 2
    balance += added_money
    print(f"{added_money:.2f} money went straight into the bank account")
    return balance


def main():
    pin_str, balance_str, age_str = input().split(", ")

    pin = pin_str
    balance = float(balance_str)
    age = int(age_str)

    while True:
        command, *args = input().split("#")

        if command == "End":
            break

        if command == "Send Money":
            amount = float(args[0])
            entered_pin = args[1]
            balance = send_money(age, amount, entered_pin, balance, pin)
        elif command == "Receive Money":
            amount = int(args[0])
            balance = received_money(amount, balance)


main()
