class LeitorDeArquivo:
    def __init__(self, arquivo) -> None:
        self.arquivo = arquivo
        raise FileNotFoundError
        print(f'Abrindo arquivo: {self.arquivo}')

    def Ler_proxima_linha(self):
        raise IOError
        print('Lendo linha...')
        return 'Linha de arquivo'

    def fechar(self):
        print('Fechando arquivo')