import 'dart:io';

//15) Desenvolver um programa que leia um número e indique se ele é positivo, negativo ou zero.

void main() {
  int num;

  print("Informe um valor numerico");
  num = int.parse(stdin.readLineSync()!);

  if (num > 0) {
    print("O valor é positivo");
  } else if (num == 0) {
    print("O valor é zero");
  } else {
    print("O valor é negativo");
  }
}
