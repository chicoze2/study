import 'dart:io';
//09) Desenvolver um programa que efetue o cálculo da média aritmética de 4 notas de entrada.

void main() {
  int n1;
  int n2;
  int n3;
  int n4;

  double media;

  print("Digite a nota 1");
  n1 = int.parse(stdin.readLineSync()!);

  print("Digite a nota 2");
  n2 = int.parse(stdin.readLineSync()!);

  print("Digite a nota 3");
  n3 = int.parse(stdin.readLineSync()!);

  print("Digite a nota 4");
  n4 = int.parse(stdin.readLineSync()!);

  media = (n1 + n2 + n3 + n4) / 4;
  print("A media aritimética é: ${media}");
}
