#Dado uma string com uma frase informada pelo usuário (incluindo espaços em 
#branco), conte:
#a. quantos espaços em branco existem na frase.
#b. quantas vezes aparecem as vogais a, e, i, o, u.

string = input("Digite uma frase: ")

blank = 0
vogais = [0, 0, 0, 0, 0]


for i in string:
    if i == " ":
      blank +=1
    
    elif i == "a":

       vogais[0] = vogais[0]+1

    elif i == "e":

       vogais[1] = vogais[1]+1

    elif i == "i":

       vogais[2] = vogais[2]+1
    
    elif i == "o":

       vogais[3] = vogais[3]+1

    elif i == "u":

       vogais[4] = vogais[4]+1

print(f""" A frase fornecida contém: 
{str(blank)} espaços em branco
{str(vogais[0])} vogal A 
{str(vogais[1])} vogal E 
{str(vogais[2])} vogal I 
{str(vogais[3])} vogal O
{str(vogais[4])} vogal U
""")