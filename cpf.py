# In Brasil, all valid CPF have the format ###.###.###-## and all valid CNPJ the format 
# But it also has a matematic formula behind it to validate if a number is or is not valid
from validate_docbr import CPF,CNPJ

class Document:
    @staticmethod
    def create_document(document, doc_type):
        doc_type = doc_type.lower()
        if doc_type == 'cpf':
            return Cpf(document)
        elif doc_type == 'cnpj':
            return Cnpj(document)
        else:
            raise ValueError('Not a valid document!')

class Cpf:
    def __init__(self, document):
        self.document = document
        self.validate_cpf()

    def __str__(self):
        return self.format_cpf()

    def format_cpf(self):
        mask = CPF()
        return mask.mask(self.document)

    def validate_cpf(self):
        validator = CPF()
        if not validator.validate(self.document):
            raise ValueError('Invalid CPF!') 

class Cnpj:
    def __init__(self, document):
        self.document = document
        self.validate_cnpj()

    def __str__(self):
        return self.format_cnpj()

    def format_cnpj(self):
        mask = CNPJ()
        return mask.mask(self.document)

    def validate_cnpj(self):
        validator = CNPJ()
        if not validator.validate(self.document):
            raise ValueError('Invalid CNPJ!') 