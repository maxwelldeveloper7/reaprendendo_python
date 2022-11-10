from sys import path

path.append("/home/maxwell/reaprendendo_python/tdd/")

# print(path)

from codigo.bytebank import Funcionario
lucas = Funcionario('Lucas Carvalho', 2000, 1000)

print(lucas.idade())
