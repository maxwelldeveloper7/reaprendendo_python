class FilaPrioritaria:
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ""
    
    def gera_senha_atual(self)-> None:
        self.senha_atual = f'PR{self.codigo}'
        
    def reseta_vila(self)-> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1
    
    def atualiza_fila(self)-> None:
        self.reseta_vila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)
        
    def chama_cliente(self, caixa:int)-> str:
        cliente_atual:str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f'Cliente atual: {cliente_atual}, digija-se ao caixa: {caixa}')
    
    def estatistica(self, dia: str, agencia: int, flag: str)-> dict:
        if flag!='detail':
            estatisticas = {f'{agencia}-{dia}': len(self.clientes_atendidos)}
        else:
            estatisticas = {}
            estatisticas['dia'] = dia
            estatisticas['agencia'] = agencia
            estatisticas['clientes_atendidos'] = self.clientes_atendidos
            estatisticas['quantidade_clientes_atendidos'] = len(self.clientes_atendidos)
        
        return estatisticas
    