import 'dart:io';
//05) Desenvolver um programa que solicite um valor numérico e informe o sucessor dele.

void main(){
  print("Digite um número: ");
  int num = int.parse(stdin.readLineSync()!);

  print("O número anterior é: ${num + 1}");
}
