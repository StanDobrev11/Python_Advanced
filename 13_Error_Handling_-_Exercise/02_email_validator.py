"""
You will be given some emails until you receive the command "End". Create the following custom exceptions to
validate the emails:
• NameTooShortError - raise it when the name in the email is less than or equal to 4 ("peter" will be the
name in the email "peter@gmail.com")
• MustContainAtSymbolError - raise it when there is no "@" in the email
• InvalidDomainError - raise it when the domain of the email is invalid (valid domains are: .com, .bg,
.net, .org)
When an error is encountered, raise it with an appropriate message:
• NameTooShortError - "Name must be more than 4 characters"
• MustContainAtSymbolError - "Email must contain @"
• InvalidDomainError - "Domain must be one of the following: .com, .bg, .org,
.net"
Hint: use the following syntax to add a message to the Exception: MyException("Exception Message")
If the current email is valid, print "Email is valid" and read the next one

Input               Output
abc@abv.bg
                    Traceback (most recent call last):
                     File ".\email_validator.py", line 20, in <module>
                     raise NameTooShort("Name must be more than 4 characters")
                    __main__.NameTooShort: Name must be more than 4 characters
peter@gmail.com
petergmail.com
                    Email is valid
                    Traceback (most recent call last):
                     File ".\email_validator.py", line 18, in <module>
                     raise MustContainAtSymbolError("Email must contain @")
                    __main__.MustContainAtSymbolError: Email must contain @
peter@gmail.hotmail
                    Traceback (most recent call last):
                     File ".\email_validator.py", line 22, in <module>
                     raise InvalidDomainError("Domain must be one of the folowing:
                    .com, .bg, .org, .net")
                    __main__.InvalidDomainError: Domain must be one of the folowing:
                    .com, .bg, .org, .net
"""
import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


name_regex = r'[A-Za-z]{4,}(?=@)'
symbol_regex = r'@'
domain_regex = r'(?<=[a-z])\.[a-z]{2,3}\b'

data = input()
while True:
    if not re.search(name_regex, data):
        raise NameTooShortError("Name must be more than 4 characters")
    if not re.search(symbol_regex, data):
        raise MustContainAtSymbolError("Email must contain @")
    if not re.search(domain_regex, data):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print('Email is valid')
    data = input()
