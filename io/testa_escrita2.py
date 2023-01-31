arquivo_contatos = open('dados/contatos-escrita.csv', mode='w', encoding='latin_1')

"""Video 02 - método close e flush
"""
contatos = [
    '11,Maxwell,maxwell@maxwell.com.br\n',
    '12,Ana,ana@ana.com.br\n',
    '13,Tais,tais@tais.com.br\n',
    '14,Felipe,felipe@felipe.com.br\n'
]

for contato in contatos:
    arquivo_contatos.write(contato)

arquivo_contatos.flush()

input('Pressione <Enter> para encerrar o programa')