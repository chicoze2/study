import 'dart:io';
//04) Desenvolver um programa que efetue o cálculo da área do triângulo.

double calcArea(int base, int altura) {
  double area = 0.5 * base * altura;

  return area;
}

void main() {
  int base;
  int altura;

  print('Digite a base');
  base = int.parse(stdin.readLineSync()!);

  print('Digite a altura');
  altura = int.parse(stdin.readLineSync()!);

  print('A area do triangulo é: ${calcArea(base, altura)}');
}
