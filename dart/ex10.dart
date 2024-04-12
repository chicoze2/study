import 'dart:io';
//10) Desenvolver um programa que efetue o cálculo da média ponderada de 4 notas de entrada. Sendo as nota1, nota2 e nota3 equivalendo a 30% da nota total e a nota4 equivalendo a 70% de peso.

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

  media = (n1 + n2 + n3 ) *0.3 + (n4 * 0.7);
  print("A media aritimética é: ${media}");
}
