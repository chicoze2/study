import 'dart:io';
//02) Desenvolver um programa que efetue o cálculo da área do quadrado.

void main() {
  int l1;
  int area;

  print("Informe um valor numerico");

  l1 = int.parse(stdin.readLineSync()!);
  area = l1 * 2;

  print("A area do quadrado é: $area");

}
