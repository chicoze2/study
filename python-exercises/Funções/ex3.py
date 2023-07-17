def soma(arg1, arg2, arg3):
    print("\nSoma: ", arg1 + arg2 + arg3)
args = []
for i in range(3):
    print("\nArgumento n°", i + 1)
    arg = args.append(float(input("Digite o argumento: ")))
soma(args[0], args[1], args[2])