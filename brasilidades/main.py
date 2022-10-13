from cpf_cnpj import CpfCnpj

cpf = '04960780622'
cnpj = '28975623000107'

objeto_cpf = CpfCnpj(cpf,'cpf')
objeto_cnpj = CpfCnpj(cnpj,'cnpj')

print(objeto_cpf)
print(objeto_cnpj)
