import 'dart:io';
//07) Desenvolver um programa que solicite um valor numérico e informe o seu dobro e o seu triplo.

void main() {
  int num;

  print("Digite um numero");

  num = int.parse(stdin.readLineSync()!);

  print("""O dobro de $num é ${num * 2}
e o seu triplo é ${num * 3}""");
}
