#Escreva um programa que solicite ao usuário a digitação de um número até 99 e 
#imprima-o na tela por extenso

def obter_nome_unicos(u):
    unicos = { ##dicionario simples
        1: "um",
        2: "dois",
        3: "tres",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove",
        10: "dez",
        11: "onze",
        12: "doze",
        13: "treze",
        14: "quatorze",
        15: "quinze"
    }
    return unicos.get(u)

def obter_nome_dezenas(d):
    dezenas = { ##dicionario simples
        10: "dez",
        20: "vinte",
        30: "trinta",
        40: "quarenta",
        50: "cinquenta",
        60: "sessenta",
        70: "setenta",
        80: "oitenta",
        90: "noventa"
    }
    return dezenas.get(d)



numeroUsuario = int(input("Digite seu numero a ser escrito por extenso (0-99): "))

if numeroUsuario > 99: 
  print('Numero digitado fora do range')    

else:
  dezena = numeroUsuario // 10 #divide por 10 e recebe o valor da divisao em inteiro
  unidade = numeroUsuario % 10 #tira o módulo do numero e retorna as unidades

if numeroUsuario < 16:
   print("O seu número é: " + obter_nome_unicos(numeroUsuario))

elif(unidade == 0):
   print("O seu número é: " + obter_nome_dezenas(numeroUsuario))
   
else:
   if dezena == 1:
      out = "Seu numero é deze" + obter_nome_unicos(unidade)
      print(out)
   else:
      numeroOutput = "Seu número é: " + obter_nome_dezenas(dezena*10) + " e " + obter_nome_unicos(unidade)
      print(numeroOutput)