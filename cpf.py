# In Brasil, all valid CPF have the format xxx.xxx.xxx-xx 
class Cpf:
    def __init__(self, cpf):
        self.cpf = cpf
        self.validate_cpf()

    def __str__(self):
        return self.format_cpf()

    def format_cpf(self):
        return f'{self.cpf[0:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}'

    def validate_cpf(self):
        if len(self.cpf) != 11:
            raise TypeError('Invalid CPF!') 