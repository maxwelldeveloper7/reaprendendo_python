class Data:
    def __init__(self, dia, mes, ano) -> None:
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")