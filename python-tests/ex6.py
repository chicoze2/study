#faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

dataUser = input("Informe o dia do seu nascimento: dd/mm/aaaa")

dia, mes, ano = map(int, dataUser.split("/")) #separando a data em variáveis menores

def obter_nome_mes(mes):
    meses = { ##dicionario simples
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro"
    }
    return meses.get(mes) ##retorna a string equivalente ao numero do mes

mesExtenso = obter_nome_mes(mes)

dataExtenso = f"{dia} de {mesExtenso} de {ano}" #string literals

print(dataExtenso) 

