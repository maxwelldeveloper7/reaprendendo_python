class FilaNormal:
    codigo:int = 0
    fila = []
    clientes_atendidos = []
    senha_atual:str = ""
    
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'NM{self.codigo}'