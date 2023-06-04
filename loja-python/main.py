import estoque as est
import clientes as cl

import os
def limpar_console():
    if os.name == 'nt':  # Para sistemas Windows
        os.system('cls')
    else:  # Para sistemas Unix/Linux/Mac
        os.system('clear')


while True:
    opcao = input("""Selecione sua opção desejada: 
    1 - Adicionar produto ao estoque
    2 - Listar estoque
    3 - Cadastrar cliente
    4 - Fazer venda
    ---> """)

    # limpar_console()


    if opcao == '1':
        
        description = input("Digite a descrição do seu  produto: ")
        quantidade = input("Digite a quantidade em  estoque: ")
        preco = input("Digite o preco do seu produto: ")
        est.add(description, quantidade, preco)



    elif opcao == '2':
        itens = est.listar()
    
    elif opcao == '3':
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF: ")
        telefone = input("Digite o telefone de contato: ")   
        cl.add(nome, cpf, telefone)

    elif opcao == '4':
        nome = input("Digite o nome do produto: ")
        cpf = input("Digite o CPF do cliente: ")
        
        cl.vender(nome, cpf)

    else:
        print("Você digitou uma opção invalida")