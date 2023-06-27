from enum import Enum


class RegExEnum(Enum):
    CAR_MODEL = (
        r'^.*@[A-Z][a-zA-Z/d]{1,24}$',
        'Should be started with a capital letter, min length 2 symb and max length - 25 symb'
    )

    USER_EMAIL = (
        r'^.+@.*gmail.com$',
        'The only --@gmail.com-- domain is valid'
    )
    PASSWORD = (
        r'^(?=.*[A-Z])(?=.*[a-z])((?=.*[[:punct:]]){2,})(?=.*\d)[a-zA-Z\d[:punct:]]{8,20}$',
        'At least 1 uppercase + 1 lowercase + 2 spesial + 1 digit symbols and length up to 20 symbols are supposed when setting password'
    )
    NAME = (
        r"^[А-ЯЁЄЇҐ][а-яёєїґ`]{1,49}$",
        'First letter shoud be capital and length from 2 up to 50 symbols'
    )

    SURNAME = (
        r"^[А-ЯЁЄЇҐ][а-яёєїґ`]{1,49}$",
        'First letter shoud be capital and length from 2 up to 50 symbols'
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.msg = msg
        self.pattern = pattern
