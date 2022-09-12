from xml.etree.ElementInclude import include


def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "maça".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    '''
        for letra in palavra_secreta:
            letras_acertadas.append("_")
    '''
    enforcou = False
    acertou = False

    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Qual letra?:").strip().upper()

        if(chute in palavra_secreta):            
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    #print("Encontrei a letra {} na posição {}".format(letra, index))
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

        if(acertou):
            print("Você ganhou!")
        else:
            print("Você perdeu!")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()#continuar de estrutura de dados
