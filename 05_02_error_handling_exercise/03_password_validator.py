class PasswordTooShortError(Exception):
    """Raised when password length is less than 8 characters."""
    pass


class PasswordTooCommonError(Exception):
    """Raised when password contains only digits, only letters, or only special characters."""
    pass


class PasswordNoSpecialCharactersError(Exception):
    """Raised when password does not contain at least one special character."""
    pass


class PasswordContainsSpacesError(Exception):
    """Raised when password contains empty spaces."""
    pass


SPECIAL_CHARACTER = ("@", "*", "&")


def validate_password(password_check):
    if len(password_check) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if " " in password_check:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    if not any(char in SPECIAL_CHARACTER for char in password_check):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    digit_check = password_check.isdigit()
    letter_check = password_check.isalpha()
    special_character = all(char in SPECIAL_CHARACTER for char in password_check)

    if digit_check or letter_check or special_character:
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")


while True:
    password = input()
    if password == "Done":
        break

    try:
        validate_password(password)
        print("Password is valid")

    except Exception as error:
        raise
