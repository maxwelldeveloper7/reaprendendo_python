from fila_base import FilaBase


class FilaNormal(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'NM{self.codigo}'

    def atualiza_fila(self) -> None:
        self.reseta_vila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, digija-se ao caixa: {caixa}')
