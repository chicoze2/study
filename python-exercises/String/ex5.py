#Altere o programa anterior de modo que a escada seja invertida.

nome = input("Nome do usuário: ").upper()
tam = len(nome)

for i in nome:
  print(nome[:tam]) #nesse caso a variavel de controle começa com o tamanho da string e vai reduzindo a cada loop
  tam-=1