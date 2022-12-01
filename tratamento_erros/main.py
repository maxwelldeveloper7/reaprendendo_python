from pprint import pprint

class Cliente:
    def __init__(self, nome: str, cpf: str, profissao: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

cliente = Cliente('Jhon Doe', '123.456.789-00', 'Desenvolvedor')
pprint(cliente.nome)
pprint(cliente.cpf)
pprint(cliente.profissao)

pprint(cliente.__dict__, width=40)