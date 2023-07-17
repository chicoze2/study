#Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu 
#comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou 
#diferentes no conteúdo.

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

print("String 1: " +string1+ "\n Tamanho: " + str(len(string1)))
print("String 2: " +string2+ "\n Tamanho: " + str(len(string2)))

if len(string1) != len(string2):
    print("As duas strings são de tamanhos diferentes.")
else:
    print("As duas strings são de tamanhos iguais.")
    
if string1 == string2:
    print("As duas strings são de igual conteúdo.")
else:
    print("As duas strings são de conteúdo diferente.")
        