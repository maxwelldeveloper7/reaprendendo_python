print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = int(input("Digite o seu número: "))

print("Você digitou ", chute)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")#02. comparando variáveis

print("Fim do jogo")