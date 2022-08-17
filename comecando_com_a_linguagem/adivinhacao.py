import random

print("\u001b[37m\u001b[44m Bem vindo ao jogo de Adivinhação! \u001b[m")

numero_secreto = int(round((random.randrange(1,101))))
total_de_tentativas = 3
print(numero_secreto)

'''
rodada = 1
while(rodada <= total_de_tentativas):

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute = int(input("Digite o seu número: "))
    print("Você digitou ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!")
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto")

    
    rodada += 1
'''

for rodada in range(0,total_de_tentativas):

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))
    print("Você digitou ", chute)

    if (chute < 1 or chute >100):
        print("Você deve digitar um número de 1 a 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!")
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto")    
    

print("Fim do jogo")#continuar de aula 6 definindo um intervalo