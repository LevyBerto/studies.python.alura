import adivinhacao
import forca

def escolhe_jogo():

    print("*******************************")
    print("***** Escolha o seu jogo ***** ")
    print("*******************************")

    print("(1) Forca\n(2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("foca")
        forca.jogar()
    else:
        print("adiv")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()