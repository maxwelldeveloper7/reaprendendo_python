'''formatação para numero flutuante'''

print(40*'*')
print("Formatação para Número Flutuante")
print(40*'*')

print('numero simples {}'.format(1.59))

print('numero flutuante simples {:f}'.format(1.59))

print('numero flutuante controlando casas decimais {:.2f}'.format(1.59))

print('numero flutuante controlando casas decimais e número de digitos {:7.2f}'.format(1.59))

print('numero flutuante controlando casas decimais e número de digitos e preenchendo espaços vazios com zero {:07.2f}'.format(1.59))

print('numero flutuante controlando casas decimais e número de digitos e preenchendo espaços vazios com zero {:08.3f}'.format(1.59))


print(40*'*')
print("Formatação para Número Inteiro")
print(40*'*')

print("{:07d}".format(4))

print(40*'*')
print("Formatação para Data")
print(40*'*')

print("Data {:02d}/{:02d}/{:04d}".format(25,5,1979))