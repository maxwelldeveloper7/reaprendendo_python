    # def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
    #     estatisticas: Dict[str, Union[List[str], str, int]] = {}
    #     if flag != 'detail':
    #         estatisticas = {f'{agencia}-{dia}': len(self.clientes_atendidos)}
    #     else:
    #         estatisticas['dia'] = dia
    #         estatisticas['agencia'] = agencia
    #         estatisticas['clientes_atendidos'] = self.clientes_atendidos
    #         estatisticas['quantidade_clientes_atendidos'] = len(
    #             self.clientes_atendidos)
    #     return estatisticas