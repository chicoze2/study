def conversor(hora_24):
    hora_12 = hora_24 - 12
    return hora_12
def saida(hora_12, hora_24, minuto_24):
    if hora_24 >= 12 and hora_24 <= 24:
        print(hora_12,":", minuto_24, "PM")
    else:
        print(hora_24, ":", minuto_24, "AM")

while True:
    hora_24 = int(input("\nDigite a hora: "))
    minuto_24 = int(input("Digite o minuto: "))
    hora_12 = conversor(hora_24)
    saida(hora_12, hora_24, minuto_24)

