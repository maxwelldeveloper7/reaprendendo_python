class LeitorDeArquivo:
    def __init__(self, arquivo) -> None:
        self.arquivo = arquivo
        print(f'Abrindo arquivo: {self.arquivo}')

    def Ler_proxima_linha(self):
        print('Lendo linha...')
        return 'Linha de arquivo'

    def fechar(self):
        print('Fechando arquivo')