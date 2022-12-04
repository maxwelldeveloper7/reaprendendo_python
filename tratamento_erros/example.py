def dividir(dividendo: int, divisor: int) -> float:
    # print(divisor.resultado)
    return dividendo / divisor


def testa_divisao(divisor: int) -> str:
    resultado: float = dividir(10, divisor)
    print(f'O resultado da divisão de 10 por {divisor} é {resultado}')
    


try:
    testa_divisao(0)
# except Exception as E:
#     print(E)
except ZeroDivisionError as E:
    print("Erro de divisão por zero")
except Exception as E:
    print("Tratamento genêrico")
print('Programa encerrado')
