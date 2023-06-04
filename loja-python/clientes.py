import json

def add(nome, cpf, tel):

    with open('data.json', 'r') as data_file:
        data =json.load(data_file)

    cliente = {"nome": nome, "cpf": cpf, "tel": tel} 

    data[0] = cliente

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

    print("------- NOVO CLIENTE -------")
    print("Nome: " + nome )
    print("CPF: " + cpf )
    print("TEL: " + tel )
    print('-----------------------------')


def vender(prodcutName, cpf):
    with open('data.json', 'r') as data_file:
        data =json.load(data_file)    
    
    for i in data['produtos']:
        if i == prodcutName:
            for i in data['clientes']:
                if i == cpf:
                    ## Achou o produto e o cliente
                    print("------- VENDA REALIZADA ------")
                    print(f"Você vendeu {prodcutName} para {data['clientes'][i]}")
                else:
                    print("Não foi encontrado um cliente com esse CPF")

        else:
            print("Não foi encontrado um produto com esse nome")