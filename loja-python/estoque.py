import json

def add(description, qtd, value):

    with open('data.json', 'r') as data_file:
        data =json.load(data_file)

    arrayProdutos = data['produtos']

    newProduct = {"nome": description, "qtd": qtd, "value": value} 

    arrayProdutos.append(newProduct)

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

    print("------- NOVO PRODUTO -------")
    print("Nome: " + description )
    print("Quantidade de itens: " + qtd )
    print("Preço: " + value )
    print('-----------------------------')


def listar():
    with open('data.json', 'r') as data_file:
        data =json.load(data_file)

    contador = 0
    print("--------------------------")

    for i in data['produtos']:
        contador += 1

        nome = i['nome']
        qtd = i['qtd']
        preco = i['value']

        print(f"------- PRODUTO {str(contador)} -------")  
        print("Nome: " + nome )
        print("Quantidade de itens: " + qtd )
        print("Preço: " + preco )