import 'dart:io';
//03) Desenvolver um programa que efetue o cálculo da área do retângulo.

void main() {
  int l1;
  int l2;
  double area;

  print("Informe o lado");
  l1 = int.parse(stdin.readLineSync()!);
  
  print("Informe o outro lado");
  l2 = int.parse(stdin.readLineSync()!);

  area = (l1 * l2) / 2;
  print('A area é: $area');
}
