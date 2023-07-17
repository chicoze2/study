import random  # Importa o módulo random para gerar números aleatórios
import time  # Importa o módulo time para criar atrasos

def lancamento_dados():
    resultado_lancamento = random.randrange(2, 13)  # Gera um número aleatório entre 2 e 12 (inclusive)
    return resultado_lancamento

def verificar_resultado(lancamento):
    if lancamento in [7, 11]:  # Se o resultado for 7 ou 11
        print("Você tirou: ", lancamento, "\nVocê é um natural e ganhou!")  # Imprime uma mensagem de vitória
    elif lancamento in [2, 3, 12]:  # Se o resultado for 2, 3 ou 12
        print("Você tirou: ", lancamento, "\n[Craps] VOCÊ PERDEU!")  # Imprime uma mensagem de derrota
    else:
        print("Você tirou: ", lancamento, "\nVocê ganhou um Ponto")  # Imprime uma mensagem informando que o jogador ganhou um ponto
        numero_tirado = lancamento  # Armazena o número do ponto que o jogador tirou inicialmente
        lancamento2 = True  # Variável para controlar o loop do jogo
        while numero_tirado != lancamento2:
            lancamento2 = random.randrange(2, 13)  # Gera um novo lançamento de dados
            if lancamento2 == 7:  # Se o novo lançamento for 7
                print("Você tirou: ", lancamento2, "\nVocê perdeu!")  # Imprime uma mensagem informando que o jogador perdeu
                break  # Sai do loop
            elif lancamento2 == numero_tirado:  # Se o novo lançamento for igual ao número do ponto
                print("Você tirou: ", lancamento2, "\nVocê tirou o mesmo número novamente. você GANHOU")  # Imprime uma mensagem informando que o jogador ganhou novamente
            else:
                print("Você tirou:", lancamento2, "\nJogando novamente em 2 segundos...")  # Imprime uma mensagem informando o novo lançamento de dados
                time.sleep(2)  # Aguarda 2 segundos antes do próximo lançamento

lancamento = lancamento_dados()  # Gera o resultado do lançamento de dados
verificar_resultado(lancamento)  # Verifica o resultado do jogo
