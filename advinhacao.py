import os
import time
numero_secreto = 42
total_de_tentativas = 3
rodadas = 1

while(rodadas <= total_de_tentativas):
    print("********************************")
    print("Bem vindo ao Jogo de advinhação!")
    print("********************************")
    print("Rodada {} de {}".format(rodadas,total_de_tentativas))
    chute = int(input("Digite o seu número: "))
    print("Você digitou ", chute)

    acertou = (chute == numero_secreto)
    maior = (chute > numero_secreto)
    menor = (chute < numero_secreto)

    if not acertou:
        if(maior):
            print("Você errou!")
            print("O chute foi maior que o número secreto!")
        elif(menor):
            print("Você errou!")
            print("O chute foi menor que o número secreto!")
    else:
        print("Você acertou!")
        break
    rodadas +=1
    time.sleep(2)
    os.system('cls')

print("Fim do jogo!")