#Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo 
#texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

import random

arquivo = open("String/palavras.txt", "r").readlines()

palavraEscolhida = arquivo[random.randint(0, 5)]
letrasEscolhidas = []
vidas = 6

print("A palavra escolhida tem: " + str(len(palavraEscolhida)-1) + " letras")

while vidas != 0:
    letraTentativa = input("Digite uma letra como tentativa: ")
    
    if letraTentativa in letrasEscolhidas:
       print("Essa letra já foi escolhida")
    
    else:

      letrasEscolhidas.append(letraTentativa)

      if letraTentativa in palavraEscolhida:
        print("Você acertou a letra: " + letraTentativa)
        ## imprimir a letra na posição
        #fazer um método a parte ?

      else:
        vidas -1
        print("A letra digitada não faz parte da palavra!")
        print(f"Você tem {vidas} vidas")


print(palavraEscolhida)