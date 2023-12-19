import pygame
from pygame.locals import *
import sys

import random

def jogar_pedra_papel_tesoura(jogada_usuario):
    opcoes = ['pedra', 'papel', 'tesoura']
    jogada_computador = random.choice(opcoes)

    print(f"Você escolheu: {jogada_usuario}")
    print(f"MarquesHTD escolheu: {jogada_computador}")

    if jogada_usuario == jogada_computador:
        return "Empate!"
    elif (
        (jogada_usuario == 'pedra' and jogada_computador == 'tesoura') or
        (jogada_usuario == 'papel' and jogada_computador == 'pedra') or
        (jogada_usuario == 'tesoura' and jogada_computador == 'papel')
    ):
        return "Você ganhou!"
    else:
        return "Você perdeu!"

if __name__ == "__main__":
    print("Bem-vindo ao Jogo Pedra, Papel e Tesoura!")

    while True:
        escolha = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()

        if escolha == 'sair':
            print("Obrigado por jogar. Até mais!")
            break
        elif escolha not in ['pedra', 'papel', 'tesoura']:
            print("Escolha inválida. Tente novamente.")
        else:
            resultado = jogar_pedra_papel_tesoura(escolha)
            print(resultado)

