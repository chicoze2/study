import 'dart:io';
//01) Desenvolver um programa que efetue a soma de dois números.

void main() {
  //Declarando as variáveis
  int numero;
  int posterior;

  //Definindo os valores de entrada
  print("Informe um valor numérico:");
  numero = int.parse(stdin.readLineSync()!);

  // Efetuando o processamento
  posterior = numero + 1;

  // Exibindo o resultado
  print("O valor posterior é: $posterior");
}
