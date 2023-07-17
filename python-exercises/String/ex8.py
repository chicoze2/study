#Faça um programa que leia uma seqüência de caracteres, mostre−a e 
#diga se é um palíndromo ou não.

frase = input("Digite sua frase palíndroma: ").upper()

fraseSemEspaco = frase.replace(" ", "")
fraseReversa = fraseSemEspaco[::-1]

if fraseSemEspaco == fraseReversa:
  print(f"A Frase {frase} é palíndroma")

else:
  print(f"A Frase {frase} não é palíndroma")
