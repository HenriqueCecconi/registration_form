# Phones in Brasil have the format (##)9####-####, the 9 indicate a cellphone number, and thus don't always appear.
# Also, I might want to make the country code for Brasil as an optional add since +55(##)9####-#### is also a valid number.
import re
class Phones:
    def __init__(self, phone_number):
        self.pattern = '(55)?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        self.phone_number = phone_number
        self.validate_phone()

    def __str__(self):
        return self.format_phone()

    def validate_phone(self):
        if not re.findall(self.pattern, self.phone_number):
            raise ValueError('Invalid number!')

    def format_phone(self):
        match = re.search(self.pattern, self.phone_number)
        if match.group(1):
            formated_number = f'+{match.group(1)}({match.group(2)}){match.group(3)}-{match.group(4)}'
        else:
            formated_number = f'({match.group(2)}){match.group(3)}-{match.group(4)}'
        return formated_number