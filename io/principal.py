arquivo_contatos = open('dados/contatos.csv',encoding='latin_1')
# dessa forma sobrecarrega a memória
# conteudo = arquivo_contatos.readlines()
# # print(conteudo)

# for linha in conteudo:
#     print(linha, end='')

for linha in arquivo_contatos:
    print(linha, end='')