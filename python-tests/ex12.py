numero = input("Digite o número de telefone: ")

# Removendo o traço, se existir
numero = numero.replace('-', '')

# Verificando se o número contém apenas 7 dígitos
if len(numero) == 7:
    numero_corrigido = '3' + numero
    print("Número corrigido:", numero_corrigido)
else:
    print("Número válido:", numero)
