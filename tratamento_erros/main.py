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
    
    def __init__(self, cliente: Cliente, agencia: int, numero: int) -> None:
        self.__saldo = 100
        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__numero = numero
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas
        
    @property
    def agencia(self):
        return self.__agencia
    
    def __set_agencia(self, value):
        if not isinstance(value, int):
            return
        if value <= 0:
            print('O atributo agencia deve ser maior que zero')
            return
        self.__agencia = value

    @property
    def numero(self):
        return self.__numero
    
    def __set_numero(self, value):
        if not isinstance(value, int):
            return
        if value <= 0:
            return
        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            return
        if value <= 0:
            return
        self.__saldo = value
    
    def transferir(self, valor: float, favorecido: Cliente) -> None:
        favorecido.depositar(valor)

    def sacar(self, valor: float) -> None:
        self.saldo -= valor

    def depositar(self, valor: float) -> None:
        self.saldo += valor


conta_corrente = ContaCorrente(None, 'agencia falsa', 22500)
conta_corrente.agencia = 0
print(conta_corrente.saldo)