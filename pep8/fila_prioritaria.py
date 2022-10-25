from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO

from typing import Dict, Union, List


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, digija-se ao caixa: {caixa}')

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        estatisticas: Dict[str, Union[List[str], str, int]] = {}
        if flag != 'detail':
            estatisticas = {f'{agencia}-{dia}': len(self.clientes_atendidos)}
        else:
            estatisticas['dia'] = dia
            estatisticas['agencia'] = agencia
            estatisticas['clientes_atendidos'] = self.clientes_atendidos
            estatisticas['quantidade_clientes_atendidos'] = len(
                self.clientes_atendidos)
        return estatisticas
