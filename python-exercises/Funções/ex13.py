altura = int(input("Digite a altura do retangulo: "))
largura = int(input("Digite a largura do retangulo: "))
while altura < 1 or altura > 20 or largura < 1 or largura > 20:
    print("\n" * 3, "[Digite numeros entre 1 e 20]")
    altura = int(input("Digite a altura do retangulo: "))
    largura = int(input("Digite a largura do retangulo: "))
def teto_chao(largura):
    print("+", "  -  " * (largura - 2), "+")
def paredes(altura, largura):
    for i in range(altura - 2):
        print("|", "     " * (largura - 2), "|")
def desenhar(altura, largura):
    teto_chao(largura)
    paredes(altura, largura)
    teto_chao(largura)
desenhar(altura, largura)