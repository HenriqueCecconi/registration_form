# In Brasil, all valid CPF have the format ###.###.###-##
# But it also has a matematic formula behind it to validate if a number is or is not valid
from validate_docbr import CPF
class Cpf:
    def __init__(self, cpf):
        self.cpf = cpf
        self.validate_cpf()

    def __str__(self):
        return self.format_cpf()

    def format_cpf(self):
        mask = CPF()
        return mask.mask(self.cpf)

    def validate_cpf(self):
        validator = CPF()
        if not validator.validate(self.cpf):
            raise ValueError('Invalid CPF!') 