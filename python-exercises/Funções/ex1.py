def executar(n):
    for i in range(n + 1):
        lista = ''
        for j in range(i):
            lista += str(i) + "\t"
        print(lista)
n = int(input("Digite n: "))
executar(n)