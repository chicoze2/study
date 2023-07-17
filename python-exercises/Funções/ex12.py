import random
def embaralhar_palavra(palavra):
    palavra_embaralhada = ''.join(random.sample(palavra,len(palavra)))
    return palavra_embaralhada
palavra = str(input("Digite uma palavra: "))
print(embaralhar_palavra(palavra))
