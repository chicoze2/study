def somaImposto(taxaImposto, custo):
    imposto_total = custo + (custo * taxaImposto / 100)
    return imposto_total


taxaImposto = input("digite taxa")
custo = input("digite custo")

imposto = somaImposto(taxaImposto, custo)
print(imposto)