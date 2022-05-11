# In Brasil, all valid CPF have the format ###.###.###-## and all valid CNPJ the format 
# But it also has a matematic formula behind it to validate if a number is or is not valid
from validate_docbr import CPF,CNPJ
class Person:
    def __init__(self, document, doc_type):
        self.document = document
        self.doc_type = doc_type.lower()
        self.validate_cpf() if self.doc_type == 'cpf' else self.validate_cnpj()

    def __str__(self):
        return self.format_cpf() if self.doc_type == 'cpf' else self.format_cnpj()

    def format_cpf(self):
        mask = CPF()
        return mask.mask(self.document)

    def format_cnpj(self):
        mask = CNPJ()
        return mask.mask(self.document)

    def validate_cpf(self):
        validator = CPF()
        if not validator.validate(self.document):
            raise ValueError('Invalid CPF!') 

    def validate_cnpj(self):
        validator = CNPJ()
        if not validator.validate(self.document):
            raise ValueError('Invalid CNPJ!') 