from validate_docbr import CPF
from validate_docbr import CNPJ

class CpfCnpj:
    
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_e_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!!")        
    
    def cpf_e_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")
        
    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.formata_cpf()
    
    def cnpj_e_valido(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError("CNPJ inválido!!")
