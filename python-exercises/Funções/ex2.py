def executar(n, lista):
    for i in range(n):
         lista += str(i + 1) + "\t"
         print(lista)
lista = ''
n = int(input("Digite n: "))
executar(n, lista)
