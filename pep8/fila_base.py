import abc


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ""

    def reseta_vila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1


@abc.abstractmethod
def gera_senha_atual(self):
    ...


@abc.abstractmethod
def atualiza_fila(self):
    ...


@abc.abstractmethod
def chama_cliente(self, caixa: int):
    ...
