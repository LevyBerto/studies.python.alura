import random

def jogar():

    print("***********************************")
    print("Olá bem vindo ao jogo de Adinhação!")
    print("***********************************")

    pontos = 1000
    numero_secreto = random.randrange(1, 101)
    total_tentatativas = 0

    print("Qual o nível de dificuldade?")
    print("(1) Fácil\n(2) Médio\n(3) Difícil")

    nivel = int(input("Defina o nível: "))

    # print(numero_secreto)

    if (nivel == 1):
        total_tentatativas = 20
    elif (nivel == 2):
        total_tentatativas = 10
    else:
        total_tentatativas = 5


    for rodada in range(1,total_tentatativas + 1):
        print("Tentativa: {} de {}".format(rodada, total_tentatativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou: ", chute, end="\n\n")

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número de 1 a 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você Acertou! e fez {} pontos!".format(pontos), end="\n\n")
            break
        else:
            if (maior):
                print("Você Errou! O seu chute foi maior!", end="\n\n")
            elif menor:
                print("Você Errou! O seu chute foi menor!", end="\n\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print("***********************************")
    print("******* Fim do Jogo! **************")
    print("***********************************")

if (__name__ == "__main__"):
    jogar()