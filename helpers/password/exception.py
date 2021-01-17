from sanic.exceptions import SanicException


class PasswordHashException(SanicException):
    status_code = 500


class GeneratePasswordHashException(PasswordHashException):
    pass


class CheckPasswordHashException(PasswordHashException):
    pass
