#Faça um programa que permita ao usuário digitar o seu nome e em 
#seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. 

nome = input("Nome do usuário: ").upper()

print(nome[::-1]) #utilizado o principio de slicing