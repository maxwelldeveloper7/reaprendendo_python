arquivo_contatos = open('dados/contatos-escrita.csv', mode='a', encoding='latin_1')

"""Video 01 - escrevendo uma linha no arquivo
"""
contato = '11,maxwell,maxwell@maxwell.com.br\n'
arquivo_contatos.write(contato)
