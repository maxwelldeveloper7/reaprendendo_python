from pprint import pprint

class Cliente:
    def __init__(self, nome: str, cpf: str, profissao: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

# cliente = Cliente('Jhon Doe', '123.456.789-00', 'Desenvolvedor')
# pprint(cliente.nome)
# pprint(cliente.cpf)
# pprint(cliente.profissao)

# pprint(cliente.__dict__, width=40)

class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None
    
    def __init__(self, cliente: Cliente, agencia: str, numero: str) -> None:
        self.saldo = 100
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas        
    
    def transferir(self, valor: float, favorecido: Cliente) -> None:
        favorecido.depositar(valor)

    def sacar(self, valor: float) -> None:
        self.saldo -= valor

    def depositar(self, valor: float) -> None:
        self.saldo += valor


conta_corrente = ContaCorrente(None, '00', '101')