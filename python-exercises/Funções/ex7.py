def valor_pagamento(valor_prestaocao, dias_atraso):
    if dias_atraso == 0:
        valor = valor_prestaocao
        return valor
    else:
        valor = (valor_prestaocao * 1.03) * ((0.001 * dias_atraso) + 1)
        return valor
valor_prestacao = True
while valor_prestacao != 0:
    valor_prestacao = float(input("\nDigite o valor da prestação: "))
    if valor_prestacao == 0:
        break
    else:
        dias_atraso = int(input("Digite os dias de atraso: "))
        valor = valor_pagamento(valor_prestacao, dias_atraso)
        print("\nO valor do pagamento será de: ", round(valor, 2))