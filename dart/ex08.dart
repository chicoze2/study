import "dart:io";
//08) Desenvolver um programa que solicite um valor numérico e informe 25%, 50%, 100% e 150% do valor de entrada.

void main() {
  int num;

  print("Digite um numero");
  num = int.parse(stdin.readLineSync()!);

    print("""O numero escolhido foi (100%)$num
25% de $num é ${num * 0.25}
50% de $num é ${num * 0.50}
150% de $num é ${num * 1.5}""");
}
