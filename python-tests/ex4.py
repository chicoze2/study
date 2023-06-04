#Modifique o programa anterior de forma a mostrar o nome em formato de 
#escada

nome = input("Nome do usuário: ").upper()
aux = 1

for i in nome:
  print(nome[:aux]) #utilizado o princípio de slicing [:int] e uma varivel de controle 
  aux+=1